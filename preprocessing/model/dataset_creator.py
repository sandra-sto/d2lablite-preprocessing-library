import numpy as np
import pandas as pd

from preprocessing.model.dataset import DataSet
from preprocessing.model.instance import Instance


class InstanceCreator:
    def create_dataset(self, rows) -> DataSet:
        instances = [self.create_instance(row) for row in rows]

        return DataSet(instances)

    def create_instance(self, instance_json: dict) -> Instance:
        # Todo: finish implementation, all instances need to have same number of parameters and values
        if instance_json['data_range'] == None or instance_json['data_range'].used_for_clustering:
            start = instance_json['data_range'].start if instance_json['data_range'] else None
            end = instance_json['data_range'].end if instance_json['data_range'] else None

            params = instance_json['params']
            params = pd.DataFrame(dtypes = [np.float32])
            instance = Instance(instance_json['uuid'], params, instance_json['type'], instance_json['date_added'], instance_json['metadata'])

        return instance