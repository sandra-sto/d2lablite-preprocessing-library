import datetime


class Instance:

    def __init__(self, id: str, data: object, type: str, start_date: datetime, metadata: dict):
        self._id = id
        self._data = data
        self._type = type
        self._start_date = start_date
        self._metadata = metadata

    @property
    def data(self):
        return self._data

    @property
    def meta_data(self):
        return self._metadata

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

    @property
    def start_date(self):
        return self._start_date

    @property
    def feature_vector(self):
        return self.data.values.T.flatten()

    @property
    def columns(self):
        return self.data.columns

    @property
    def num_of_columns(self):
        return len(self.columns)

    @property
    def num_of_values(self):
        return len(self.data)

    def copy_with_different_data(self, new_data):
        return Instance(self.id, new_data, self.type, self.start_date, self.meta_data)

    def copy(self):
        return Instance(self.id, self.data, self.type, self.start_date, self.meta_data)

    def index_to_timedelta_ms(self):
        self.data.index = self.data.index - self.data.index[0]

    @start_date.setter
    def start_date(self, date):
        self._start_date = date

    @data.setter
    def data(self, data):
        self._data = data

    def get_instance_index(self, num):
        return self.data.index[num]




