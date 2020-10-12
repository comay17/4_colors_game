from four_colors_game_builder import FourColorsGameBuilder

if __name__ == '__main__':
    game = FourColorsGameBuilder(18, 21, 4, ['red', 'blue', 'green', 'yellow']).build()
    game.run()
