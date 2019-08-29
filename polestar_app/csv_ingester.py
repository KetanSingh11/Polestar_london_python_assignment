"""
Nuke the db
Reads a csv file and ingests the data into the Database
"""

import csv
import sys
import os
import logging
from datetime import datetime
from db.models import db, ShipData, IMO

logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO, format = '%(levelname)s : %(asctime)s: %(message)s')


CSV_HEADER = ['imo', 'datetimestamp', 'latitude', 'longitude']

def is_valid_file(csv_filename):
    if os.path.exists(csv_filename) and os.path.isfile(csv_filename):
        return True
    else:
        return False

def csv_reader(csv_filename):
    try:
        if is_valid_file(csv_filename):
            with open(csv_filename, 'r') as csv_file:
                reader = csv.reader(csv_file)
                logger.info("Inserting data from csv to db table...")
                row_count = 0

                for row in reader:
                    #todo: this way its not scalable
                    imo_id = int(row[0])
                    datetimestamp = convert_str_to_datetime(row[1])
                    latitude = float(row[2])
                    longitude = float(row[3])

                    data = ShipData(imo_id=imo_id, datetimestamp=datetimestamp, latitude=latitude, longitude=longitude)
                    db.session.add(data)
                    row_count += 1

                db.session.commit()

            return "{} rows inserted to Database".format(row_count), 200
        else:
            msg = "File '{}' not found! Please check if file path exists.".format(csv_filename)
            logger.error(msg)
            return msg, 404
    except Exception as e:
        logger.exception(e)
        return e, 500

def convert_str_to_datetime(datetimestr):
    # 2019-01-14 11:33:34+00
    if len(datetimestr) < 23:
        datetimestr = datetimestr + ":00"

    return datetime.strptime(datetimestr, "%Y-%m-%d %H:%M:%S%z")


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            csv_filename = sys.argv[1]
            file_ext = csv_filename.split(".")[-1]
            if file_ext.lower() != "csv":
                logger.error("Invalid CSV file specified: '{}'".format(csv_filename))
                sys.exit(1)

            csv_reader(csv_filename)
        elif len(sys.argv) < 2:
            logger.error("Missing argument: <filename>. Please specify a csv file path")
            sys.exit(1)
        else:
            logger.error("Too Many Parameters. ")
            logger.error("Use syntax: {} <csv filename>".format(sys.argv[0]))
    except Exception as e:
        logger.exception(e)
        sys.exit(1)
