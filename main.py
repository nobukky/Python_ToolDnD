from window.window import Window
from data.serializer import Serializer


if __name__ == '__main__':

    # load data
    data = Serializer.load_data_from_json()

    # open window with data
    window = Window()
    window.open_window(data)
