from typing import List, Callable

import numpy as np

from preprocessing.model.instance import Instance
from multiprocessing import Pool

class DataSet:
    def __init__(self, instances : List[Instance]):
        self.instances = instances

    def perform_instance_transform(self, transform: Callable, arguments: dict, inplace: bool = True) :
        transform_method = transform(**arguments)
        pool = Pool()
        # transformed = pool.map(transform_method, self.instances)

        transformed = [transform_method(instance) for instance in self.instances]
        transformed = list(filter(None.__ne__, transformed))
        if inplace:
            self.instances = transformed
            return self
        else:
            return DataSet(transformed)

    def perform_dataset_transform(self, transform: Callable, arguments: dict, inplace: bool = True):
        transformed_dataset = transform(self, **arguments)
        if inplace:
            self.instances = transformed_dataset.instances
        return transformed_dataset

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
