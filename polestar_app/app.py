# from db.models import create_app
from db.models import db, app
from flask_restful import Resource, Api
from resources.csv import CSVResource
from resources.imo import IMOResource
from resources.position import PositionResource
from resources.ship import ShipResource
from utils.logger import log
from flask_cors import CORS
import os
import sys

# app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = "dlka34j90(&83nan341!#3d"

api = Api(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

class health(Resource):
    def get(self):
        # return "Hello World!", 200, {'Access-Control-Allow-Origin': '*'}
        return "Hello World!", 200



# register APIs
## my internal api's
api.add_resource(health, "/test/")
api.add_resource(CSVResource, "/api/init_db/")
api.add_resource(ShipResource, "/api/shipsdata/")

## asked in assignment
api.add_resource(IMOResource, "/api/ships/")
api.add_resource(PositionResource, "/api/positions/<int:imo>")


def create_app():
    # app = Flask(__name__)
    db.create_all()
    db.init_app(app)
    return app

if __name__ == "__main__":
    # from db import db
    # db.init_app(app)
    # wipe_all_db_files()
    default_port = 8010
    try:
        app = create_app()
        if len(sys.argv) == 2:
            port = int(sys.argv[1])
            app.run(host="0.0.0.0", port=port, debug=True)
        else:
            app.run(host="0.0.0.0", port=default_port, debug=True)
    except Exception as e:
        log.exception(e)

