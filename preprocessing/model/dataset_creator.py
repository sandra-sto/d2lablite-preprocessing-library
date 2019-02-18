from collections import namedtuple
import pandas as pd

from preprocessing.model.dataset import DataSet
from preprocessing.model.instance import Instance


class InstanceCreator:
    def create_dataset(self, rows, instance_tranforms, dataset_transforms):
        instances = [self.create_instance(row) for row in rows]

        return DataSet(instance_tranforms, dataset_transforms, instances)

    def create_instance(self, instance_json) -> Instance:

        if instance_json['data_range'] == None or instance_json['data_range'].used_for_clustering:
            start = instance_json['data_range'].start if instance_json['data_range'] else None
            end = instance_json['data_range'].end if instance_json['data_range'] else None

            params = instance_json['params']
            params = pd.DataFrame()
            instance = Instance(instance_json['uuid'], params, instance_json['type'], instance_json['date_added'], instance_json['metadata'])

        return instance