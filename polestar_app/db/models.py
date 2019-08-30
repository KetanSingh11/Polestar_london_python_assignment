from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DATABASE = 'polestar_db.db'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "dlka34j90(&83nan341!#3d"

db = SQLAlchemy(app)

class IMO(db.Model):
    """ International Maritime Organisation (IMO) numbers """
    __tablename__ = 'imo'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"IMO: <id={self.id}, name={self.name}>"

    def to_json(self):
        return {'imo': self.id, 'name': self.name}


class ShipData(db.Model):
    """ contains live ship locations (latitudes, longitude) """
    __tablename__ = 'shipdata'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    imo_id = db.Column(db.Integer, db.ForeignKey('imo.id'), nullable=False)
    datetimestamp = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    #relationship
    imo = db.relationship("IMO", backref="imo")

    def __repr__(self):
        return f"<ShipData: id={self.id}, date={self.datetimestamp}, latitude={self.latitude}, longitude={self.longitude}>"

    def to_json(self):
        return {'id': self.id, 'imo_id': self.imo_id, 'date': str(self.datetimestamp),
                'latitude': self.latitude, 'longitude': self.longitude}


# Mathilde Maersk​, IMO number ​9632179​.
# Australian Spirit​, IMO number ​9247455​.
# MSC Preziosa​, IMO number ​9595321​.


# def create_app():
#     app = Flask(__name__)
#     db.init_app(app)
#     return app

