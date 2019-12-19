import numpy as np

data = np.loadtxt("matrix_gts.txt", dtype=int)

# Check degree
vertex = int(input("Enter a vertex to check the degree"))

def degree(vertex):
    count = 0
    for i in range(len(data)):
        if data[vertex][i] != 0:
            count = count + 1
    return count


print(degree(vertex))

# Check Euler circuit
flag = True
for i in range(len(data)):
    if degree(i) % 2 != 0:
        flag = False

if flag:
    print("Yes")
else:
    print("No")




