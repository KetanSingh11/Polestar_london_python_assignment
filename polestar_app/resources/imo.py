from db.models import IMO, db
from flask_restful import Resource
from utils.db_utils import delete_all_table_rows
from utils.logger import log


class IMOResource(Resource):
    __model__ = IMO

    def create_base_data(self):
        """
        Creates 3 rows on the fly and inserts into IMO table.
        Drops all rows before re-inserting.
        """
        try:
            log.info("Dropping all rows of 'imo' table first...")
            self.delete()

            a = IMO(id=9632179, name="Mathilde Maersk")
            b = IMO(id=9247455, name="Australian Spirit")
            c = IMO(id=9595321, name="MSC Preziosa")
            db.session.add(a)
            db.session.add(b)
            db.session.add(c)
            db.session.commit()
            log.info("Inserted 3 base IMOs into 'imo' table.")
            return "{} rows inserted to database table '{}'".format(3, self.__model__.__tablename__), 200
        except Exception as e:
            log.exception(e)
            return str(e), 500

    def get(self):
        """ get all the IMOs from the db """
        # todo: should return paginated responses

        try:
            self.create_base_data()

            imodata = IMO.query.all()
            data = []
            for imo in imodata:
                data.append(imo.to_json())

            return data, 200
        except Exception as e:
            log.exception(e)
            return {"message": str(e)}, 500

    def delete(self):
        """Empty IMO table (only) """
        try:
            res = delete_all_table_rows(IMO.__tablename__)
            msg = "Deleted all rows of table '{}': {} rows".format(IMO.__tablename__, res)
            log.warn(msg)

            return {'message': "Rows Deleted: {}".format(res)}, 200
        except Exception as e:
            log.exception(e)
            return {"message": str(e)}, 500