
# create decorators (closures)
# instance based transforms



# better to have transforms isolated than in instance part
# since transforms will be sent through API and are easier to execute this way

from preprocessing.timeseries.instance_transforms_strategy import InstanceTransformsStrategy


class InstanceTransforms:
    def __init__(self, transforms_strategy: InstanceTransformsStrategy):
        self.transforms_strategy = transforms_strategy

    def resample(self, **args):

        def resample_with_factor(instance):
            result = self.transforms_strategy.resample(args['resample_factor'], args['resample_method'], instance)
            return result
        return resample_with_factor

    def remove_peaks(self, **args):
        def remove_peaks(instance):
            result = self.transforms_strategy.remove_peaks(args['removing_peaks_method'], instance)
            return result
        return remove_peaks

    def make_windows(self, **args):
        def make_windows(instance):
            result = self.transforms_strategy.remove_peaks(args['window_size'], instance)
            return result
        return make_windows

    def remove_constants(self, **args):
        def remove_constant_transform(instance):
            result = self.transforms_strategy.remove_constant_parameters(instance)
            return result
        return remove_constant_transform

    def boost_parameters(self, **args):
        def boost(instance):
            result = self.transforms_strategy.boost_parameters(args['parameters'], args['factor'], instance)
            return result

        return boost