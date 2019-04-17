from unittest import TestCase

import numpy as np

from preprocessing.transforms import dataset_transforms
from tests import instance_and_dataset_creator


class TestDataSetTransforms(TestCase):
    def setUp(self):
        self.dataset = instance_and_dataset_creator.create_dataset()

    def test_standardize_inplace(self):
        standardized_dataset, mean, stdev = dataset_transforms.standardize(self.dataset, True)

        standardized_array_first = np.array([[0,0,0], [0,0,0], [0,0,0]])
        np.testing.assert_array_almost_equal(standardized_dataset.instances[0], standardized_array_first)

    def test_standardize_copy(self):
        standardized_dataset, mean, stdev = dataset_transforms.standardize(self.dataset, False)
        standardized_array_first_instance = np.array([[0,0,0], [0,0,0], [0,0,0]])
        np.testing.assert_array_almost_equal(standardized_dataset.instances[0], standardized_array_first_instance)

        self.assertEqual(1, mean['param2'])