import random


# Function for calculating budget overruns
def budget_overrun(
    list_cost: float, overrun_factor: float, overrun_likelihood: float
) -> float:
    likelihood_draw = random.random()  # Draws a float between 0 and 1
    if overrun_likelihood >= likelihood_draw:  # Project has run over budget
        overrun_draw = 1 + random.uniform(0, overrun_factor)
        print(f">>overrun_draw: {overrun_draw}")
        actual_budget = round((list_cost * overrun_draw), 2)
        print(f">>actual: {actual_budget}")
    else:
        actual_budget = list_cost
    return actual_budget


a = budget_overrun(2, 0.8, 1)
print(f">>a: {a}")

b = budget_overrun(1, 1, 1)
print(f">>b: {b}")

c = budget_overrun(1, 3, 1)
print(f">>c: {c}")

d = budget_overrun(5, 10, 1)
print(f">>d: {d}")
