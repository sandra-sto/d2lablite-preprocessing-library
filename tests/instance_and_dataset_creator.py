import datetime
import pandas as pd

from preprocessing.model.dataset import DataSet
from preprocessing.model.instance import Instance


def create_dataset(num_of_columns = 3, num_of_values = 3, num_of_instances = 5):
    instances = [create_instance(num_of_columns, num_of_values) for _ in range (num_of_instances)]

    return DataSet(instances)

def create_instance(num_of_columns, num_of_values, columns_prefix ='param', index = False):
    columns = [columns_prefix + str(i) for i in range(1, num_of_columns + 1)]

    values = [range(0, num_of_values) for _ in range(len(columns))]


    instance = Instance('', pd.DataFrame(columns = columns, data = values), 'type', datetime.datetime.strptime('2018-11-11', '%Y-%d-%m'), {})
    if index:
        instance.data.index = ['2018-11-11', '2018-11-12', '2018-11-13']
        instance.data.index = pd.to_datetime(instance.data.index, format='%Y-%m-%d %H:%M:%S')

    return instance


