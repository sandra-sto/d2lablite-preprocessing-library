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
        instance = instance_transforms_impl.boost_parameters(self.instance, ['param2'], 5, )
        values = np.array([[0, 5, 2]]*3)
        boosted_expected = pd.DataFrame(values, columns = instance.data.columns)
        pd.testing.assert_frame_equal(boosted_expected, instance.data)

    def test_remove_constant_parameters(self):
        instance = instance_transforms_impl.remove_constant_parameters(self.instance)

        npt.assert_array_equal(instance.columns, [])

    def test_filter_parameters(self):
        parameters = ['param1']
        instance = instance_transforms_impl.filter_parameters(self.instance, parameters)

        npt.assert_array_equal(instance.columns, ['param1'])

    def test_filter_parameters_except(self):
        parameters = ['param1']
        instance = instance_transforms_impl.filter_parameters_except(self.instance, parameters)


        npt.assert_array_equal(np.sort(list(instance.columns)), np.sort(['param2', 'param3']))

    def test_smooth_data(self):
        factor = 2
        method = 'mean'
        instance = instance_transforms_impl.smooth_data(self.instance, factor, method)
        self.assertIsNotNone(instance)

    def test_resample(self):
        instance = instance_transforms_impl.resample(self.instance_with_index, '2d', 'mean')
        npt.assert_array_equal(list(instance.data.index), [pd.Timestamp('2018-11-11 00:00:00'), pd.Timestamp('2018-11-13 00:00:00')])

    def test_make_windows_months(self):
        instance = instance_transforms_impl.make_windows(self.instance_with_index, 'M')
        npt.assert_array_equal(list(instance.data.index), [pd.Period('2018-11'), pd.Period('2018-11'), pd.Period('2018-11')])

    def test_filter_instances_by_date(self):
        filtered = instance_transforms_impl.filter_instance_by_date(self.instance_with_index, '2018-11-12', '2018-11-13')
        npt.assert_array_equal(list(filtered.data.index), [pd.Timestamp('2018-11-12 00:00:00'), pd.Timestamp('2018-11-13 00:00:00')])

    ############## test timedelta index
    def test_filter_instances_by_date_timedelta_index(self):
        instance = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3, index=True)
        instance.index_to_timedelta_ms()
        filtered = instance_transforms_impl.filter_instance_by_date(instance, '2018-11-11 00:00:00.0', '2018-11-12 00:00:00.0')
        npt.assert_array_equal(list(filtered.data.index), [pd.Timedelta('0 days 00:00:00'), pd.Timedelta('1 days 00:00:00')])

    def test_resample_timedelta_index(self):
        instance = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3, index=True)
        instance.index_to_timedelta_ms()
        instance = instance_transforms_impl.resample(instance, '2d', 'mean')
        npt.assert_array_equal(list(instance.data.index), [pd.Timedelta('0 days 00:00:00'), pd.Timedelta('2 days 00:00:00')])

    def test_make_windows_months_timedelta_index(self):
        instance = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3, index=True)

        instance = instance_transforms_impl.make_windows(instance, 'M')
        npt.assert_array_equal(list(instance.data.index), [pd.Period('2018-11'), pd.Period('2018-11'), pd.Period('2018-11')])


    ##############
    def test_standardize_instance(self):
        instance = instance_and_dataset_creator.create_instance(num_of_columns= 3, num_of_values = 3)
        means = pd.Series(np.array([0, 0.5, 1]), instance.columns)
        stdevs = pd.Series(np.array([0.1, 0.5, 0.2]), instance.columns)

        instance = instance_transforms_impl.standardize_instance(instance, means, stdevs)
        values = np.array([[0., 1., 5.]]*3)
        expected = pd.DataFrame(values, columns = instance.data.columns)
        pd.testing.assert_frame_equal(expected, instance.data)



