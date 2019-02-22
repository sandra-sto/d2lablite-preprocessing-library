from unittest import TestCase

import numpy as np

from preprocessing.dataset_transforms import dataset_transforms
from tests import instance_and_dataset_creator


class TestDataSetTransforms(TestCase):
    def setUp(self):
        self.dataset = instance_and_dataset_creator.create_dataset()


    # @patch('sklearn.decomposition.PCA.fit_transform')
    # # @patch('sklearn.decomposition.PCA')
    # @unittest.skip()
    # def test_pca(self, mockpca1, mockpca2):
    #     mockpca2.return_value = []
    #     # mockpca2.return_value = 3
    #     mockpca1.components_=3
    #     num_components = 3
    #
    #     dataset, components = dataset_transforms.pca(self.dataset, num_components)
    #     self.assertIsInstance(dataset, DataSet)
    #     feature_vector = np.array([np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])]*3)
    #
    #     mockpca2.assert_called_with(feature_vector)


    def test_standardize_inplace(self):
        standardized_dataset, mean, stdev = dataset_transforms.standardize(self.dataset, True)

        standardized_array_first = np.array([[0,0,0], [0,0,0], [0,0,0]])
        np.testing.assert_array_almost_equal(standardized_dataset.instances[0], standardized_array_first)

    def test_standardize_copy(self):
        standardized_dataset, mean, stdev = dataset_transforms.standardize(self.dataset, False)
        standardized_array_first_instance = np.array([[0,0,0], [0,0,0], [0,0,0]])
        np.testing.assert_array_almost_equal(standardized_dataset.instances[0], standardized_array_first_instance)

        self.assertEqual(1, mean['param2'])





