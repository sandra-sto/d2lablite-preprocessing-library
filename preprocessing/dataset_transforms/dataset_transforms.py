import numpy as np
from pandas import Series
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from preprocessing.model.dataset import DataSet


class DataSetTransforms:

    def normalize(self, dataset: DataSet):
        return

    def pca_reduced_and_components(self, dataset: DataSet, **kwargs) :

        num_components = kwargs['num components']

        pca = PCA(n_components=num_components)
        reduced= pca.fit_transform(dataset.feature_vector)
        components = pca.components_

        return DataSet(reduced), components


    def standardize_and_get_params(self, dataset: DataSet, **kwargs)-> (DataSet, Series, Series):
        inplace = kwargs['in_place']
        ss = StandardScaler(copy = not inplace)
        data_by_columns = np.array([instance.values for instance in dataset.instances]).reshape(dataset.num_of_columns)

        if inplace:

            # array = np.array(dataset.instances)
            ss.fit_transform(data_by_columns)

            return data_by_columns, Series(dataset.columns, ss.mean_), Series(dataset.columns, ss.scale_)

