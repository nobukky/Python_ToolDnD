from data.serializer import Serializer


class DataHandler:

    def __init__(self):
        self.data = Serializer.load_data_from_json()

    def save(self):
        """
        Save the data using the 'Serializer' class
        """
        Serializer.save_data_to_json(self.data)