import numpy as np
from pandas import Series
from dask_ml.decomposition import PCA

from preprocessing.model.dataset import DataSet
from dask_ml.preprocessing import StandardScaler

def normalize(dataset: DataSet):
    return

def pca(dataset: DataSet, num_components: int) :
    pca = PCA(n_components=num_components)
    reduced= pca.fit_transform(dataset.feature_vector)
    components = pca.components_

    return DataSet(reduced), components

def standardize(dataset: DataSet, inplace: bool = False)-> (DataSet, Series, Series):
    scaler = StandardScaler(copy = not inplace)

    data_by_columns = np.array([instance.data.values.flatten() for instance in dataset.instances])
    data_by_columns = data_by_columns.reshape(-1, dataset.num_of_columns)

    data_by_columns =scaler.fit_transform(data_by_columns)

    data_by_instances = data_by_columns.reshape(dataset.num_of_instances, -1)
    standardized_array = np.array([instance.reshape(-1, dataset.num_of_columns) for instance in data_by_instances])

    return DataSet(standardized_array), Series(scaler.mean_, dataset.columns, ), Series(scaler.scale_, dataset.columns)


def robust_scale():
    raise NotImplementedError()