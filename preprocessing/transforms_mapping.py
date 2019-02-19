from enum import Enum
from typing import Callable

from preprocessing.preprocessing_exception import PreprocessingException


class DataType(Enum):
    timeseries = 0
    univariate = 1




class TransformsMapping:
    def __init__(self, instance_transforms):
        self.init_mapping_for_tranforms(instance_transforms)


        self.mapping = {DataType.univariate: self.univariate_transforms, DataType.timeseries: self.timeseries_transforms}


    def init_mapping_for_tranforms(self, instance_transforms):
        self.timeseries_transforms = {instance_transforms.resample,
                                      instance_transforms.remove_peaks,
                                      instance_transforms.make_windows,
                                      instance_transforms.remove_constant_parameters,
                                      instance_transforms.filter_parameters,
                                      instance_transforms.filter_instances_by_date,
                                      instance_transforms.boost_parameters,
                                      instance_transforms.wavelet,
                                      instance_transforms.smooth_data}

        self.univariate_transforms = {instance_transforms.remove_constant_parameters,
                                      instance_transforms.filter_parameters,
                                      instance_transforms.filter_instances_by_date,
                                      instance_transforms.boost_parameters}


    def is_transform_applicable(self, data_type: DataType, transform: Callable):

        if not isinstance(data_type, DataType):
            raise PreprocessingException('Data type {} not found'.format(data_type))

        return transform in self.mapping[data_type]
