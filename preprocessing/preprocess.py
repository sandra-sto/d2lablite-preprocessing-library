import logging
from os.path import dirname

from preprocessing.model.dataset import DataSet
from preprocessing.transforms import dataset_transforms, instance_transforms_impl
from preprocessing.util.transforms_mapping import DataType, TransformsMapping

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
DEFAULT_LOGGER_PATH = dirname(__file__) + '/preprocessing.log'

def define_logger(log_file):
    logger = logging.getLogger("Preprocessing")

    if log_file == '':
        log_file = DEFAULT_LOGGER_PATH
        logging.warning('No log file specified, default {}'.format(DEFAULT_LOGGER_PATH))

    f_handler = logging.FileHandler(log_file)
    f_format = logging.Formatter(FORMAT, datefmt='%d-%b-%y %H:%M:%S')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    return logger

class Preprocessor:

    def __init__(self, log_file = ''):
        self.transforms_mapping = TransformsMapping()
        logging.basicConfig(level=logging.INFO, filename=log_file)
        self.logger = define_logger(log_file)

    def preprocess(self, instance_transforms_passed : dict, dataset_transforms_passed: dict, dataset: DataSet, data_type: DataType, inplace= True, order = None):

        if order is None:
            for transform in instance_transforms_passed.keys():
                method = getattr(instance_transforms_impl, transform)

                if self.transforms_mapping.is_transform_applicable(data_type, method):
                    transform_parameters = instance_transforms_passed[transform]
                    self.logger.info('Transform started: {transform} with params: {params}'.format(transform = transform, params = transform_parameters))
                    dataset.perform_instance_transform(method, inplace, transform_parameters)


            for transform in dataset_transforms_passed.keys():
                method = getattr(dataset_transforms, transform)
                transform_parameters = dataset_transforms_passed[transform]

                dataset.perform_dataset_transform(method, transform_parameters)

        return dataset