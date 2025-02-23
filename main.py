import arcade
from classes.start_view import StartView
from classes.card_pack_opener_window import CardPackOpenerWindow

def main():
    window = CardPackOpenerWindow()
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
