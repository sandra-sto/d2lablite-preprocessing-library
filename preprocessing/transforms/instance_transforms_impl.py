from typing import List

import numpy as np
from pandas import DatetimeIndex, TimedeltaIndex, Series

from preprocessing.model.instance import Instance
from preprocessing.util.preprocessing_exception import PreprocessingException

methods = {'MEDIAN': np.median, 'MEAN': np.mean}


# these methods always return new instance
def resample(instance: Instance, resample_factor: str, resample_method: str) -> Instance:
    try:
        resampled = instance.data.resample(resample_factor).apply(methods[resample_method.strip().upper()])
        resampled_filled = resampled.fillna(method = 'bfill')
    except Exception as exc:
        raise PreprocessingException('Unappropriate argument for resampling', exc)
    else:
        return instance.copy_with_different_data(resampled_filled)

def remove_peaks(instance: Instance, removing_peaks_method: str) -> Instance:

    if removing_peaks_method.strip().upper() == 'QUANTILES':
        return __eliminate_peaks_using_quantiles(instance)
    else:
        raise PreprocessingException('Unappropriate argument for removing peaks')

def make_windows(instance: Instance, period) -> Instance:
    if isinstance(instance.data.index, DatetimeIndex):
        period_index_data = instance.data.to_period(period)
        return instance.copy_with_different_data(period_index_data)
    else:
        raise PreprocessingException('Inappropriate DataFrame format')

def remove_constant_parameters(instance : Instance) -> Instance:
    data = instance.data
    data_without_constants = data.loc[:, (data != data.iloc[0]).any()]

    return instance.copy_with_different_data(data_without_constants)

def filter_parameters(instance: Instance, parameters_used : List[str]) -> Instance:
    # if
    filtered_data = instance.data[parameters_used]
    return instance.copy_with_different_data(filtered_data)

def filter_parameters_except(instance: Instance, parameters_excluded: List[str]) -> Instance:
    parameters_used = list(set(instance.columns) - set(parameters_excluded))
    return filter_parameters(instance, parameters_used)

def wavelet(instance: Instance, frequency_range) -> Instance:
    pass

def smooth_data(instance: Instance, factor, method_name: str) -> Instance:
    windowed = instance.data.rolling(window = factor)
    smoothed = windowed.apply(methods[method_name.strip().upper()])
    smoothed = smoothed.fillna(method='bfill')
    return smoothed

def boost_parameters(instance, parameters: List[str], factor: int):
    boosted = instance.copy()
    boosted.data[parameters]*=factor
    return boosted

def filter_instance_by_date(instance: Instance, start_date : str, end_date: str) -> Instance:

    filtered_instance = instance.copy()
    if isinstance(instance.data.index, DatetimeIndex):
        filtered_instance.data = filtered_instance.data.loc[start_date : end_date]

    elif isinstance(instance.data.index, TimedeltaIndex):
        # todo fill for timedelta index

        filtered_instance.data.index = np.datetime64(filtered_instance.start_date)+filtered_instance.data.index
        filtered_instance.data = filtered_instance.data.loc[start_date : end_date, ]
        filtered_instance.data.index = filtered_instance.data.index-filtered_instance.data.index[0]

    else:
        raise PreprocessingException('Inappropriate DataFrame format')

    # change start time if needed
    if filtered_instance.start_date != filtered_instance.get_instance_index(0):
        filtered_instance.start_date = filtered_instance.get_instance_index(0)

    return None if len(filtered_instance.data) == 0 else filtered_instance

def __eliminate_peaks_using_quantiles(instance : Instance) -> Instance:
    low, high = 0.05, 0.95

    quantiles = instance.data.quantile([low, high])

    instance_with_eliminated_peaks = instance.copy()

    for name in instance.columns:
        instance_with_eliminated_peaks = instance[(instance[name] >= quantiles.loc[low, name]) &
                            (instance[name] <= quantiles.loc[high, name])]

    instance_with_eliminated_peaks.fillna(method='ffill', inplace=True)
    return instance_with_eliminated_peaks

def standardize_instance(instance: Instance, means: Series, stdevs: Series):
    standardized = instance.copy()
    for param in means.index:
        standardized.data[param] = (instance.data[param]-means[param]) / stdevs[param]
    return standardized