import wx
import pcbnew
import os
from .SpaceFillingCurveUI import SpaceFillingCurveUI
from .SpaceFillingCurveMethods import SpaceFillingCurveMethods

class SpaceFillingCurveInterface(SpaceFillingCurveUI):
    def __init__(self):
        super(SpaceFillingCurveInterface, self).__init__(None)
        self.SetTitle("Space-Filling Curve")
        self.order_spin.Bind(wx.EVT_TEXT, self.OnOrderChanged)
        self.ok_button.Bind(wx.EVT_BUTTON, self.OnOK)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.OnCancel)
        self.width_spin.Bind(wx.EVT_TEXT, self.OnWidthChanged)
        self.size_spin.Bind(wx.EVT_TEXT, self.OnSizeChanged)
        self.height_spin.Bind(wx.EVT_TEXT, self.OnHeightChanged)
        self.shape_combo.Bind(wx.EVT_COMBOBOX, self.OnShapeChanged)
        self.type_combo.Bind(wx.EVT_COMBOBOX, self.OnTypeChanged)
        self.curve_combo.Bind(wx.EVT_COMBOBOX, self.OnCurveChanged)


        self.order = self.order_spin.GetValue()
        self.shape = self.shape_combo.GetSelection()
        self.type = self.type_combo.GetSelection()
        self.curve = self.curve_combo.GetSelection()
        self.width = self.width_spin.GetValue()
        self.size = self.size_spin.GetValue()
        self.height = self.height_spin.GetValue()

        self.height_spin.Enable(False)
    

    def OnOrderChanged(self, event):
        self.order = event.GetEventObject().GetValue()
    def OnWidthChanged(self, event):
        self.width = event.GetEventObject().GetValue()
    def OnSizeChanged(self, event):
        self.size =event.GetEventObject().GetValue()
    def OnHeightChanged(self, event):
        self.height = event.GetEventObject().GetValue()
    def OnShapeChanged(self, event):
        self.shape = event.GetEventObject().GetSelection()
        self.set_curve_image(self.shape, self.type)
        if self.shape == 2:
            self.height_spin.Enable(True)
        else:
            self.height_spin.Enable(False)
    def OnTypeChanged(self, event):
        self.type = event.GetEventObject().GetSelection()
        self.set_curve_image(self.shape, self.type)
    def OnCurveChanged(self, event):
        self.curve = event.GetEventObject().GetSelection()
    def OnOK(self, event):

        self.space_filling_curve()


        
    def OnCancel(self, event):
        self.EndModal(wx.ID_CANCEL)
    def space_filling_curve(self):
        self.board = pcbnew.GetBoard()
        self.group=pcbnew.PCB_GROUP(self.board)
        fscm=SpaceFillingCurveMethods(self.board, self.group)
        fscm.draw_space_filling_curve(self.curve, self.type, self.shape, self.width,pcbnew.FromMM(self.size),pcbnew.FromMM(self.height), self.order)
        pcbnew.Refresh()
    def set_curve_image(self, shape, type):
        if shape == 2:  #如果是矩形
            shape=0  #则使用方形的图片

        image_path = os.path.join(os.path.dirname(__file__), "images", f"curve_{shape}_{type}.png")
        if not os.path.exists(image_path):
            image_path = os.path.join(os.path.dirname(__file__), "images", f"curve_0_0.png")
        new_image = wx.Image(image_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.shape_bitmap.SetBitmap(new_image)
        self.Layout()

