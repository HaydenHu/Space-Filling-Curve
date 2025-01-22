import os
import pcbnew
import math

class SpaceFillingCurveMethods:
    def __init__(self, board, group):
        self.board = board
        self.group = group

    def draw_segment(self,start, end, width,curve, layer=pcbnew.F_Cu):
        if curve==0:
            segment = pcbnew.PCB_TRACK(self.board)
        elif curve==1:
            segment = pcbnew.PCB_SHAPE(self.board)
        else:
            segment = pcbnew.PCB_TRACK(self.board)
        segment.SetStart(start)
        segment.SetEnd(end)
        segment.SetLayer(layer)
        segment.SetWidth(pcbnew.FromMM(width))
        return segment
    def hilbert_curve(self, x, y, xi, xj, yi, yj, n):
        if n <= 0:
            return [(x + (xi + yi) // 2, y + (xj + yj) // 2)]
        else:
            points = []
            points.extend(self.hilbert_curve(x, y, yi // 2, yj // 2, xi // 2, xj // 2, n - 1))
            points.extend(self.hilbert_curve(x + xi // 2, y + xj // 2, xi // 2, xj // 2, yi // 2, yj // 2, n - 1))
            points.extend(self.hilbert_curve(x + xi // 2 + yi // 2, y + xj // 2 + yj // 2, xi // 2, xj // 2, yi // 2, yj // 2, n - 1))
            points.extend(self.hilbert_curve(x + xi // 2 + yi, y + xj // 2 + yj, -yi // 2, -yj // 2, -xi // 2, -xj // 2, n - 1))
            return points
        
    def lowd_square_to_disk(self, x, y):
        a = 2 * x - 0
        b = 2 * y - 0

        if a == 0 and b == 0:
            r = theta = 0
        elif a * a > b * b:
            r = a
            theta = (math.pi / 4) * (b / a)
        else:
            r = b
            theta = (math.pi / 2) - ((math.pi / 4) * (a / b))


        x_out = r * math.cos(theta)
        y_out = r * math.sin(theta)

        return (x_out, y_out)

    def add2group(self, item,group):
        
        
        # for i in self.board.Groups():
        #     if i.GetName() == "Space-Filling Curve":
        #         break
        group.SetName("Space-Filling Curve")
        group.AddItem(item)
        return group
    def square_to_disk(self,points):
        # 平移原点到中心
        x, y = zip(*points)
        x_center = (max(x) + min(x)) / 2
        y_center = (max(y) + min(y)) / 2
        x = [(xi - x_center)/2 for xi in x] #缩放一下，边长变为内切圆直径
        y = [(yi - y_center)/2 for yi in y]

        # 将点映射到圆形轮廓
        mapped_points = []
        total_mapped_length = 0.0
        
        for xi, yi in zip(x, y):
            mapped_x, mapped_y = self.lowd_square_to_disk(xi, yi)
            
            # 计算映射后的线段长度 (如果是第一个点则跳过)
            if mapped_points:
                prev_mapped_x, prev_mapped_y = mapped_points[-1]
                mapped_length = math.sqrt((mapped_x - prev_mapped_x) ** 2 + (mapped_y - prev_mapped_y) ** 2)
                total_mapped_length += mapped_length
            
            mapped_points.append((mapped_x, mapped_y))
        return mapped_points

    def draw_space_filling_curve(self,curve,type, shape,width, size,height, order):
        if type==0:
            # x, y = self.hilbert(size, order)
            points = self.hilbert_curve(0, 0, size, 0, 0, size, order)
            
        elif type==1:
            scale_size = 1/(2**order)*size 
            x, y = self.moore(scale_size, order)
            points = list(zip(x, y))
            
        elif type==2:
            x, y=self.peano( size, order-1)
            points = list(zip(x, y))
            
        else:
            pass
        # 是否映射到圆形轮廓
        if shape==1:
            mapped_points = self.square_to_disk(points)
            x, y = zip(*mapped_points)
        elif shape==2:  #如果是矩形，把方形映射成矩形
            points = [(xi,yi*height/size) for xi,yi in points]
            x, y = zip(*points)
        else:
            x, y = zip(*points)
        for i in range(len(x) - 1):
            curve=self.draw_segment(pcbnew.VECTOR2I(int(x[i]), int(y[i])), pcbnew.VECTOR2I(int(x[i+1]), int(y[i+1])),width,curve)
            group=self.add2group(curve,self.group)
            self.board.Add(curve)
            self.board.Add(group)
    def _hilbert(self, direction, rotation, size, order):
        if order == 0:
            return

        direction += rotation
        self._hilbert(direction, -rotation,size, order - 1)
        self.step(direction,size)

        direction -= rotation
        self._hilbert(direction, rotation, size,order - 1)
        self.step(direction,size)
        self._hilbert(direction, rotation,size, order - 1)

        direction -= rotation
        self.step(direction,size)
        self._hilbert(direction, -rotation,size, order - 1)

    def step(self, direction, scale=1):
        next = {0: (scale, 0), 1: (0, scale), 2: (-scale, 0), 3: (0, -scale)}[direction & 0x3]

        global x, y
        x.append(x[-1] + next[0])
        y.append(y[-1] + next[1])


    def hilbert(self, size, order):
        global x, y
        x = [0,]
        y = [0,]
        self._hilbert(0, 1, size,order)
        return (x, y)
        
    def _moore(self, direction, rotation, size, order):
        if order == 0:
            return
        direction -= rotation
        self._hilbert(direction, rotation,size,order - 1)
        self.step(direction,size)
        self._hilbert(direction, rotation, size,order - 1)

        direction -= rotation
        self.step(direction,size)
        direction -= rotation
        self._hilbert(direction, rotation, size,order - 1)
        self.step(direction,size)
        self._hilbert(direction, rotation, size,order - 1)

    def moore(self, size, order):
        global x, y
        x = [2**(order-1)-1,]
        y = [0,]
        self._moore(2, 1, size,order)
        return (x, y)
    def peano_curve(self, x, y, size, n, pattern=0):
        """
        生成Peano曲线的点序列
        参数:
            x, y: 起始坐标
            size: 当前正方形的大小
            n: 递归深度
            pattern: S形状的模式
                0: 基本S形状（从左下到右上）
                1: 水平翻转（从右下到左上）
                2: 垂直翻转（从左上到右下）
                3: 水平+垂直翻转（从右上到左下）
        """
        if n == 0:
            return [(x, y)]
        
        points = []
        size /= 3

        # 定义4种模式
        if pattern == 0:  # 基本S形状
            sequence = [
                ((0, 0), 0), ((1, 0), 1), ((2, 0), 0),
                ((2, 1), 1), ((1, 1), 0), ((0, 1), 1),
                ((0, 2), 0), ((1, 2), 1), ((2, 2), 0)
            ]
        elif pattern == 1:  # 水平翻转
            sequence = [
                ((2, 0), 1), ((1, 0), 0), ((0, 0), 1),
                ((0, 1), 0), ((1, 1), 1), ((2, 1), 0),
                ((2, 2), 1), ((1, 2), 0), ((0, 2), 1)
            ]
        elif pattern == 2:  # 垂直翻转
            sequence = [
                ((0, 2), 2), ((1, 2), 3), ((2, 2), 2),
                ((2, 1), 3), ((1, 1), 2), ((0, 1), 3),
                ((0, 0), 2), ((1, 0), 3), ((2, 0), 2)
            ]
        else:  # pattern == 3
            sequence = [
                ((2, 2), 3), ((1, 2), 2), ((0, 2), 3),
                ((0, 1), 2), ((1, 1), 3), ((2, 1), 2),
                ((2, 0), 3), ((1, 0), 2), ((0, 0), 3)
            ]

        # 遍历每个子块
        for index, ((dx, dy), next_pattern) in enumerate(sequence):
            next_x = x + dx * size
            next_y = y + dy * size
            sub_points = self.peano_curve(next_x, next_y, size, n - 1, next_pattern)

            # 调整反转逻辑
            if (index%3) == 1:  # 奇数层
                sub_points = sub_points[::-1]

            points.extend(sub_points)
        
        return points    
    def peano(self, size, order):
        global x, y
        x = [0,]
        y = [0,]
        points = self.peano_curve(0, 0, size, order)
        x, y = zip(*points)
        return (x, y)

