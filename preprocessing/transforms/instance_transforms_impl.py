import logging
from typing import List

import datetime
import numpy as np
from pandas import DatetimeIndex, TimedeltaIndex
from unittest import skip
from preprocessing.model.instance import Instance
from preprocessing.util.preprocessing_exception import PreprocessingException

methods = {'MEDIAN': np.median, 'MEAN': np.mean}

def resample( resample_factor: str, resample_method: str, instance: Instance) -> Instance:
    try:
        resampled = instance.data.resample(resample_factor).apply(methods[resample_method.strip().upper()])
        resampled_filled = resampled.fillna(method = 'bfill')
        # return resampled_filled
    except Exception as exc:
        logging.exception('Error occured during resampling')
        raise PreprocessingException('Unappropriate argument for resampling', exc)
    else:
        return instance.copy_with_different_data(resampled_filled)

def remove_peaks(removing_peaks_method: str, instance: Instance) -> Instance:

    if removing_peaks_method.strip().upper() == 'QUANTILES':
        return __eliminate_picks_using_quantiles(instance)
    else:
        raise PreprocessingException('Unappropriate argument for removing peaks')

def make_windows(period, instance: Instance) -> Instance:
    if isinstance(instance.data.index, DatetimeIndex):
        period_index_data = instance.data.to_period(period)
        return instance.copy_with_different_data(period_index_data)
    else:
        raise PreprocessingException('Inappropriate DataFrame format')

def remove_constant_parameters(instance : Instance) -> Instance:
    data = instance.data
    return data.loc[:, (data != data.iloc[0]).any()]

def filter_parameters(parameters_used : List[str], instance: Instance) -> Instance:
    instance = instance.data[parameters_used]
    return instance

def filter_parameters_except(parameters_excluded: List[str], instance: Instance) -> Instance:
    parameters_used = list(set(instance.columns) - set(parameters_excluded))
    return filter_parameters(parameters_used, instance)

def boost_parameters(parameters: List[str], factor : int, instance):
    instance.data[parameters]*=factor
    return instance

def filter_instance_by_date(start_date : str, end_date: str, instance: Instance) -> Instance:

    if isinstance(instance.data.index, DatetimeIndex):
        instance.data = instance.data.loc[start_date : end_date]


    elif isinstance(instance.data.index, TimedeltaIndex):
        # todo fill for timedelta index
        # start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
        # end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S.%f')
        #
        # diff_start = np.timedelta64(start_date - instance.start_date)
        # diff_end = np.timedelta64(end_date- instance.start_date)
        #
        # instance.data = instance.data.loc[diff_start : diff_end]

        instance.data.index = np.datetime64(instance.start_date)+instance.data.index

        instance.data = instance.data.loc[start_date : end_date,]
        instance.data.index = instance.data.index-instance.data.index[0]

    else:
        raise PreprocessingException('Inappropriate DataFrame format')

    # change start time if needed
    if instance.start_date != instance.get_instance_index(0):
        instance.start_date = instance.get_instance_index(0)

    return None if len(instance.data) == 0 else instance

def __eliminate_picks_using_quantiles(instance : Instance) -> Instance:
    low, high = 0.05, 0.95

    quantiles = instance.data.quantile([low, high])

    for name in instance.columns:
        instance = instance[(instance[name] >= quantiles.loc[low, name]) &
                            (instance[name] <= quantiles.loc[high, name])]

    instance.fillna(method='ffill', inplace=True)
    return instance

def wavelet(frequency_range, instance: Instance) -> Instance:
    pass

def smooth_data(factor, method_name: str, instance: Instance) -> Instance:
    windowed = instance.data.rolling(window = factor)
    smoothed = windowed.apply(methods[method_name.strip().upper()])
    smoothed = smoothed.fillna(method='bfill')
    return smoothed