# Hungarian method
# satisfaction: 4/10

customers = [
    [75, 61, 52, 66, 56, 70, 77, 42, 77, 41, 70, 40],
    [50, 42, 70, 56, 60, 50, 71, 56, 52, 52, 76, 65],
    [77, 40, 42, 61, 53, 58, 65, 40, 40, 52, 77, 68],
    [50, 45, 79, 51, 48, 56, 79, 65, 46, 68, 61, 75],
    [52, 43, 72, 56, 77, 41, 74, 57, 67, 43, 55, 79],
    [41, 61, 54, 67, 73, 75, 40, 72, 61, 48, 61, 40],
    [64, 71, 66, 45, 62, 73, 56, 60, 52, 49, 64, 72],
    [60, 48, 46, 59, 41, 55, 77, 50, 57, 41, 73, 43]]

def print_grid():
    print("\t", end="")
    for c in range(n_customers):
        print(c, end="\t")
    print()
    for s in range(n_students):
        print(s, end="\t")
        for c in range(n_customers):
            print(customers[s][c]["modified_value"], end="\t")
        print()

    print()
    print()



n_students = len(customers)
n_customers = 12

student_choices = [[i for i in range(n_customers)] for j in range(n_students)]

for i in range(n_students):
    for j in range(n_customers):
        customers[i][j] = {
            "original_value": customers[i][j],
            "modified_value": customers[i][j]
        }

print_grid()

# Columns
for c in range(n_customers):
    lowest = min([customers[s][c]["original_value"] for s in range(n_students)])

    for s in range(n_students):
        customers[s][c]["modified_value"] = max(0, customers[s][c]["modified_value"] - lowest)

print_grid()

# Rows
for s in range(n_students):
    lowest = min([customers[s][c]["modified_value"] for c in range(n_customers)])

    for c in range(n_customers):
        customers[s][c]["modified_value"] = max(0, customers[s][c]["modified_value"] - lowest)

print_grid()

n_assigned = 0
assignments = [-1] * n_students
customers_assigned = [0] * n_customers

n_newly_assigned = 0

while n_assigned < n_students:

    for s in range(n_students):
        if assignments[s] != -1:
            continue

        n_zero = 0
        c_best = -1
        for c in range(n_customers):
            if customers[s][c]["modified_value"] == 0 and not customers_assigned[c]:
                n_zero += 1
                c_best = c
        if n_zero != 0 and n_zero == 1:
                print("Assigning", s, "to customer", c_best)
                assignments[s] = c_best
                customers_assigned[c_best] = 1
                n_assigned += 1
                n_newly_assigned += 1

    if n_newly_assigned == 0:
        break

    n_newly_assigned = 0

#assignments[3] = 10

print(assignments)

sum = sum([customers[s][assignments[s]]["original_value"] for s in range(n_students)])

print(sum)

