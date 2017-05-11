class utils:
      def __init__(self,):
          print("")



      def giniIndex(self,groups,class_values):
          gini = 0.0
          for class_value in class_values:
              for groupe in groups:
                  size = len(groupe)
                  if size ==0: continue
                  proportion = [row[-1] for row in groupe].count(class_value) / float(size)
                  gini +=(proportion * (1.0 - proportion))
          return gini


      def test_split(self,index,value,dataset):
          left,right,=list(),list()
          for row in dataset:
              if row[index] < value:
                  left.append(row)
              else:
                  right.append(row)
          return left,right

      def get_split(self,dataset):
          class_values = list(set(row[-1] for row in dataset))
          b_index , b_value , b_score, b_groups = 999,999,999, None
          for index in range(len(dataset[0])-1):
              for row in dataset:
                  groups =self.test_split(index,row[index],dataset)
                  gini = self.giniIndex(groups,class_values)
                  print('X%d < %.3f Gini=%.3f' % ((index + 1), row[index], gini))
                  if gini < b_score:
                      b_index,b_value,b_score,b_groups = index,row[index] ,gini , groups
          return {'index':b_index,'value':b_value,'groups':b_groups}

      # def convertValuesToDummies(self,data):
      #     s = map(pd.Series, data)
      #     return map(pd.get_dummies, s)
      #
      #
      # def prettyList(self, inputlist):
      #     for item in inputlist:
      #         print(item)
      #
      # def dumiesToFile(self,dumiesList):
      #     with open(getDataPath() + "\\temp.csv", 'w') as f:
      #         for item in dumiesList:
      #           f.write(str(item)+",")
      #           f.flush()



def test():
    utils_ = utils()
    giniIndex1 = utils_.giniIndex([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1])
    giniIndex2 = utils_.giniIndex([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1])
    print(giniIndex1)
    print(giniIndex2)

    dataset = [[2.771244718, 1.784783929, 0],
               [1.728571309, 1.169761413, 0],
               [3.678319846, 2.81281357, 0],
               [3.961043357, 2.61995032, 0],
               [2.999208922, 2.209014212, 0],
               [7.497545867, 3.162953546, 1],
               [9.00220326, 3.339047188, 1],
               [7.444542326, 0.476683375, 1],
               [10.12493903, 3.234550982, 1],
               [6.642287351, 3.319983761, 1]]
    split = utils_.get_split(dataset)
    print('Split: [X%d < %.3f]' % ((split['index'] + 1), split['value']))


if __name__ == "__main__":
    test()
