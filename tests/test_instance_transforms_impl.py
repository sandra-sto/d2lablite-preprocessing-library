from unittest import TestCase

import numpy as np
import numpy.testing as npt
import pandas as pd

from preprocessing.transforms import instance_transforms_impl
from tests import instance_and_dataset_creator


class TestInstanceTransformsImpl(TestCase):

    def setUp(self):
        self.instance = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3)
        self.instance_with_index = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3, index = True)

    def test_boost(self):
        instance = instance_transforms_impl.boost_parameters(['param2'], 5, self.instance)
        values = np.array([[0, 5, 2]]*3)
        boosted_expected = pd.DataFrame(values, columns = instance.data.columns)
        pd.testing.assert_frame_equal(boosted_expected, instance.data)

    def test_remove_constant_parameters(self):
        instance = instance_transforms_impl.remove_constant_parameters(self.instance)

        npt.assert_array_equal(instance.columns, [])

    def test_filter_parameters(self):
        parameters = ['param1']
        instance = instance_transforms_impl.filter_parameters(parameters, self.instance)

        npt.assert_array_equal(instance.columns, ['param1'])

    def test_filter_parameters_except(self):
        parameters = ['param1']
        instance = instance_transforms_impl.filter_parameters_except(parameters, self.instance)

        npt.assert_array_equal(list(instance.columns), ['param2', 'param3'])

    def test_smooth_data(self):
        factor = 2
        method = 'mean'
        instance = instance_transforms_impl.smooth_data(factor, method, self.instance)
        self.assertIsNotNone(instance)

    def test_resample(self):
        instance = instance_transforms_impl.resample('2d', 'mean', self.instance_with_index)
        npt.assert_array_equal(list(instance.data.index), [pd.Timestamp('2018-11-11 00:00:00'), pd.Timestamp('2018-11-13 00:00:00')])

    def test_make_windows_months(self):
        instance = instance_transforms_impl.make_windows('M', self.instance_with_index)
        npt.assert_array_equal(list(instance.data.index), [pd.Period('2018-11'), pd.Period('2018-11'), pd.Period('2018-11')])

    def test_filter_instances_by_date(self):
        filtered = instance_transforms_impl.filter_instance_by_date('2018-11-12', '2018-11-13', self.instance_with_index)
        npt.assert_array_equal(list(filtered.data.index), [pd.Timestamp('2018-11-12 00:00:00'), pd.Timestamp('2018-11-13 00:00:00')])

    ############## test timedelta index
    def test_filter_instances_by_date_timedelta_index(self):
        instance = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3, index=True)
        instance.index_to_timedelta_ms()
        filtered = instance_transforms_impl.filter_instance_by_date('2018-11-11 00:00:00.0', '2018-11-12 00:00:00.0', instance)
        npt.assert_array_equal(list(filtered.data.index), [pd.Timedelta('0 days 00:00:00'), pd.Timedelta('1 days 00:00:00')])

    def test_resample_timedelta_index(self):
        instance = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3, index=True)
        instance.index_to_timedelta_ms()
        instance = instance_transforms_impl.resample('2d', 'mean', instance)
        npt.assert_array_equal(list(instance.data.index), [pd.Timedelta('0 days 00:00:00'), pd.Timedelta('2 days 00:00:00')])

    def test_make_windows_months_timedelta_index(self):
        instance = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3, index=True)

        instance = instance_transforms_impl.make_windows('M', instance)
        npt.assert_array_equal(list(instance.data.index), [pd.Period('2018-11'), pd.Period('2018-11'), pd.Period('2018-11')])

    ##############
    def test__eliminate_picks_using_quantiles(self):
        return



