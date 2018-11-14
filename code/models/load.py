import os
import pandas as pd


class DataLoad(object):

    def __init__(self, db_conn):

        self.db_conn = db_conn
        self.file_path = None

    def execute(self):

        self.get_file_path()

        with open(self.file_path, 'r') as fh:
            self.db_conn.copy_from(
                fh=fh,
                table='users',
                sep=','
            )

        self.db_conn.commit()

        # @IURII - why does the code below fail? for some reason it can't find the file

        # query = """
        #     COPY users
        #     FROM '{}'
        #     DELIMITER ','
        #     CSV HEADER
        #     ;
        # """
        #
        # self.db_conn.execute(
        #     query.format(
        #         self.file_path
        #     )
        # )

    def get_file_path(self):

        file_name = 'MOCK_DATA2.csv'
        path = os.path.join(
            '/data',
            file_name)

        self.file_path = path
