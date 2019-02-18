from typing import List
import numpy as np

from preprocessing.dataset_transforms.dataset_transforms import DataSetTransforms
from preprocessing.model.instance import Instance
from preprocessing.timeseries.instance_transforms import InstanceTransforms


class DataSet:
    def __init__(self, instance_transforms : InstanceTransforms, dataset_transforms: DataSetTransforms, instances : List[Instance]):

        self.instances = instances
        self.instance_transforms = instance_transforms
        self.dataset_transforms = dataset_transforms

    def perform_transform(self, transform, **args) :
        # parallel implementation

        transform_method = transform(args)

        transformed = [transform_method(instance) for instance in self.instances]
        return DataSet(self.instance_transforms, self.dataset_transforms, transformed)

    def perform_transforms(self, transforms):
        return

    def perform_dataset_transform(self, transform, **args):
        transform(self, args)

    @property
    def feature_vector(self):
        return np.array([df.values.T.flatten() for df in self.instances])

    @property
    def columns(self):
        return self.instances[0].columns

    @property
    def num_of_columns(self):
        return len(self.instances[0].columns)
