import arcade
from classes.game_view import GameView

class StartView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Card Pack Opener", 400, 350,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Click to start", 400, 250,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)
