from unittest import TestCase

import pandas as pd
from mock import Mock, mock
from numpy.testing import assert_array_equal
from preprocessing.dataset_transforms.dataset_transforms import DataSetTransforms
from preprocessing.model.dataset import DataSet
from preprocessing.timeseries.instance_transforms import InstanceTransforms
from tests import instances_creator
import numpy as np

class TestDataset(TestCase):
    def setUp(self):
        self.num_of_instances = 5
        instances = instances_creator.create_instances(self.num_of_instances)
        self.dataset = DataSet(instances)


    def test_feature_vector(self):
        expected_result = np.array([[0, 0, 0, 1, 1, 1, 2, 2, 2]]*self.num_of_instances)
        assert_array_equal(expected_result, self.dataset.feature_vector)

    def test_perform_transform_inplace_false(self):
        mock = Mock(return_value = lambda x: x)
        dataset = self.dataset.perform_transform(mock, False, {'param' : 'value'})

        mock.assert_called_with(param = 'value')
        self.assertIsNotNone(dataset)

    def test_perform_transform_inplace_true(self):
        mock = Mock(return_value = lambda x: x)
        dataset = self.dataset.perform_transform(mock, True, {'param' : 'value'})

        mock.assert_called_with(param = 'value')
        self.assertIsNone(dataset)

    def test_perform_dataset_transform(self):
        mock = Mock(return_value = self.dataset)

        dataset= self.dataset.perform_dataset_transform(mock, {'param' : 'value'})

        mock.assert_called_with(self.dataset, param = 'value')
        self.assertIsNotNone(dataset)