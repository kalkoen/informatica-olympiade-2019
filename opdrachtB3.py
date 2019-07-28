# Brute force
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

n_students = 8
n_customers = 12
n_fav_customers = n_students
student_choices = [[i for i in range(n_customers)] for j in range(n_students)]

for i in range(n_students):
    student_choices[i].sort(key=lambda c: customers[i][c])
    student_choices[i] = student_choices[i][:n_fav_customers]

# An n^n for. It's not completely clean, as in, it uses context to determine what to loop, but it works. I may challenge myself to create a 'true' n^n for in the future. I could bundle 8 for loops but what would be the fun in that?

# Taken or not
customer_status = [-1] * n_customers
student_indexes = [0] * n_students

lowest_total = 10000000

total = 0
solution = ()

i = 0

while student_indexes[0] < n_fav_customers:

    if student_indexes[i] > 0:
        c_num = student_choices[i][student_indexes[i] - 1]
        c = customers[i][c_num]
        if customer_status[c_num] == i:
            total -= c
            if i == 0 and total != 0:
                print("Rollback", i, "customer", c_num)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!", i, "so", total)
            customer_status[c_num] = -1

    if student_indexes[i] >= n_fav_customers:
        student_indexes[i] = 0
        i -= 1
        if i < 0:
            i = 0

        student_indexes[i] += 1
        continue

    c_num = student_choices[i][student_indexes[i]]
    c = customers[i][c_num]
    # for i in reversed(range(start_i)):
    if customer_status[c_num] == -1:
        total += c
        customer_status[c_num] = i
        i += 1

        if i == n_students:
            i = n_students - 1

            if total < lowest_total:
                lowest_total = total
                solution = student_indexes.copy()

            student_indexes[i] += 1
    else:
        # print(i, "cannot claim", c_num)
        student_indexes[i] += 1


print(lowest_total)

for i in range(len(solution)):
    print("Student", i, "got", solution[i], "choice... customer", student_choices[i][solution[i]], "costs", customers[i][student_choices[i][solution[i]]])
