
from Playground.Complexity.cellular_automata._2D.general_2d_automata import \
    game_of_live_rules
from Playground.Complexity.cellular_automata._2D.general_visualization import CellularAutomata2DVisualization

if __name__ == "__main__":
    visualization = CellularAutomata2DVisualization(game_of_live_rules)
    visualization.main_loop()