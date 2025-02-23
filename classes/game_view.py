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
        self.cards_obtained = []
        self.pack_opened = False

        # Button size
        self.button_x = 300
        self.button_y = 250
        self.button_width = 200
        self.button_height = 50

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)

    def on_draw(self):
        self.clear()

        # Start screen
        arcade.draw_text("Card Pack Opener", self.window.width // 2, 550,
                         arcade.color.WHITE, font_size=24, anchor_x="center")

        # Draws the "Open Pack" button
        arcade.draw_rectangle_filled(self.button_x + self.button_width // 2, 
                                     self.button_y + self.button_height // 2, 
                                     self.button_width, self.button_height, 
                                     arcade.color.GRAY_BLUE)
        arcade.draw_text("Open Pack", self.button_x + self.button_width // 2, 
                         self.button_y + self.button_height // 2, 
                         arcade.color.WHITE, font_size=20, anchor_x="center", anchor_y="center")

        # Displays obtained cards
        if self.pack_opened:
            arcade.draw_text("You opened:", self.window.width // 2, 450,
                             arcade.color.WHITE, font_size=20, anchor_x="center")
            for index, card in enumerate(self.cards_obtained):
                arcade.draw_text(f"- {card}", self.window.width // 2, 400 - index * 30,
                                 arcade.color.YELLOW, font_size=16, anchor_x="center")

    def on_mouse_press(self, x, y, _button, _modifiers):
        # Ensures the button activates only when the mouse clicks in the button
        if (self.button_x < x < self.button_x + self.button_width and
            self.button_y < y < self.button_y + self.button_height):
            self.cards_obtained = self.open_master_pack()
            self.pack_opened = True  # Ensures only one pack opens

    def open_master_pack(self):
        return random.sample(self.card_library, k=10)  # No duplicate cards will be pulled
