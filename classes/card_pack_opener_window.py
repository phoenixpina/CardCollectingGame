import arcade

class CardPackOpenerWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Card Pack Opener")
        self.start_view = None

    def setup(self, start_view):
        self.start_view = start_view
        self.show_view(self.start_view)
