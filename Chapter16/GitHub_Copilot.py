import matplotlib.pyplot as plt

def draw_scatterplot(x, y):
    plt.scatter(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()



draw_scatterplot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
