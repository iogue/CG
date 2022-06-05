"""Realizado por Diogo Batista"""
from core_ext.mesh import Mesh
from core_ext.texture import Texture

from geometry.rectangle import RectangleGeometry

from material.texture import TextureMaterial
from extras.text_texture import TextTexture

class GameOver(Mesh):
    def __init__(self):
        geometry = RectangleGeometry(1.5, 1)
        grid_texture = Texture(file_name="images/mainpage.jpg")
        material = TextureMaterial(texture=grid_texture)
        self.mesh = Mesh(
            geometry=geometry,
            material=material
        )

        geometry1 = RectangleGeometry(0.75,0.25)
        message1 = TextTexture(text="You Lost",
                               font_file_name="fonts/ALGER.TTF",
                               background_color=[255,255,255,0],
                               font_size=40, font_color=[255, 255, 255],
                               image_width=768, image_height=256,
                               align_horizontal=0.5, align_vertical=0.5,
                               image_border_width=0)
        material1 = TextureMaterial(message1)
        self.mesh1 = Mesh(geometry1, material1)

        geometry2 = RectangleGeometry(0.75,0.25)
        message2 = TextTexture(text="Press [R] to restart or [Esc] to quit",
                               font_file_name="fonts/ALGER.TTF",
                               background_color=[255,255,255,0],
                               font_size=32, font_color=[255, 255, 255],
                               image_width=768, image_height=256,
                               align_horizontal=0.5, align_vertical=0.5,
                               image_border_width=0)
        material2 = TextureMaterial(message2)
        self.mesh2 = Mesh(geometry2, material2)

        geometry3 = RectangleGeometry(0.75,0.25)
        message3 = TextTexture(text="Game Over",
                               font_file_name ="fonts/Wide Latin Regular.ttf",
                               background_color=[255,255,255,0],
                               font_size=50, font_color=[255, 255, 255],
                               image_width=768, image_height=192,
                               align_horizontal=0.5, align_vertical=0.5,
                               image_border_width=0)
        material3 = TextureMaterial(message3)
        self.mesh3 = Mesh(geometry3, material3)
        
        self.mesh = super().__init__(geometry,material)
        self.mesh1 = Mesh(geometry1, material1)
        self.mesh1.translate(0,0,0.05)

        self.mesh2 = Mesh(geometry2, material2)
        self.mesh2.translate(0,-0.1,0.05)

        self.mesh3 = Mesh(geometry3, material3)
        self.mesh3.translate(0,0.25,0.05)

        self.add(self.mesh1)
        self.add(self.mesh2)
        self.add(self.mesh3)