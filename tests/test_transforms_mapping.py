from unittest import TestCase

from preprocessing.transforms import instance_transforms, instance_transforms_impl
from preprocessing.util.preprocessing_exception import PreprocessingException
from preprocessing.util.transforms_mapping import TransformsMapping, DataType


class TestTransformsMapping(TestCase):
    def setUp(self):
        self.mapping = TransformsMapping()

    def test_is_transform_applicable_when_true(self):
          type = DataType.timeseries

          is_applicable = self.mapping.is_transform_applicable(type, instance_transforms_impl.make_windows)
          self.assertEqual(is_applicable, True)

    def test_is_transform_applicable_when_false(self):
        type = DataType.univariate

        is_applicable = self.mapping.is_transform_applicable(type, instance_transforms_impl.make_windows)
        self.assertEqual(is_applicable, False)

    def test_is_transform_applicable_for_unexisting_tranform(self):
        type = "univariate"

        self.assertRaises(PreprocessingException, self.mapping.is_transform_applicable, type, instance_transforms.make_windows)
