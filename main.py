"""
import arcade

# Costanti che non cambiano mai
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "MetroidVania"

def main():
    # Apri la finestra
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    
    # Imposta lo sfondo
    arcade.set_background_color(arcade.color.SKY_BLUE)
    
    # Inizia a renderizzare
    arcade.start_render()
    
    # Scrivi qualcosa
    arcade.draw_text("Hello, Arcade!", 
                     SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                     arcade.color.WHITE, 40, anchor_x="center")
    
    # Finisci di renderizzare
    arcade.finish_render()
    
    # Fai partire il tutto e mantieni la finestra aperta
    arcade.run()

if __name__ == "__main__":
    main()
"""
"""
Platformer Game

python -m arcade.examples.platform_tutorial.01_open_window
"""
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Platformer"


class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.player_texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""
        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here
        arcade.draw_sprite(self.player_sprite)
    """
    def on_key_press(self, key, midifiers):
        if key == arcade.key.D:
            self.sprite.center_x += 10
        if key == arcade.key.A:
            self.sprite.center_x -= 10
        if key == arcade.key.SPACE:
            self.sprite.center_y += 10
    """
def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()