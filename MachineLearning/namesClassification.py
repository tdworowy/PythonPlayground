import random

import nltk

from MachineLearning.dataUtils import get_list_percent_head, get_list_percent_tail


class NamesClassification:

    def get_data(self):
        nltk.download('names')
        male_names = nltk.corpus.names.words('male.txt')
        female_names = nltk.corpus.names.words('female.txt')
        labeled_names = [(name, 'male') for name in male_names]
        labeled_names += [(name, 'female') for name in female_names]
        random.shuffle(labeled_names)
        return labeled_names

    def __init__(self):
        self.labeled_names = self.get_data();

    def get_features(self, name):
        return {
            'first_letter': name[0],
            'last_but_one_letter': name[-2],
            'last_letter': name[-1],
            'lenght': len(name)
        }

    def get_feature_set(self):
        return [(self.get_features(name), gender) for (name, gender) in self.labeled_names]

    def set_Sets(self, train_percent, test_percent):
        featureSet = self.get_feature_set()
        self.train_set, self.test_Set = get_list_percent_head(featureSet, train_percent), get_list_percent_tail(
            featureSet, test_percent)

    def bays_clasyfication(self, namesList):
        self.bays_classifier = nltk.NaiveBayesClassifier.train(self.train_set)
        features = [self.get_features(name) for name in namesList]
        clasfified = self.bays_classifier.classify_many(features)
        return clasfified

    # TODO
    def Weka_clasyfication(self, namesList):
        features = [self.get_features(name) for name in namesList]
        self.Weka_classifier = nltk.WekaClassifier.train(self.train_set, features)

        clasfified = self.Weka_classifier.classify_many(features)
        return clasfified

    def print_classifier_data(self):
        print("Accuracy: ", nltk.classify.accuracy(self.bays_classifier, self.test_Set))
        print(self.bays_classifier.show_most_informative_features())

    def test_classify(self, classification, train, test):
        self.set_Sets(train, test)
        classified = classification(["Adam", "Anna", "Thomas", "Sigmund", "Kathrin", "Anthony"])
        result = ['male', 'female', 'male', 'male', 'female', 'male']
        if classified != result:
            print("INCORRECT CLASSIFICATION")
            print("WAS:", classified)
            print("SHOULD BY: ", result)

    def test_byts(self, train, test):
        self.test_classify(self.bays_clasyfication, train, test)

    def test_Weka(self, train, test):
        self.test_classify(self.Weka_clasyfication, train, test)


if __name__ == '__main__':
    x = NamesClassification()
    x.test_byts(90, 10)
    x.test_byts(10, 90)
    x.test_byts(1, 99)
    x.test_byts(99, 1)
