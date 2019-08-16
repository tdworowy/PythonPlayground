from  multipledispatch import dispatch

class Thing(object): pass
class Rock(Thing): pass
class Paper(Thing): pass
class Scissors(Thing): pass

class RPS:

    @dispatch(Rock, Rock)
    def beats(x, y): return None

    @dispatch(Rock, Paper)
    def beats(x, y): return y

    @dispatch(Rock, Scissors)
    def beats(x, y): return x

    @dispatch(Paper, Rock)
    def beats(x, y): return x

    @dispatch(Paper, Paper)
    def beats(x, y): return None

    @dispatch(Paper, Scissors)
    def beats(x, y): return x

    @dispatch(Scissors, Rock)
    def beats(x, y): return y

    @dispatch(Scissors, Paper)
    def beats(x, y): return x

    @dispatch(Scissors, Scissors)
    def beats(x, y): return None

    @dispatch(object, object)
    def beats(x, y):
        if not isinstance(x, (Rock, Paper, Scissors)):
            raise TypeError("Unknown first thing")
        else:
            raise TypeError("Unknown second thing")


if __name__ == '__main__':
    game = RPS()
    print(game.beats(Rock(),Paper()))
    print(game.beats(Rock(), Scissors()))
    print(game.beats(Scissors(), Paper()))
    print(game.beats(Scissors(), Scissors()))
