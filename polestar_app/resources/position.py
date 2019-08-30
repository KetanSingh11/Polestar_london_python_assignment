from db.models import ShipData, db
from flask_restful import Resource
from utils.logger import log

class PositionResource(Resource):
    def get(self, imo):
        """
        Queries ShipData table on given imo_id and returns
        list of all matching rows in desc order of datetime

        :param imo: Integer
        :return: list of dicts of {latitude, longitude} in DESC order
        """

        try:
            result = db.session.query(ShipData).filter(ShipData.imo_id==imo).order_by(ShipData.datetimestamp.desc())
            # log.info(result)
            data = []

            for row in result:
                data.append({'latitude': row.latitude,
                             'longitude': row.longitude})

            # return {'count': len(data), 'positions': data}, 200
            return data, 200
        except Exception as e:
            log.exception(e)
            return {"message": str(e)}, 500
