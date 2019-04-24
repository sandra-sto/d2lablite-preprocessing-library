from enum import Enum
from typing import Callable

from preprocessing.transforms import instance_transforms_impl
from preprocessing.util.preprocessing_exception import PreprocessingException


class DataType(Enum):
    timeseries = 0
    one_valued = 1


class TransformsMapping:
    def __init__(self):
        self.init_mapping_for_tranforms()
        self.mapping = {DataType.one_valued: self.one_valued_transforms, DataType.timeseries: self.timeseries_transforms}


    def init_mapping_for_tranforms(self):
        self.timeseries_transforms = {instance_transforms_impl.resample,
                                      instance_transforms_impl.remove_peaks,
                                      instance_transforms_impl.make_windows,
                                      instance_transforms_impl.remove_constant_parameters,
                                      instance_transforms_impl.filter_parameters,
                                      instance_transforms_impl.filter_instance_by_date,
                                      instance_transforms_impl.boost_parameters,
                                      instance_transforms_impl.wavelet,
                                      instance_transforms_impl.smooth_data}

        self.one_valued_transforms = {instance_transforms_impl.remove_constant_parameters,
                                      instance_transforms_impl.filter_parameters,
                                      instance_transforms_impl.filter_instance_by_date,
                                      instance_transforms_impl.boost_parameters}


    def is_transform_applicable(self, data_type: DataType, transform: Callable):

        if not isinstance(data_type, DataType):
            raise PreprocessingException('Data type {} not found'.format(data_type))

        return transform in self.mapping[data_type]
