from client import Client
from repository import DB
from pydantic import ValidationError
from models import AirVisualModel


class GetDataFromDB(DB):
    def __init__(self) -> None:
        super().__init__()

    def data_from_db(self):
        return self.get_data_db()
    
    
class GetDataFromClient(Client, DB):
    def __init__(self) -> None:
        super().__init__()
        DB.__init__(self)

    def add_data_to_db(self):
        data = self.get_data_client()
        try:
            validated_data = AirVisualModel(**data)
            self.database.add_data(validated_data.dict())
        except ValidationError as e:
            print(f"Data validation failed: {e}")
    
