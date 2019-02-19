from typing import List, Callable

import numpy as np

from preprocessing.model.instance import Instance
from preprocessing.timeseries.instance_df_transforms_strategy import InstanceDfTransformsStrategy
from preprocessing.timeseries.instance_transforms import InstanceTransforms


class DataSet:
    def __init__(self, instances : List[Instance]):
        self.instances = instances

    def perform_transform(self, transform: Callable, inplace: bool, arguments: dict) :
        # parallel implementation
        # change parameters
        # t = InstanceTransforms(InstanceDfTransformsStrategy()).filter_parameters(**kwargs)
        transform_method = transform(**arguments)

        transformed = [transform_method(instance) for instance in self.instances]

        if inplace:
            self.instances = transformed
            return None
        else:
            return DataSet(transformed)

    def perform_dataset_transform(self, transform: Callable, arguments: dict):
        return transform(self, **arguments)

    @property
    def feature_vector(self) -> np.array:
        return np.array([df.values.T.flatten() for df in self.instances])

    @property
    def columns(self) -> List[str]:
        return self.instances[0].columns

    @property
    def num_of_columns(self) -> int:
        return len(self.instances[0].columns)
