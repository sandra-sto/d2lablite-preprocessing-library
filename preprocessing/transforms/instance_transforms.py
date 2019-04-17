
# THIS CLOSURES ARE NOT USED

# instance based transforms

# better to have transforms isolated than in instance part
# since transforms will be sent through API and are easier to execute this way
from typing import Callable
from preprocessing.transforms import instance_transforms_impl

def resample(resample_factor, resample_method) -> Callable:

    def resample_with_factor(instance):
        result = instance_transforms_impl.resample(instance, resample_factor, resample_method)

        return result
    return resample_with_factor

def remove_peaks(removing_peaks_method) -> Callable:
    def remove_peaks(instance):
        result = instance_transforms_impl.remove_peaks(instance, removing_peaks_method)
        return result
    return remove_peaks

def make_windows(window_size) -> Callable:
    def make_windows(instance):
        result = instance_transforms_impl.remove_peaks(instance, window_size)
        return result
    return make_windows

def remove_constant_parameters() -> Callable:
    def remove_constant_transform(instance):
        result = instance_transforms_impl.remove_constant_parameters(instance)
        return result
    return remove_constant_transform

def boost_parameters(parameters, factor) -> Callable:
    def boost(instance):
        result = instance_transforms_impl.boost_parameters(instance, parameters, factor)
        return result

    return boost

def filter_parameters(parameters_used) -> Callable:
    def filter_parameters(instance):
        return instance_transforms_impl.filter_parameters(instance, parameters_used)
    return filter_parameters

def filter_parameters_except(parameters_used) -> Callable:
    def filter_parameters(instance):
        return instance_transforms_impl.filter_parameters(instance, parameters_used)
    return filter_parameters

def filter_instance_by_date(start_date, end_date) -> Callable:
    def filter_instance(instance):
        result = instance_transforms_impl.filter_instance_by_date(instance, start_date, end_date)
        return result
    return filter_instance

def wavelet(frequency_range) -> Callable:
    def wavelet_transform(instance):
        result = instance_transforms_impl.wavelet(instance, frequency_range)
        return result
    return wavelet_transform

def smooth_data(factor, smothing_method) -> Callable:
    def smooth(instance):
        result = instance_transforms_impl.smooth_data(instance, factor, smothing_method)
        return result
    return smooth
