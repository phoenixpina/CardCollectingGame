import arcade
import random

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.card_library = [
            "Dragon Warrior", "Mystic Elf", "Fire Sorcerer", "Water Knight", 
            "Shadow Beast", "Thunder Hawk", "Earth Golem", "Wind Spirit", 
            "Light Paladin", "Dark Assassin"
        ]

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Choose a Pack to Open", 400, 550,
                         arcade.color.WHITE, font_size=24, anchor_x="center")
        arcade.draw_text("Click to open Master Pack", 400, 300,
                         arcade.color.YELLOW, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        cards_obtained = self.open_master_pack()
        print("You obtained the following cards:")
        for card in cards_obtained:
            print(f"- {card}")

    def open_master_pack(self):
        return random.choices(self.card_library, k=10)
