from unittest import TestCase

from mock import MagicMock

from preprocessing.preprocessing_exception import PreprocessingException
from preprocessing.timeseries.instance_transforms import InstanceTransforms
from preprocessing.transforms_mapping import TransformsMapping, DataType


class TestTransformsMapping(TestCase):
    def setUp(self):


        strategy = MagicMock()
        self.instance_transforms = InstanceTransforms.get_instance(strategy)
        self.mapping = TransformsMapping(self.instance_transforms)


    def test_is_transform_applicable_when_true(self):
          type = DataType.timeseries

          is_applicable = self.mapping.is_transform_applicable(type, self.instance_transforms.make_windows)
          self.assertEqual(is_applicable, True)

    def test_is_transform_applicable_when_false(self):
        type = DataType.univariate

        is_applicable = self.mapping.is_transform_applicable(type, self.instance_transforms.make_windows)
        self.assertEqual(is_applicable, False)

    def test_is_transform_applicable_for_unexisting_tranform(self):
        type = "univariate"

        self.assertRaises(PreprocessingException, self.mapping.is_transform_applicable, type, self.instance_transforms.make_windows)
