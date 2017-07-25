# Loan-Predictor

The dataset (as a csv) contains information about customers & loans. It contains 111k data points, 18 features and 1 response variable (loan
status). The goal is to predict the response variable.


    K       weight      p   Accuracy
___________________________________________
    14      uniform     2   80.1259
    10      u           2   79.4964
    5       u           2   78.9568
    14      distance    2   80.6655
    10      d           2   80.6655
    5       d           2   79.6762
    14      d           6   80.8453
________________________________________________
    10      d           16  81.2050     Best result
------------------------------------------------
    14      d           16  80.8453
    10      d           32  81.2050
    10      d           64  81.0251


changing algorithm (auto, ball_tree, kd_tree, brute) has no effect on accuracy
changing leaf size has no impact on accuracy.
