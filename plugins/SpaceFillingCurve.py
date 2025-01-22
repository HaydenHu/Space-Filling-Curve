import os
import pcbnew
import math
from . import SpaceFillingCurveUI
from . import SpaceFillingCurveInterface
class SpaceFillingCurve(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Space-Filling Curve"
        self.category = "Modify PCB"
        self.description = "Create a space-filling curve"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "images", "curve.png")

    def Run(self):

        dialog = SpaceFillingCurveInterface.SpaceFillingCurveInterface()
        dialog.Show()
            
        
SpaceFillingCurve().register()
