import os
import wx
class SpaceFillingCurveUI(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Space-Filling Curve", pos=wx.DefaultPosition,  style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.MAXIMIZE_BOX)

        gs = wx.FlexGridSizer(rows=7, cols=2, hgap=10, vgap=10)
        gs.AddGrowableCol(1)
        for i in range(7):
            gs.AddGrowableRow(i)
        main_sizer = wx.BoxSizer(wx.VERTICAL|wx.EXPAND)

        ref_image_sizer = wx.BoxSizer(wx.HORIZONTAL)

        ref_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        order_label = wx.StaticText(self, wx.ID_ANY, u"Order:")
        gs.Add(order_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        self.order_spin = wx.SpinCtrl(self, wx.ID_ANY, u"3", min=1, max=10)
        gs.Add(self.order_spin, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        width_label = wx.StaticText(self, wx.ID_ANY, u"Width:")
        gs.Add(width_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        self.width_spin = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 1.0, 0.1)
        gs.Add(self.width_spin, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        size_label = wx.StaticText(self, wx.ID_ANY, u"Size:")
        gs.Add(size_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        self.size_spin = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 100.0, 1)
        gs.Add(self.size_spin, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        hight_label = wx.StaticText(self, wx.ID_ANY, u"Height:")
        gs.Add(hight_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        self.height_spin = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 100.0, 1)
        gs.Add(self.height_spin, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        shape_label = wx.StaticText(self, wx.ID_ANY, u"Shape:")
        gs.Add(shape_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        self.shape_combo = wx.ComboBox(self, wx.ID_ANY, choices=[u"Square", u"Circle",u"Rectangle"], style=wx.CB_READONLY)
        self.shape_combo.SetSelection(0)
        gs.Add(self.shape_combo, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        type_label = wx.StaticText(self, wx.ID_ANY, u"Type:")
        gs.Add(type_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        self.type_combo = wx.ComboBox(self, wx.ID_ANY, choices=[u"Hilbert", u"Moore", u"Peano"], style=wx.CB_READONLY)
        self.type_combo.SetSelection(0)
        gs.Add(self.type_combo, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        curve_label = wx.StaticText(self, wx.ID_ANY, u"Curve:")
        gs.Add(curve_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)
        self.curve_combo = wx.ComboBox(self, wx.ID_ANY, choices=[u"Track", u"Line"], style=wx.CB_READONLY)
        self.curve_combo.SetSelection(0)
        gs.Add(self.curve_combo, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL| wx.EXPAND, 8)

        ref_box_sizer.Add(gs, 1, wx.ALL| wx.EXPAND, 5)
        ref_image_sizer.Add(ref_box_sizer, 1, wx.ALL| wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        shape_image = wx.Image(os.path.join(os.path.dirname(__file__), "images", "curve_0_0.png"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.shape_bitmap = wx.StaticBitmap(self, wx.ID_ANY, shape_image)
    
        ref_image_sizer.Add(self.shape_bitmap, 1, wx.ALL| wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
        

        main_sizer.Add(ref_image_sizer, 1, wx.ALL | wx.EXPAND, 5)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.cancel_button = wx.Button(self, wx.ID_CANCEL, u"Cancel")
        button_sizer.Add(self.cancel_button, 1,  wx.ALL |wx.EXPAND, 5)
        self.ok_button = wx.Button(self, wx.ID_OK, u"OK")
        button_sizer.Add(self.ok_button, 1,  wx.ALL |wx.EXPAND, 5)
        main_sizer.Add(button_sizer, 0, wx.ALL |wx.EXPAND, 5)
        self.SetSizer(main_sizer)
        self.Fit()
        self.SetMinSize(wx.Size(430, 460))
        self.Layout()