from static import prepare_data, measure_accuracy, hamming_distance
from sklearn.naive_bayes import GaussianNB


if __name__ == '__main__':

    tr = open('cleaned data/train.txt').readline().strip()
    test = open('test_data/test_result.txt').readline().strip()

    print('Preparing data for training....')

    data_features, train_data = prepare_data(open('cleaned data/clean_loan.csv').readlines(), tr)

    # SVM
    classifier = GaussianNB()
    classifier.fit(data_features, train_data)
    # classifier.predict(test)

    # test_data = prepare_data(open('cleaned data/clean_loan.csv').readlines())
    print('Preparing data for test....')
    test_data = prepare_data(open('test_data/test_loan.csv').readlines())
    result = ''
    for data in test_data:
        result += repr(classifier.predict([data])[0])

    print('\n\n\n')
    print('Total number of training data: ', len(list(tr)))
    print('Total number of testing data: ', len(list(test)))
    print('Original  : ' ,test)
    print('Predicted : ',result)
    print('Accuracy  : ', measure_accuracy(test, result))