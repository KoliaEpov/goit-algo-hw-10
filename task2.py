import random
import scipy.integrate as spi


def f(x):
    return x**2


def is_inside(x, y):
    return y <= x**2


def main():
    a = 0  # Нижня межа
    b = 2  # Верхня межа
    y_max = f(b)

    points = [(random.uniform(a, b), random.uniform(0, y_max)) for _ in range(15000)]
    inside_points = [point for point in points if is_inside(point[0], point[1])]

    rect_area = (b - a) * y_max
    N = len(points)
    M = len(inside_points)

    # Теоретична площа трикутника
    result, error = spi.quad(f, a, b)
    # Площа за методом Монте-Карло
    Sm = (M / N) * rect_area

    result = spi.quad(f, a, b)

    print('Sm', Sm)
    print('result', result)


if __name__ == "__main__":
    main()
