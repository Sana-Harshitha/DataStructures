class SelectionSorter:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

# Example usage
my_sorter = SelectionSorter([6, 2, 1, 0, 7])
my_sorter.sort()
print(my_sorter.data)
