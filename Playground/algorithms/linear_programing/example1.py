import pulp

if __name__ == "__main__":
    model = pulp.LpProblem("Profit_maximising_problem", pulp.LpMaximize)
    A = pulp.LpVariable("A", lowBound=0, cat="Integer")
    B = pulp.LpVariable("B", lowBound=0, cat="Integer")

    # Objective function
    model += 5000 * A + 2500 * B, "Profit"

    # Constraints
    model += 3 * A + 2 * B <= 20
    model += 4 * A + 3 * B <= 30
    model += 4 * A + 3 * B <= 44

    # Solve problem
    model.solve()
    status = pulp.LpStatus[model.status]

    print(status)
    print(A.varValue)
    print(B.varValue)
    objective_function_value = pulp.value(model.objective)
    print(objective_function_value)
