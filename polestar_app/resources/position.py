from db.models import ShipData, db
from flask_restful import Resource


class PositionResource(Resource):
    def get(self, imo):
        result = db.session.query(ShipData).filter(ShipData.imo_id==imo)
        data = []
        for row in result:
            data.append({'latitude': row.latitude,
                         'longitude': row.longitude})

        # return {'count': len(data), 'positions': data}, 200
        return data, 200

