from typing import List, Callable

import numpy as np

from preprocessing.model.instance import Instance


class DataSet:
    def __init__(self, instances : List[Instance]):
        self.instances = instances

    def perform_instance_transform(self, transform: Callable, inplace: bool, arguments: dict) :
        transform_method = transform(**arguments)

        transformed = [transform_method(instance) for instance in self.instances]
        transformed = list(filter(None.__ne__, transformed))
        if inplace:
            self.instances = transformed
            return None
        else:
            return DataSet(transformed)

    def perform_dataset_transform(self, transform: Callable, arguments: dict):
        return transform(self, **arguments)

    @property
    def feature_vector(self) -> np.array:
        return np.array([instance.feature_vector for instance in self.instances])

    @property
    def columns(self) -> List[str]:
        return self.instances[0].columns

    @property
    def num_of_columns(self) -> int:
        return self.instances[0].num_of_columns

    @property
    def num_of_values(self) -> int:
        return self.instances[0].num_of_values

    @property
    def num_of_instances(self) -> int:
        return len(self.instances)
