from unittest import TestCase

from mock import Mock

from preprocessing.preprocess import Preprocessor
from preprocessing.transforms import dataset_transforms, instance_transforms_impl
from preprocessing.util.transforms_mapping import DataType


class TestInstanceDfTransformsStrategy(TestCase):
    def setUp(self):
        self.dataset = Mock()
        self.preprocessor = Preprocessor()

    def test_preprocess(self):
        inplace=True
        instance_transforms_passed = {'filter_parameters':{'parameters_used':['param1']}}
        dataset_transforms_passed= {'pca':{'num_components':3}}
        type = DataType.timeseries

        self.preprocessor.preprocess(instance_transforms_passed, dataset_transforms_passed, self.dataset, type, inplace)

        self.dataset.perform_instance_transform.assert_called_with(instance_transforms_impl.filter_parameters, inplace, {'parameters_used':['param1']})
        self.dataset.perform_dataset_transform.assert_called_with(dataset_transforms.pca, {'num_components':3})





