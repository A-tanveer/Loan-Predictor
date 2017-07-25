import pandas as pd
import re


def _if_blank(string):
    if not string:
        return 0
    return string


def _keep_only_number(string):
    if not string:
        return 0
    elif string in ['n/a', 'NA', 'N/A']:
        return 0
    return re.sub("[^0-9.]", "", repr(string))

file = pd.read_csv('raw_data/loan.csv')
clean_file = open('cleaned data/clean_loan.csv', 'w')
test_file = open('test_data/test_loan.csv', 'w')

columns = ['Loan ID', 'Customer ID', 'Loan Status', 'Current Loan Amount', 'Term', 'Credit Score',
           'Years in current job', 'Home Ownership', 'Annual Income', 'Purpose', 'Monthly Debt',
           'Years of Credit History', 'Months since last delinquent', 'Number of Open Accounts',
           'Number of Credit Problems', 'Current Credit Balance', 'Maximum Open Credit', 'Bankruptcies', 'Tax Liens']

keep_columns = ['Current Loan Amount', 'Term', 'Credit Score', 'Years in current job', 'Home Ownership',
                'Annual Income', 'Purpose', 'Monthly Debt', 'Years of Credit History','Months since last delinquent',
                'Number of Open Accounts', 'Number of Credit Problems', 'Current Credit Balance', 'Maximum Open Credit', 'Loan Status']

new_file = file[keep_columns]

# listing items in columns
purpose_list = [0]
purpose_list.extend(list(set(new_file["Purpose"])))
home_ownership_list = [0]
home_ownership_list.extend(list(set(new_file["Home Ownership"])))
term_list = [0]
term_list.extend(list(set(new_file["Term"])))
loan_status = sorted(list(set(new_file['Loan Status'])))
res = ''
test_res = ''
counter = 0

for each_row in new_file.itertuples():
    temp = []
    blank_replace_list = [1, 3, 6, 10, 11, 12, 13, 14]
    # blank_replace_list = [1, 3, 6, 10, 11, 12, 13, 14, 15, 16]  # columns that contains blank cells. *starts from 1. 1 > Current Loan ....
    for i in blank_replace_list:
        # print(each_row[i])
        if each_row[i] is None:
            temp.append(0)
        else:
            temp.append(_if_blank(each_row[i]))

    only_numbers = [4, 8, 9]  # columns that contains only numbers but with giberish
    for i in only_numbers:
        temp.append(_keep_only_number(each_row[i]))

    temp.append(purpose_list.index(each_row[7]))
    temp.append(term_list.index(each_row[2]))
    temp.append(home_ownership_list.index(each_row[5]))

    for i, j in zip(temp, range(len(temp))):
        if counter % 100 == 0:
            # test_res += repr(loan_status.index(each_row[17]))
            if j + 1:
                test_file.write(repr(i))
                test_file.write(',')
            else:
                test_file.write(repr(i))
        else:
            # res += repr(loan_status.index(each_row[17]))
            if j + 1:
                clean_file.write(repr(i))
                clean_file.write(',')
            else:
                clean_file.write(repr(i))

    if counter % 100 == 0:
        test_res += repr(loan_status.index(each_row[15]))
        test_file.write('\n')
    else:
        res += repr(loan_status.index(each_row[15]))
        clean_file.write('\n')

    counter += 1

#

res_file = open('cleaned data/train.txt', 'w')
res_file.write(res)
res_file.close()
res_file = open('test_data/test_result.txt', 'w')
res_file.write(test_res)
res_file.close()

clean_file.close()
file = open('cleaned data/clean_loan.csv')
data = file.read().replace('nan', '0').replace('\'', '').replace('#VALUE!', '0')
file.close()
f = open('cleaned data/clean_loan.csv', 'w')
f.write(data)
f.close()

test_file.close()
file = open('test_data/test_loan.csv')
data = file.read().replace('nan', '0').replace('\'', '').replace('#VALUE!', '0')
file.close()
f = open('test_data/test_loan.csv', 'w')
f.write(data)
f.close()
