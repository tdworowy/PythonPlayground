from Decisions_Trees.CART.DecisionsTreesUtils2 import Utils
from Decisions_Trees.CART.tree import Cart


def test():
    cart_ = Cart()
    utils_ = Utils()
    filename = 'data.csv'
    data_set = utils_.load_csv(filename)

    for i in range(len(data_set[0])):
        utils_.str_column_to_float(data_set, i)

    n_folds = 10
    max_depth = 10
    min_size = 15
    scores = cart_.evaluate_algorithm(data_set,cart_.decision_tree , n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))


if __name__ == "__main__":
    test()