import pandas as pd


def create_instances(num_of_instances = 5):
    columns = ['param1', 'param2', 'param3']
    values = [range(0, 3) for i in range(len(columns))]

    dfs = [pd.DataFrame(columns = columns, data = values) for i in range (num_of_instances)]

    return dfs
