import logging


from preprocessing.data_type_transforms import TransformsMapping
from preprocessing.dataset_transforms.dataset_transforms import DataSetTransforms
from preprocessing.model.dataset import DataSet
from preprocessing.timeseries.instance_df_transforms_strategy import InstanceDfTransformsStrategy
from preprocessing.timeseries.instance_transforms import InstanceTransforms

logger = logging.getLogger("Preprocessing")
logging.basicConfig(level=logging.INFO)


transform_strategy = InstanceDfTransformsStrategy()
instance_transforms = InstanceTransforms(transform_strategy)
transforms_mapping = TransformsMapping(transform_strategy)
dataset_transformer = DataSetTransforms()

def preprocess(instance_transforms : dict, dataset_transforms: dict, dataset: DataSet, data_type: str):

    for transform in instance_transforms.keys():
        if transforms_mapping.is_transform_applicable(data_type, transform):
            method = getattr(instance_transforms, transform)
            parameters = instance_transforms[transform]

            dataset.perform_transform(method, **parameters)

    for transform in dataset_transforms.keys():
        method = getattr(dataset, transform)
        parameters = dataset_transforms[transform]


    # if isinstance(instance.index, DatetimeIndex):


