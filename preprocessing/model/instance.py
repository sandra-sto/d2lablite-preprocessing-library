

class Instance:

    def __init__(self, id, data, type, start_date, metadata):
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



