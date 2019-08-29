from flask_restful import Resource, request, reqparse
from csv_ingester import csv_reader
from utils.db_utils import wipe_all_db_files, delete_all_table_rows
from utils.logger import log
from db.models import ShipData
from resources.imo import IMOResource

parser = reqparse.RequestParser()
parser.add_argument('action', type=str, required=True, help="This field is required! Possible values ['delete']")

class CSVResource(Resource):
    _default_csv_filename = "../positions.csv"

    def get(self):
        # load Shipdata table
        resp, status = csv_reader(self._default_csv_filename)
        # load imo table
        imo_resource = IMOResource()
        imo_resource.create_base_data()

        return {'message': resp}, status

    def post(self):
        try:
            data = parser.parse_args()
            action = data['action']

            if action.lower() == 'delete':
                wipe_all_db_files()
                return {"message":"Database DELETED"}, 200
            elif action.lower() == 'count':
                shipdata = ShipData.query.all()
                return {"row count": len(shipdata)}, 200
            else:
                msg = "Invalid value supplied. Valid values are ['delete']"
                log.error(msg)
                return {'error': msg}, 500
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