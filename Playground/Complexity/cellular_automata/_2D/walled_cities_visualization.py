from Playground.Complexity.cellular_automata._2D.general_2d_automata import walled_cities_rules
from Playground.Complexity.cellular_automata._2D.general_visualization import CellularAutomata2DVisualization

if __name__ == "__main__":
    CellularAutomata2DVisualization(walled_cities_rules, probability_of_one=0.2).main_loop()