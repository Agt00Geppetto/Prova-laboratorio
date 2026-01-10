import arcade
import os
# from arcade import *

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.p1 = None
        self.lista_p1 = arcade.SpriteList()

        self.setup()

    def setup(self):
        self.p1 = arcade.Sprite("./assets/Geppetto.png")
        self.p1.center_x = 100
        self.p1.center_y = 215
        self.p1.scale = 0.5
        self.lista_p1.append(self.p1)

        self.background = arcade.load_texture("./assets/sfondoG.jpg")

    def on_draw(self):
        self.clear() 
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0,0,800,800)
        ) 
        self.lista_p1.draw()
        
    def on_update(self, delta_time):
        self.lista_p1.update()

    def on_key_press(self, tasto, modificatori):
        if tasto == arcade.key.SPACE:
            self.p1.change_y += 5 
        elif tasto == arcade.key.A:
            self.p1.change_x -= 5
        elif tasto == arcade.key.D:
            self.p1.change_x += 5

    def on_key_release(self, tasto, modificatori):
        if tasto in (arcade.key.SPACE):
            self.p1.change_y -= self.p1.change_y
        elif tasto in (arcade.key.A, arcade.key.D):
            self.p1.change_x = 0


def main():
    game = MyGame(
        800, 800, "Il mio giochino"
    )
    arcade.run()


if __name__ == "__main__":
    main()