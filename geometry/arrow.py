from core_ext.mesh import Mesh
from core_ext.texture import Texture

from math import pi

from geometry.box import BoxGeometry
from geometry.cylinder import CylinderGeometry
from geometry.plane import PlaneGeometry
from geometry.polygon import PolygonGeometry
from geometry.pyramid import PyramidGeometry
from geometry.sphere import SphereGeometry

from material.texture import TextureMaterial

class ArrowMesh(Mesh):
    def __init__(self):
        geometry1 = CylinderGeometry(radius=0.075, height=3, height_segments=1)
        geometry2 = PyramidGeometry(radius=0.2, height=0.5, sides=4, height_segments=1)
        geometry3 = PlaneGeometry()
        geometry4 = PolygonGeometry(sides=30, radius=0.1)
        geometry5 = CylinderGeometry(radius=0.65, height=0.5, closed=False)
        geometry6 = PolygonGeometry(sides=30, radius=0.1)
        geometry7 = SphereGeometry()
        geometry8 = SphereGeometry()
        geometry9 = SphereGeometry()
        geometry10 = SphereGeometry()
        geometry11 = SphereGeometry()
        geometry12 = SphereGeometry()
        geometry13 = SphereGeometry()
        geometry14 = BoxGeometry(height=2.25)
        geometry15 = PlaneGeometry(height=0.525, width=0.75/3)
        geometry16 = PlaneGeometry(height=0.525, width=0.75/3)
        geometry17 = PyramidGeometry(radius=0.1, height=0.5, sides=4, height_segments=1)
        geometry18 = PyramidGeometry(radius=0.175, height=0.1, sides=4, height_segments=1)
        geometry19 = CylinderGeometry(radius=0.025, height=0.5, closed=False)
        geometry20 = CylinderGeometry(radius=0.025, height=0.5, closed=False)
        geometry21 = CylinderGeometry(radius=0.025, height=0.5, closed=False)
        geometry22 = CylinderGeometry(radius=0.025, height=0.5, closed=False)
        geometry23 = PlaneGeometry(height=0.525, width=0.75/3)
        geometry24 = PlaneGeometry(height=0.525, width=0.75/3)

        primMetal = TextureMaterial(Texture("images/metal.jpg"))
        secMetal = TextureMaterial(Texture("images/sec-metal.jpg"), property_dict={"repeatUV": [5, 5]})
        wood = TextureMaterial(Texture("images/wood.jpg"))
        white = TextureMaterial(Texture("images/white.jpg"), property_dict={"doubleSide": True})
        
        self.mesh1 = super().__init__(geometry1,wood)

        self.mesh2 = Mesh(geometry2, primMetal)
        self.mesh2.translate(0.0,1.75,0.0)

        self.mesh3 = Mesh(geometry3, primMetal)
        self.mesh3.translate(0.0,1.5001,0.0)
        self.mesh3.rotate_x(pi/2)
        self.mesh3.rotate_z(pi/4)
        self.mesh3.scale(0.28)
        
        self.mesh4 = Mesh(geometry4, wood)
        self.mesh4.translate(0.0,-1.5,0.0)
        self.mesh4.rotate_x(pi/2)
        self.mesh4.scale(0.75)

        self.mesh5 = Mesh(geometry5, secMetal)
        self.mesh5.translate(0.0,1.45,0.0)
        self.mesh5.scale(0.2)
        
        self.mesh6 = Mesh(geometry6, primMetal)
        self.mesh6.translate(0.0,1.4,0.0)
        self.mesh6.rotate_x(pi/2)
        self.mesh6.scale(1.3075)

        self.mesh7 = Mesh(geometry7, secMetal)
        self.mesh7.translate(0.0,1.15,0.0)
        self.mesh7.scale(0.09)

        self.mesh8 = Mesh(geometry8, secMetal)
        self.mesh8.translate(0.0,-0.875,0.0)
        self.mesh8.scale(0.09)

        self.mesh9 = Mesh(geometry9, secMetal)
        self.mesh9.translate(0.0,-1.0,0.0)
        self.mesh9.scale(0.0825)

        self.mesh10 = Mesh(geometry10, secMetal)
        self.mesh10.translate(0.0,-1.1,0.0)
        self.mesh10.scale(0.0825)

        self.mesh11 = Mesh(geometry11, secMetal)
        self.mesh11.translate(0.0,-1.2,0.0)
        self.mesh11.scale(0.0825)

        self.mesh12 = Mesh(geometry12, secMetal)
        self.mesh12.translate(0.0,-1.3,0.0)
        self.mesh12.scale(0.0825)

        self.mesh13 = Mesh(geometry13, secMetal)
        self.mesh13.translate(0.0,-1.4,0.0)
        self.mesh13.scale(0.0825)

        self.mesh14 = Mesh(geometry14, primMetal)
        self.mesh14.translate(0.0,1.3,0.0)
        self.mesh14.scale(0.125)

        self.mesh15 = Mesh(geometry15, white)
        self.mesh15.translate(-0.2,-1.135,0.0)
        
        self.mesh16 = Mesh(geometry16, white)
        self.mesh16.translate(0.0,-1.135,-0.2)
        self.mesh16.rotate_y(pi/2)

        self.mesh17 = Mesh(geometry17, primMetal)
        self.mesh17.translate(0.0,1.15,0.0)
        self.mesh17.rotate_x(pi)

        self.mesh18 = Mesh(geometry18, primMetal)
        self.mesh18.translate(0.0,1.46,0.0)
        self.mesh18.rotate_x(pi)

        self.mesh19 = Mesh(geometry19, primMetal)
        self.mesh19.translate(0.0575,-1.15,0.0)

        self.mesh20 = Mesh(geometry20, primMetal)
        self.mesh20.translate(-0.0575,-1.15,0.0)

        self.mesh21 = Mesh(geometry21, primMetal)
        self.mesh21.translate(0.0,-1.15,0.0575)

        self.mesh22 = Mesh(geometry22, primMetal)
        self.mesh22.translate(0.0,-1.15,-0.0575)

        self.mesh23 = Mesh(geometry23, white)
        self.mesh23.translate(0.2,-1.135,0.0)
        
        self.mesh24 = Mesh(geometry24, white)
        self.mesh24.translate(0.0,-1.135,0.2)
        self.mesh24.rotate_y(pi/2)


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
        self.add(self.mesh13)
        self.add(self.mesh14)
        self.add(self.mesh15)
        self.add(self.mesh16)
        self.add(self.mesh17)
        self.add(self.mesh18)
        self.add(self.mesh19)
        self.add(self.mesh20)
        self.add(self.mesh21)
        self.add(self.mesh22)
        self.add(self.mesh23)
        self.add(self.mesh24)

        self.scale(0.4)
        