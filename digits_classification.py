import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
import numpy as np

def multi_class_classification():
    digits = datasets.load_digits()
    x = digits['data']
    y = digits['target']
    logistic_regression(x, y)

# 测试集，画图对预测值和实际值进行比较
def test_validate(x_test, y_test, y_predict, classifier):
    x = range(len(y_test))
    plt.plot(x, y_test, "ro", markersize=5, zorder=3, label=u"true_v")
    plt.plot(x, y_predict, "go", markersize=8, zorder=2, label=u"predict_v,$R^2$=%.3f" % classifier.score(x_test, y_test))
    plt.legend(loc="upper left")
    plt.xlabel("number")
    plt.ylabel("true?")
    plt.show()

def logistic_regression(x, y):

    # 对数据的训练集进行标准化
    ss = StandardScaler()
    x_regular = ss.fit_transform(x)
    # 划分训练集与测试集
    x_train, x_test, y_train, y_test = train_test_split(x_regular, y, test_size=0.1)

    lr = LogisticRegression()
    lr.fit(x_train, y_train)

    print("回归系数：",lr.coef_)
    print("截距：",lr.intercept_)

    # 模型效果获取
    r = lr.score(x_train, y_train)
    print("R值(准确率):", r)
    # 预测
    y_predict = lr.predict(x_test)  # 预测
    print(y_predict)
    print(y_test)

    # 绘制测试集结果验证
    test_validate(x_test=x_test, y_test=y_test, y_predict=y_predict, classifier=lr)

multi_class_classification()