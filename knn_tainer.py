from sklearn.neighbors import KNeighborsClassifier


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


def train_knn(data, target):
    """
    create trainer
    :param data: ready to train data
    :param target: result for data
    :return:
    """
    print('Do you want to use custom classifier?  y/n: ')
    custom = input().strip()
    if custom.startswith('y') or custom.startswith('Y'):
        print('Number of neighbors: ')
        k = int(input().strip())
        print('weights (uniform or distance): ')
        w = input().strip()
        print('p : (default = 2): ')
        p = int(input().strip())
        knn = KNeighborsClassifier(n_neighbors=k, weights=w, p=p)
    else:
        print('Do you want to use custom k?  y/n: ')
        custom = input().strip()
        if custom.startswith('y') or custom.startswith('Y'):
            print('insert k: ')
            k = int(input().strip())
            knn = KNeighborsClassifier(n_neighbors=k)
        else:
            knn = KNeighborsClassifier()

    knn.fit(data, target)
    return knn


if __name__ == '__main__':

    tr = open('cleaned data/train.txt').readline().strip()
    test = open('test_data/test_result.txt').readline().strip()

    print('Preparing data for training....')

    data_features, train_data = prepare_data(open('cleaned data/clean_loan.csv').readlines(), tr)

    knn = train_knn(data_features, train_data)

    # test_data = prepare_data(open('cleaned data/clean_loan.csv').readlines())
    print('Preparing data for test....')
    test_data = prepare_data(open('test_data/test_loan.csv').readlines())
    result = ''
    for data in test_data:
        result += repr(knn.predict([data])[0])

    print('\n\n\n')
    print('Total number of trainning data: ', len(list(tr)))
    print('Total number of testing data: ', len(list(test)))
    print('Original  : ' ,test)
    print('Predicted : ',result)
    print('Accuracy  : ', measure_accuracy(test, result))