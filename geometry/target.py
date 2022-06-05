from math import pi
from material.texture import TextureMaterial
from core_ext.mesh import Mesh
from core_ext.texture import Texture
from geometry.polygon import PolygonGeometry
from geometry.cylindrical import CylindricalGeometry
from material.surface import SurfaceMaterial

class TargetMesh(Mesh):
    def __init__(self):
        geometry = CylindricalGeometry(height=0.1, height_segments=2, radial_segments=100, closed_bottom=False, closed_top=False)
        geometry1 = PolygonGeometry(sides=100)
        geometry2 = PolygonGeometry(sides=100)
        geometry3 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.85, radius_bottom=0.825, closed_bottom=False, closed_top=False)
        geometry4 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.85, radius_bottom=0.85, closed_bottom=False, closed_top=False)
        geometry5 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.685, radius_bottom=0.66, closed_bottom=False, closed_top=False)
        geometry6 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.685, radius_bottom=0.685, closed_bottom=False, closed_top=False)
        geometry7 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.55, radius_bottom=0.55, closed_bottom=False, closed_top=False)
        geometry8 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.55, radius_bottom=0.525, closed_bottom=False, closed_top=False)
        geometry9 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.38, radius_bottom=0.35, closed_bottom=False, closed_top=False)
        geometry10 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.38, radius_bottom=0.38, closed_bottom=False, closed_top=False)
        geometry11 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.23, radius_bottom=0.23, closed_bottom=False, closed_top=False)
        geometry12 = CylindricalGeometry(height=0.02, height_segments=1, radial_segments=100, radius_top=0.23, radius_bottom=0.205, closed_bottom=False, closed_top=False)

        madeira = TextureMaterial(Texture(file_name="images/madeira.jpg"))
        alvo = TextureMaterial(Texture(file_name="images/alvo.jpg"))
        red = TextureMaterial(Texture(file_name="images/red.jpg"))
        white = TextureMaterial(Texture(file_name="images/clear_white.jpg"))
        

        self.mesh = super().__init__(geometry,madeira)
        self.mesh1 = Mesh(geometry1, madeira)
        self.mesh2 = Mesh(geometry2, alvo)
        self.mesh3 = Mesh(geometry3, red)
        self.mesh4 = Mesh(geometry4, red)
        self.mesh5 = Mesh(geometry5, white)
        self.mesh6 = Mesh(geometry6, white)
        self.mesh7 = Mesh(geometry7, red)
        self.mesh8 = Mesh(geometry8, red)
        self.mesh9 = Mesh(geometry9, white)
        self.mesh10 = Mesh(geometry10, white)
        self.mesh11 = Mesh(geometry11, red)
        self.mesh12 = Mesh(geometry12, red)
        
        self.mesh1.rotate_x(pi/2)
        self.mesh2.rotate_x(-pi/2)
        
        self.mesh1.translate(0,0,0.05)
        self.mesh2.translate(0,0,0.05)
        self.mesh3.translate(0,0.06,0)
        self.mesh4.translate(0,0.06,0)
        self.mesh5.translate(0,0.06,0)
        self.mesh6.translate(0,0.06,0)
        self.mesh7.translate(0,0.06,0)
        self.mesh8.translate(0,0.06,0)
        self.mesh9.translate(0,0.06,0)
        self.mesh10.translate(0,0.06,0)
        self.mesh11.translate(0,0.06,0)
        self.mesh12.translate(0,0.06,0)


        self.add(self.mesh1)
        self.add(self.mesh2)
        self.add(self.mesh3)
        self.add(self.mesh4)
        self.add(self.mesh5)
        self.add(self.mesh6)
        self.add(self.mesh7)
        self.add(self.mesh8)
        self.add(self.mesh9)
        self.add(self.mesh10)
        self.add(self.mesh11)
        self.add(self.mesh12)

        self.scale(0.675)
        