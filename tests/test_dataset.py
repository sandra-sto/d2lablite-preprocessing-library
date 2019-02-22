from unittest import TestCase

import numpy as np
from mock import Mock
from numpy.testing import assert_array_equal

from tests import instance_and_dataset_creator


class TestDataset(TestCase):
    def setUp(self):
        self.num_of_instances = 5
        self.dataset = instance_and_dataset_creator.create_dataset(3, 3, self.num_of_instances)

    def test_feature_vector(self):
        expected_result = np.array([[0, 0, 0, 1, 1, 1, 2, 2, 2]]*self.num_of_instances)
        assert_array_equal(expected_result, self.dataset.feature_vector)

    def test_perform_transform_inplace_false(self):
        mock = Mock(return_value = lambda x: x)
        dataset = self.dataset.perform_instance_transform(mock, False, {'param' : 'value'})

        mock.assert_called_with(param = 'value')
        self.assertIsNotNone(dataset)

    def test_perform_transform_inplace_true(self):
        mock = Mock(return_value = lambda x: x)
        dataset = self.dataset.perform_instance_transform(mock, True, {'param' : 'value'})

        mock.assert_called_with(param = 'value')
        self.assertIsNone(dataset)

    def test_perform_dataset_transform(self):
        mock = Mock(return_value = self.dataset)

        dataset= self.dataset.perform_dataset_transform(mock, {'param' : 'value'})

        mock.assert_called_with(self.dataset, param = 'value')
        self.assertIsNotNone(dataset)