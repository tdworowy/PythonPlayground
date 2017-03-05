from Staff.DecisionsTrees.CART.DecisionsTreesUtils2 import utils
from Staff.DecisionsTrees.CART.tree import cart


def test():
    cart_ = cart()
    utils_ = utils()
    filename = 'data.csv'
    dataset = utils_.load_csv(filename)

    for i in range(len(dataset[0])):
        utils_.str_column_to_float(dataset, i)

    n_folds = 10
    max_depth = 10
    min_size = 15
    scores = cart_.evaluate_algorithm(dataset,cart_.decision_tree , n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))


if __name__ == "__main__":
    test()