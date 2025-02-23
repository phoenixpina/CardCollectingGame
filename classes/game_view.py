import os
import arcade
import random

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        #print("Current Working Directory:", os.getcwd())  # for debugging
        self.card_library = [
            "Dark Magician", "Blue Eyes White Dragon", "Elemental Hero Neos", "Stardust Dragon", 
            "Red Dragon Archfiend", "Utopia", "Odd Eyes Pendulum Dragon", "Superheavy Samurai Stealth Ninja", 
            "Clear Wing Synchro Dragon", "Decode Talker"
        ]
        self.cards_obtained = []
        self.pack_opened = False

        # Button size
        self.button_x = 300
        self.button_y = 30
        self.button_width = 200
        self.button_height = 30

        # Dictionary to hold card textures
        self.card_textures = {}
        for card in self.card_library:
            image_path = f"C:/Users/phoen/OneDrive/Documents/BYUI/2025 Winter/CSE310 (Applied Programming)/cse310/CardCollectingGame/card_images/{card.replace(' ', '_')}.jpg"
            #image_path = f"../card_images/{card.replace(' ', '_')}.jpg"
            #The above is the line of code that is supposed to work... but it isn't working. Only the absolute path is working and I don't know why.
            #I understand that the absolute path does not work on code pulled from GitHub, and the program will not function.
            #print("Full image path:", os.path.abspath(image_path))  #for debugging
            self.card_textures[card] = arcade.load_texture(image_path)

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)

    def on_draw(self):
        self.clear()

        # Start screen
        arcade.draw_text("Card Pack Opener", self.window.width // 2, 550, arcade.color.WHITE, font_size=24, anchor_x="center")

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
            arcade.draw_text("You opened:", self.window.width // 2, 450, arcade.color.WHITE, font_size=20, anchor_x="center")
            
            # Sets spacing for the cards
            card_width = 100
            card_height = 150
            padding = 60  # Space between cards
            max_per_row = 3  # Number of cards per row

            # Iterates through the obtained cards and displays them
            for index, card in enumerate(self.cards_obtained):
                row = index // max_per_row
                col = index % max_per_row

                # Calculates position for the card
                x = self.window.width // 2 - (card_width * max_per_row // 2) + col * (card_width + padding)
                y = 350 - row * (card_height + padding)

                # Draw the card texture
                card_texture = self.card_textures.get(card)
                if card_texture:
                    arcade.draw_texture_rectangle(x, y, card_width, card_height, card_texture)

                # Display the card name underneath the image
                arcade.draw_text(f"- {card}", x, y - card_height // 2 - 10, arcade.color.YELLOW, font_size=14, anchor_x="center")

    def on_mouse_press(self, x, y, _button, _modifiers):
        # Ensures the button activates only when the mouse clicks in the button
        if (self.button_x < x < self.button_x + self.button_width and
            self.button_y < y < self.button_y + self.button_height):
            self.cards_obtained = self.open_master_pack()
            self.pack_opened = True  # Ensures only one pack opens

    def open_master_pack(self):
        return random.sample(self.card_library, k=5)  # No duplicate cards will be pulled
