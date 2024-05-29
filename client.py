import requests 


class Client:
    def __init__(self) -> None:
        self.basic_url = "http://api.airvisual.com/v2/"
        self.city = "Dallas"
        self.state = "Texas"
        self.country = "USA"
        self.key = "81fea959-75e8-4eea-8df7-ef9a3e964bf2"

    def get_data_client(self):
        url = f"{self.basic_url}city?city={self.city}&state={self.state}&country={self.country}&key={self.key}"
        response = requests.get(url)
        data = response.json()
        print(data)
        return data
    

if __name__ == "__main__":
    Client().get_data_client()