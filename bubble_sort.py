data = [5, 1, 4, 3, 2, 10, 8]

def bubble_sort(data):
    steps = 0
    swapped = True
    while swapped:
        steps+=1
        swapped = False
        for i in range(len(data)-1):
            steps+=1
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
    print(data)
    print(steps)

bubble_sort(data)

# Big(O) = n^2