from preprocessing.model.dataset import DataSet
from pandas import Series
from sklearn.decomposition import PCA
import numpy as np
from sklearn.preprocessing import StandardScaler

class DataSetTransforms:

    def normalize(self, dataset: DataSet):
        return

    def pca_reduced_and_components(self, dataset: DataSet, **args) :

        num_components = args['num components']

        pca = PCA(n_components=num_components)
        reduced= pca.fit_transform(dataset.feature_vector)
        components = pca.components_

        return reduced, components


    def standardize_and_get_params(self, dataset: DataSet, **args)-> (DataSet, Series, Series):
        inplace = args['in_place']
        if inplace:
            ss = StandardScaler(copy = False)
            # array = np.array(dataset.instances)
            data_by_columns = np.array([instance.values for instance in dataset.instances]).reshape(dataset.num_of_columns, )


            ss.fit_transform(data_by_columns)


            return data_by_columns, Series(dataset.columns, ss.mean_), Series(dataset.columns, ss.scale_)

