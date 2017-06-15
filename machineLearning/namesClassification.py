import random

import nltk

from machineLearning.dataUtils import getListPercent_head, getListPercent_tail


class NamesClassification:

    def getData(self):
        nltk.download('names')
        male_names = nltk.corpus.names.words('male.txt')
        female_names = nltk.corpus.names.words('female.txt')
        labeled_names = [(name,'male') for name in male_names]
        labeled_names += [(name,'female') for name in female_names]
        random.shuffle(labeled_names)
        return labeled_names

    def __init__(self):
         self.labeled_names = self.getData();


    def getFeatures(self,name):
        return {
            'first_letter': name[0],
            'last_but_one_letter': name[-2],
            'last_letter': name[-1],
            'lenght' : len(name)
        }
    def gerFeatureSet(self):
        featureSet = [(self.getFeatures(name),gender) for(name,gender) in self.labeled_names]
        return featureSet

    def set_Sets(self,trainPercent,testPercent):
        featureSet = self.gerFeatureSet()
        self.train_set , self.test_Set = getListPercent_head(featureSet,trainPercent) , getListPercent_tail(featureSet,testPercent)

    def bays_clasyfication(self,namesList):
        self.bays_classifier = nltk.NaiveBayesClassifier.train(self.train_set)
        features = [self.getFeatures(name) for name in namesList]
        clasfified = self.bays_classifier.classify_many(features)
        return clasfified
    # TODO
    def Weka_clasyfication(self, namesList):
        features = [self.getFeatures(name) for name in namesList]
        self.Weka_classifier = nltk.WekaClassifier.train(self.train_set,features)

        clasfified = self.Weka_classifier.classify_many(features)
        return clasfified

    def printClassufierData(self):
        print("Accuracy: ", nltk.classify.accuracy(self.bays_classifier,self.test_Set))
        print(self.bays_classifier.show_most_informative_features())

    def testClassify(self,classification,train,test):
        self.set_Sets(train,test)
        classified = classification(["Adam","Anna","Thomas","Sigmund","Kathrin","Anthony"])
        result = ['male','female','male','male','female','male']
        if  classified != result:
            print("INCORRECT CLASSIFICATION")
            print("WAS:", classified)
            print("SHOULD BY: ",result)


    def testBays(self,train,test):
        self.testClassify(self.bays_clasyfication,train,test)

    def testWeka(self, train, test):
        self.testClassify(self.Weka_clasyfication,train, test)



if __name__ == '__main__':
    x = NamesClassification()
    x.testBays(90,10)
    x.testBays(10,90)
    x.testBays(1, 99)
    x.testBays(99, 1)





