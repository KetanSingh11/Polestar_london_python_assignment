from db.models import ShipData, db
from flask_restful import Resource
from utils.db_utils import delete_all_table_rows
from utils.logger import log


class ShipResource(Resource):
    __model__ = ShipData

    def get(self):
        ''' get all the ships in the db '''
        #todo: should return paginated responses
        try:
            # import pdb; pdb.set_trace()
            # shipdata = ShipData.query.all()
            result = db.session.query(ShipData).all()
            data = []
            for sd in result:
                data.append(sd.to_json())

            if len(data) == 0:
                return {'message': 'No data in shipdata table.'}, 200

            return {'shipsdata': data}, 200
        except Exception as e:
            log.exception(e)
            return {"message": str(e)}, 500

    def delete(self):
        try:
            res = delete_all_table_rows(ShipData.__tablename__)
            msg = "Deleted all rows of table '{}'".format(ShipData.__tablename__)
            log.warn(msg)

            return {'message': "Rows Deleted: {}".format(res)}, 200
        except Exception as e:
            log.exception(e)
            return {"message": str(e)}, 500