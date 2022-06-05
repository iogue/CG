from geometry.prism import PrismGeometry
from geometry.cylinder import CylinderGeometry
from material.surface import SurfaceMaterial
from core_ext.mesh import Mesh
from core_ext.texture import Texture
from material.texture import TextureMaterial



class TripeMesh(Mesh):
    def __init__(self):
       
        geometry0 = CylinderGeometry(radius=0.2,height=5)
        geometry = CylinderGeometry(radius=0.2,height=4)
        geometry1= PrismGeometry(radius=0.2,height=1.5,sides=4)
        geometry2= PrismGeometry(radius=0.2,height=4,sides=4)
        grid_texture = Texture(file_name="images/cimento.jpg")
        material = TextureMaterial(texture=grid_texture)
        
            
        self.mesh=super().__init__(geometry,material)

        mesh1 = Mesh(geometry, material)
        mesh2 = Mesh(geometry0, material)
        mesh3 = Mesh(geometry1, material)
        mesh4 = Mesh(geometry2, material)

        mesh1.translate(1.58,0.90,0) 
        mesh1.rotate_z(1)
        

        mesh2.translate(1,0.7,-2)
        mesh2.rotate_z(0.70)   
        mesh2.rotate_x(0.89)  

        mesh3.translate(0.3,1.5,0.3)
        mesh3.rotate_z(2.06)           
        mesh3.rotate_y(2.4)

        mesh4.translate(1.3,-0.5,0.3)
        mesh4.rotate_z(2.06)      
        mesh4.rotate_y(2.4) 
        

        self.add(mesh1) #pau da direita
        self.add(mesh2) #pau de tras
        self.add(mesh3) #prisma
        self.add(mesh4) #prismagrande
        self.rotate_z(-0.5)
        self.scale(0.7)
        
        