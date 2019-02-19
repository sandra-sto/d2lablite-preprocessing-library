import logging

from preprocessing.data_type_transforms import TransformsMapping

from preprocessing.dataset_transforms.dataset_transforms import DataSetTransforms
from preprocessing.model.dataset import DataSet
from preprocessing.timeseries.instance_df_transforms_strategy import InstanceDfTransformsStrategy
from preprocessing.timeseries.instance_transforms import InstanceTransforms
from preprocessing.transforms_mapping import DataType

logger = logging.getLogger("Preprocessing")
logging.basicConfig(level=logging.INFO)

class Preprocessor:

    def __init__(self):
        transform_strategy = InstanceDfTransformsStrategy()
        self.instance_transformer = InstanceTransforms(transform_strategy)
        self.transforms_mapping = TransformsMapping(self.instance_transformer)
        self.dataset_transformer = DataSetTransforms()

    def preprocess(self, instance_transforms : dict, dataset_transforms: dict, dataset: DataSet, data_type: DataType):

        for transform in instance_transforms.keys():
            if self.transforms_mapping.is_transform_applicable(data_type, transform):
                method = getattr(self.instance_transformer, transform)
                transform_parameters = instance_transforms[transform]

                dataset.perform_transform(method, **transform_parameters)

        for transform in dataset_transforms.keys():
            method = getattr(self.dataset_transformer, transform)
            transform_parameters = dataset_transforms[transform]

            dataset.perform_dataset_transform(method, **transform_parameters)


    # if isinstance(instance.index, DatetimeIndex):


