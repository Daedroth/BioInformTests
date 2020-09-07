class MainMenu:

    def __init__(self):
        self.mainMenu = {1: 'Get Nucleotide Info', 2: 'Overlap Graphs', 3: 'Exit'}

    def show_main_menu(self) -> int:
        print('****Main Menu****')
        print('Please select needed functionality\n')

        for key in self.mainMenu:
            print(key, ')', self.mainMenu[key], '\n')

        menu_item = int(input('Menu № - '))

        return menu_item
