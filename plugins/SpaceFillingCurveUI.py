import os
import wx
class SpaceFillingCurveUI(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Space-Filling Curve", pos=wx.DefaultPosition, size=wx.Size(430, 360), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        ref_image_sizer = wx.BoxSizer(wx.HORIZONTAL)

        ref_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        left_txt_sizer = wx.BoxSizer(wx.VERTICAL)
        right_spin_sizer = wx.BoxSizer(wx.VERTICAL)
        order_label = wx.StaticText(self, wx.ID_ANY, u"Order:")
        left_txt_sizer.Add(order_label, 0, wx.ALL, 8)
        width_label = wx.StaticText(self, wx.ID_ANY, u"Width:")
        left_txt_sizer.Add(width_label, 0, wx.ALL, 8)
        size_label = wx.StaticText(self, wx.ID_ANY, u"Size:")
        left_txt_sizer.Add(size_label, 0, wx.ALL, 8)
        hight_label = wx.StaticText(self, wx.ID_ANY, u"Height:")
        left_txt_sizer.Add(hight_label, 0, wx.ALL, 8)
        shape_label = wx.StaticText(self, wx.ID_ANY, u"Shape:")
        left_txt_sizer.Add(shape_label, 0, wx.ALL, 8)
        type_label = wx.StaticText(self, wx.ID_ANY, u"Type:")
        left_txt_sizer.Add(type_label, 0, wx.ALL, 8)
        curve_label = wx.StaticText(self, wx.ID_ANY, u"Curve:")
        left_txt_sizer.Add(curve_label, 0, wx.ALL, 8)
        ref_box_sizer.Add(left_txt_sizer, 0, wx.ALL, 5)

    

        self.order_spin = wx.SpinCtrl(self, wx.ID_ANY, u"3", min=1, max=10)
        right_spin_sizer.Add(self.order_spin, 0, wx.EXPAND | wx.ALL, 5)
        self.width_spin = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 1.0, 0.1)
        right_spin_sizer.Add(self.width_spin, 0, wx.EXPAND | wx.ALL, 5)
        self.size_spin = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 100.0, 1)
        self.size_spin.SetToolTip(u"width or diameter of shape")
        right_spin_sizer.Add(self.size_spin, 0, wx.EXPAND | wx.ALL, 5)
        self.height_spin = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 100.0, 1)
        right_spin_sizer.Add(self.height_spin, 0, wx.EXPAND | wx.ALL, 5)
        self.shape_combo = wx.ComboBox(self, wx.ID_ANY, choices=[u"Square", u"Circle",u"Rectangle"], style=wx.CB_READONLY)
        self.shape_combo.SetSelection(0)
        right_spin_sizer.Add(self.shape_combo, 0, wx.EXPAND | wx.ALL, 5)
        self.type_combo = wx.ComboBox(self, wx.ID_ANY, choices=[u"Hilbert", u"Moore", u"Peano"], style=wx.CB_READONLY)
        self.type_combo.SetSelection(0)
        right_spin_sizer.Add(self.type_combo, 0, wx.EXPAND | wx.ALL, 5)
        self.curve_combo = wx.ComboBox(self, wx.ID_ANY, choices=[u"Track", u"Line"], style=wx.CB_READONLY)
        self.curve_combo.SetSelection(0)
        right_spin_sizer.Add(self.curve_combo, 0, wx.EXPAND | wx.ALL, 5)
       
        ref_box_sizer.Add(right_spin_sizer, 0, wx.ALL, 5)
        ref_image_sizer.Add(ref_box_sizer, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        shape_image = wx.Image(os.path.join(os.path.dirname(__file__), "images", "curve_0_0.png"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.shape_bitmap = wx.StaticBitmap(self, wx.ID_ANY, shape_image)
    
        ref_image_sizer.Add(self.shape_bitmap, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        

        main_sizer.Add(ref_image_sizer, 0, wx.ALL | wx.EXPAND, 5)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.cancel_button = wx.Button(self, wx.ID_CANCEL, u"Cancel")
        button_sizer.Add(self.cancel_button, 1,  wx.ALL |wx.EXPAND, 5)
        self.ok_button = wx.Button(self, wx.ID_OK, u"OK")
        button_sizer.Add(self.ok_button, 1,  wx.ALL |wx.EXPAND, 5)
        main_sizer.Add(button_sizer, 0, wx.ALL |wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()