from window.menu import Menu
from data.data_handler import DataHandler


if __name__ == '__main__':
    # open window with dataS
    menu = Menu()
    data_handler = DataHandler()
    menu.open_window(data_handler)