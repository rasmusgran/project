import matplotlib.pyplot as plt
plt.rcParams["font.family"] = 'Arial'


def read_col(fname, col, convert=int, sep=None):
    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

x1 = read_col("Data/1000/Osorterad_Quicksort.txt", col=0)
y1 = read_col("Data/1000/Osorterad_Quicksort.txt", col=1)

x2 = read_col("Data/1000/Osorterad_Mergesort.txt", col=0)
y2 = read_col("Data/1000/Osorterad_Mergesort.txt", col=1)

x3 = read_col("Data/1000/Osorterad_Timsort.txt", col=0)
y3 = read_col("Data/1000/Osorterad_Timsort.txt", col=1)

plt.plot(x1, y1, label = "Quicksort")
plt.plot(x2, y2, label = "Mergesort")
plt.plot(x3, y3, label = "Timsort")
plt.legend()
plt.xlabel('N')
plt.ylabel('Tid (nanosekunder)')
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('')
plt.show()
