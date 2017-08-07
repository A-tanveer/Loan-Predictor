
def hamming_distance(a, b):
    """returns hamming distance between two strings."""
    if not len(a) == len(b):
        raise ValueError('Strings must be same in size to compute hamming distance')
    return sum(i != j for i, j in zip(a, b))


def measure_accuracy(res, test):
    """
    :returns accuray
    """
    return (len(list(test)) - hamming_distance(res, test)) / len(list(test)) * 100


def prepare_data(data, result=None):
    """
    prepares cleaned data for training
    :param data: data points with k features
    :param result: corresponding response variable for training the data model. default: None, will return test data or real data to predict
    :return: preapred data to train or predict.
    """
    data_points = []
    # print()
    # print(len(data[0].split(',')))
    # print(data[0])
    for i in data:
        x = i.strip()[:-1].split(',')
        # print(x)
        # print()
        for j in range(len(x)):
            try:
                x[j] = float(x[j])
            except ValueError:
                x[j] = 0
        data_points.append(x)
    if result is not None:
        result = [int(x) for x in result]
        return data_points, result
    return data_points

