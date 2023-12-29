from window.menu import Menu
from data.serializer import Serializer


if __name__ == '__main__':

    # load data
    data = Serializer.load_data_from_json()

    # open window with data
    menu = Menu()
    menu.open_window(data)
