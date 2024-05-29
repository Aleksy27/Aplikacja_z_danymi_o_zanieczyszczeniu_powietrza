from flask import Flask
from flask import jsonify
from flask.views import MethodView
from logic import GetDataFromDB


app = Flask(__name__)


class AirVisualApi(MethodView):
    def __init__(self):
        self.database = GetDataFromDB()

    def get(self):
        data = self.database.data_from_db()
        return jsonify(data)


app.add_url_rule('/', view_func=AirVisualApi.as_view(name='airvisualapi'))


if __name__ == "__main__":
    app.run(debug=True)