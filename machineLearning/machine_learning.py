import matplotlib.pyplot as plt
import pandas
from pandas.tools.plotting import scatter_matrix


class machineL:
    def __init__(self):
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
        self.dataset = pandas.read_csv(url, names=names)

    def printData(self):
        print("###"*20,"SHAPE","###"*20)
        print(self.dataset.shape)
        print("###"*20,"HEAD","###"*20)
        print(self.dataset.head(20))
        print("###"*20,"SUMMARY","###"*20)
        print(self. dataset.describe())

        print("###"*20,"class distribution","###"*20)
        print(self.dataset.groupby('class').size())

    def plot(self):
        self.dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.show()

    def historgram(self):
        self.dataset.hist()
        plt.show()

    def scatterPLot(self):
        scatter_matrix(self.dataset)
        plt.show()


    def splitDataSet(self):
        array = self.dataset.values
        X = array[:, 0:4]
        Y = array[:, 4]
        validation_size = 0.20
        seed = 7
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,##TODO scikit don't work
                                                                                        random_state=seed)


if __name__ == "__main__":
    ml = machineL()

