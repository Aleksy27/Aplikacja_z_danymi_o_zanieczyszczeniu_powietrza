class DB:
    def __init__(self) -> None:
        self.list = []

    def add_data(self, data):
        self.list.append(data)
    
    def get_data_db(self):
        return self.list