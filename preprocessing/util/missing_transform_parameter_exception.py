from preprocessing.util.preprocessing_exception import PreprocessingException


class MissingTransformParameterException (PreprocessingException):
    def __init__(self, parameter, transform):
        super().__init__('Transform parameter {} for transformation {} is missing'.format(parameter, transform))