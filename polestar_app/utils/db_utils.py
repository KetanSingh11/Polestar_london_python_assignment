import os

from db.models import DATABASE, db
from utils.logger import log
import time


def wipe_and_init_db():
    pass

def wipe_all_db_files():
    db_path = os.path.join("db", DATABASE)
    if os.path.exists(db_path) and os.path.isfile(db_path):
        log.warn("Database '{}' exists. Will be cleaned up shortly".format(db_path))
        time.sleep(5)
        os.remove(db_path)
        log.info("Database '{}' REMOVED Successfully".format(db_path))
        time.sleep(3)
    else:
        log.info("Path '{}' not found. Current Directory: {}".format(db_path, os.getcwd()))


def delete_all_table_rows(tablename_str):
    query = "DELETE from {};".format(tablename_str)
    result = db.engine.execute(query)

    return result.rowcount