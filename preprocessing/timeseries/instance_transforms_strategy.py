from abc import ABC, abstractmethod


class InstanceTransformsStrategy (ABC):
    @abstractmethod
    def resample(self, resample_factor, resample_method, instance):
        pass

    @abstractmethod
    def remove_peaks(self, removing_peaks_method, instance):
        pass

    @abstractmethod
    def make_windows(self, window_size, instance):
        pass

    @abstractmethod
    def remove_constant_parameters(self, instance):
        pass

    @abstractmethod
    def filter_parameters(self, parameters, instance):
        pass

    @abstractmethod
    def filter_instances_by_date(self, start_date, end_date, instance):
        pass

    @abstractmethod
    def boost_parameters(self, parameters, factor, instance):
        pass

    @abstractmethod
    def wavelet(self, instance):
        pass

    @abstractmethod
    def smooth_data(self, factor, method, instance):
        pass

