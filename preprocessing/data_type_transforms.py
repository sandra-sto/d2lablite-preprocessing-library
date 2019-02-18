from collections import namedtuple

from preprocessing.preprocessing_exception import PreprocessingException
from enum import Enum

from preprocessing.timeseries.instance_transforms_strategy import InstanceTransformsStrategy


class DataType(Enum):
    timeseries = 0
    univariate = 1




class TransformsMapping:
    def __init__(self, transforms_strategy: InstanceTransformsStrategy):
        self.init_mapping_for_tranforms(transforms_strategy)


        self.mapping = {DataType.univariate: self.univariate_transforms, DataType.timeseries: self.timeseries_transforms}


    def init_mapping_for_tranforms(self, transforms_strategy):
        self.timeseries_transforms = {transforms_strategy.resample,
                                 transforms_strategy.remove_peaks,
                                 transforms_strategy.make_windows,
                                 transforms_strategy.remove_constant_parameters,
                                 transforms_strategy.filter_parameters,
                                 transforms_strategy.filter_instances_by_date,
                                 transforms_strategy.boost_parameters,
                                 transforms_strategy.wavelet,
                                 transforms_strategy.smooth_data}

        self.univariate_transforms = {transforms_strategy.remove_constant_parameters,
                                 transforms_strategy.filter_parameters,
                                 transforms_strategy.filter_instances_by_date,
                                 transforms_strategy.boost_parameters}


    def is_transform_applicable(self, data_type, transform):
        transform_types = self.mapping.keys()

        if data_type not in transform_types:
            raise PreprocessingException('Data type {} not found'.format(data_type))

        return transform in self.mapping[data_type]
