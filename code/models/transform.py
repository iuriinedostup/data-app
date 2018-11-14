import StringIO
import time


class DataTransform(object):

    def __init__(self, db_conn):

        self.db_conn = db_conn
        self.input = None
        self.output = None

    def execute(self):
        print 'transform'
        return 0

        self.get_data()
        self.get_count_by_extension()
        self.write_output()

    def get_data(self):

        query = """
            SELECT id
                , name
                , email
                , inserted_at
                , updated_at
            FROM users
        """

        self.db_conn.execute(query)

        result_set = self.db_conn.cursor.fetchall()
        input_data = self.insert_result_into_df(result_set)
        self.input = input_data

    @staticmethod
    def insert_result_into_df(result):

        columns = ['id', 'name', 'email', 'inserted_at', 'updated_at']
        df = pd.DataFrame([x for x in result], columns=columns)
        return df

    def get_count_by_extension(self):

        with_email_split = self.split_email_into_parts(self.input)
        with_domain_split = self.split_domain_into_parts(with_email_split)
        count_per_extension = self.group_by_extension(with_domain_split)
        self.output = count_per_extension

    @staticmethod
    def split_email_into_parts(df):

        temp_df = df.copy()
        columns = ['local_part', 'domain']
        temp_df[columns] = temp_df['email'].str.split('@', expand=True)
        return temp_df

    @staticmethod
    def split_domain_into_parts(df):

        temp_df = df.copy()
        columns = ['domain', 'extension']
        temp_df[columns] = temp_df['domain'].str.split('.', 1, expand=True)
        return temp_df

    @staticmethod
    def group_by_extension(df):

        temp_df = df.copy()
        grouping_fields = ['extension']
        grouped = temp_df.groupby(
            grouping_fields
        ).id.count().reset_index
        return grouped

    def write_output(self):

        temp_df = self.output().copy()
        temp_df['inserted_at'] = int(time.time())

        string_buffer = StringIO.StringIO()
        temp_df.to_csv(
            string_buffer,
            sep='\t',
            index=False,
            header=False,
            encoding='utf-8')
        string_buffer.pos = 0

        self.db_conn.copy_from(
            fh=string_buffer,
            table='count',
            sep='\t'
        )
        self.db_conn.commit()
