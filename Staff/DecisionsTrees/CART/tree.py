from Staff.DecisionsTrees.CART.DecisionsTreesUtils2 import utils


class cart:

    def __init__(self):
        self.utils = utils()

    def to_terminal(self,group):
        outcomes=[row[-1] for row in group]
        return max(set(outcomes),key=outcomes.count)

    def split(self,node,max_depth,min_size,depth):
        left , right = node['groups']
        del(node['groups'])
        if not left or not right:
            node['left'] =node['right'] = self.to_terminal(left+right)
            return
        if depth >= max_depth:
            node['left'] , node['right'] = self.to_terminal(left) , self.to_terminal(right)
        if len(left)<=min_size:
            node['left'] = self.to_terminal(left)
        else:
            node['left']=  self.utils.get_split(left)
            self.split(node['left'],max_depth,min_size,depth+1)
        if len(right)<=min_size:
            node['right'] = self.to_terminal(right)
        else:
            node['right'] = self.utils.get_split(right)
            self.split(node['right'], max_depth, min_size, depth + 1)

    def build_tree(self,train,max_depth,min_size):
        root = self.utils.get_split(train)
        self.split(root,max_depth,min_size,1)
        return root

    def print_tree(self,node,depth=0):
        if isinstance(node,dict):
            print('%s[X%d < %.3f]' % ((depth * ' ', (node['index'] + 1), node['value'])))
            self.print_tree(node['left'], depth + 1)
            self.print_tree(node['right'], depth + 1)
        else:
            print('%s[%s]' % ((depth * ' ', node)))

    def predict(self,node,row):
        if row[node['index']] < node['value']:
            if isinstance(node['left'],dict):
                return self.predict(node['left'],row)
            else: return node['left']
        else:
            if isinstance(node['right'], dict):
                return self.predict(node['right'], row)
            else:
                return node['right']


def test():
    cart_ = cart()
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
    tree = cart_.build_tree(dataset, 1, 1)
    cart_.print_tree(tree)

    stump = {'index': 0, 'right': 1, 'value': 6.642287351, 'left': 0}
    for row in dataset:
        prediction = cart_.predict(stump, row)
        print('Expected=%d, Got=%d' % (row[-1], prediction))


if __name__ == "__main__":
    test()
