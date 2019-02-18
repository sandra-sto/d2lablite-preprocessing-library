from typing import List, Callable

from pandas import DataFrame, DatetimeIndex, TimedeltaIndex, Series, Timestamp

from preprocessing.preprocessing_exception import PreprocessingException
from preprocessing.timeseries.instance_transforms_strategy import InstanceTransformsStrategy


class InstanceDfTransformsStrategy (InstanceTransformsStrategy):

    def resample(self, resample_factor: str, resample_method: Callable, instance: DataFrame):
        try:
            resampled = instance.resample(resample_factor).resampled_method()
            resampled_filled = resampled.fillna(method = 'ffill')
            # return resampled_filled
        except Exception as exc:
            raise PreprocessingException('Unappropriate argument for resampling', exc)
        else:
            return resampled_filled

    def remove_peaks(self, removing_peaks_method : str, instance: DataFrame):

        if removing_peaks_method == ' QUANTILES':
            self.eliminate_picks_using_quartiles(instance)
        else:
            raise PreprocessingException('Unappropriate argument for removing peaks')

    def make_windows(self, window_size: int, instance: DataFrame):
        return instance.to_period(window_size)


    def remove_constant_parameters(self, instance : DataFrame):
        return instance.loc[:, (instance != instance.iloc[0]).any()]


    def filter_parameters(self, parameters_used : List[str], instance: DataFrame):
        instance = instance[parameters_used]
        return instance

    def filter_parameters_except(self, parameters_excluded: List[str], all_parameters: List[str], instance: DataFrame):
        parameters_used = list(set(all_parameters) - set(parameters_excluded))
        return self.filter_parameters(parameters_used, instance)

    def boost_parameters(self, parameters: List[str], factor : int, instance):
        instance[parameters]*=factor
        return instance

    def filter_instances_by_date(self, start_date : Timestamp, end_date: Timestamp, instance: DataFrame):
        # offsets in df
        if isinstance(instance.index, DatetimeIndex):
            return instance.loc[start_date, end_date]
        elif isinstance(instance.index, TimedeltaIndex):
            diff = end_date - start_date
            # todo fill for timedelta index
            return instance.loc[start_date, end_date]
        else:
            raise PreprocessingException('Inappropriate DataFrame format')

    def eliminate_picks_using_quartiles(self, instance : DataFrame):
        low, high = 0.05, 0.95

        quantiles = instance.quantile([low, high])
        for name in instance.columns:
            instance = instance[(instance[name] >= quantiles.loc[low, name]) &
                    (instance[name] <= quantiles.loc[high, name])]
        instance.fillna(method='ffill', inplace=True)

        return instance

    def wavelet(self, instance: DataFrame):
        pass

    def smooth_data(self, factor, method: Callable, instance: DataFrame):
        smoothed = instance.rolling(window = factor).method()
        return smoothed