from Playground.Complexity.cellular_automata._2D.general_2d_automata import amoeba_rules
from Playground.Complexity.cellular_automata._2D.general_visualization import CellularAutomata2DVisualization

if __name__ == "__main__":
    visualization = CellularAutomata2DVisualization(amoeba_rules, probability_of_one=0.3)
    visualization.main_loop()
