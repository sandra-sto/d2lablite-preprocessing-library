
# create decorators (closures)
# instance based transforms



# better to have transforms isolated than in instance part
# since transforms will be sent through API and are easier to execute this way
from typing import Callable

from preprocessing.timeseries.instance_df_transforms_strategy import InstanceDfTransformsStrategy
from preprocessing.timeseries.instance_transforms_strategy import InstanceTransformsStrategy



class InstanceTransforms:

    @staticmethod
    def get_instance(self, transforms_strategy : InstanceTransformsStrategy = None ):
        if not self.instance:
            self.instance = InstanceTransforms(transforms_strategy)
        return self.instance

    def __init__(self, transforms_strategy: InstanceTransformsStrategy):
        if not transforms_strategy:
            transforms_strategy = InstanceDfTransformsStrategy()
        self.transforms_strategy = transforms_strategy


    def resample(self, **kwargs) -> Callable:

        def resample_with_factor(instance):
            result = self.transforms_strategy.resample(kwargs['resample_factor'], kwargs['resample_method'], instance)
            return result
        return resample_with_factor

    def remove_peaks(self, **kwargs) -> Callable:
        def remove_peaks(instance):
            result = self.transforms_strategy.remove_peaks(kwargs['removing_peaks_method'], instance)
            return result
        return remove_peaks

    def make_windows(self, **args) -> Callable:
        def make_windows(instance):
            result = self.transforms_strategy.remove_peaks(args['window_size'], instance)
            return result
        return make_windows

    def remove_constant_parameters(self, **kwargs) -> Callable:
        def remove_constant_transform(instance):
            result = self.transforms_strategy.remove_constant_parameters(instance)
            return result
        return remove_constant_transform

    def boost_parameters(self, **kwargs) -> Callable:
        def boost(instance):
            result = self.transforms_strategy.boost_parameters(kwargs['parameters'], kwargs['factor'], instance)
            return result

        return boost

    def filter_parameters(self, **kwargs) -> Callable:
        def filter_parameters(instance):
            return self.transforms_strategy.filter_parameters(kwargs['parameters_used'], instance)
        return filter_parameters

    # def filter_parameters(self, parameters_used):
    #     def filter_parameters(instance):
    #         return self.transforms_strategy.filter_parameters(parameters_used, instance)
    #     return filter_parameters

    def filter_parameters_except(self, **kwargs) -> Callable:
        def filter_parameters(instance):
            return self.transforms_strategy.filter_parameters(kwargs['parameters_used'], instance)
        return filter_parameters

    def filter_instances_by_date(self, **kwargs) -> Callable:
        def filter_instances(self, instance):
            result = self.transforms_strategy.filter_instance_by_date(kwargs['start_date'], kwargs['end_date'], instance)
            return result
        return filter_instances

    def wavelet(self, **kwargs) -> Callable:
        def wavelet_transform(instance):
            result = self.transforms_strategy.wavelet(instance)
            return result
        return wavelet_transform

    def smooth_data(self, **kwargs) -> Callable:
        def smooth(instance):
            result = self.transforms_strategy.smooth_data(kwargs['factor'], kwargs['smothing_method'], instance)
            return result
        return smooth
