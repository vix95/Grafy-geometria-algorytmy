from main import generate_random_points, for_benchmark


def test_option_1(benchmark):
    points = generate_random_points(4)
    benchmark(for_benchmark, points)


def test_option_2(benchmark):
    points = generate_random_points(20)
    benchmark(for_benchmark, points)


def test_option_3(benchmark):
    points = generate_random_points(100)
    benchmark(for_benchmark, points)


def test_option_4(benchmark):
    points = generate_random_points(10 ** 3)
    benchmark(for_benchmark, points)


def test_option_5(benchmark):
    points = generate_random_points(10 ** 5)
    benchmark(for_benchmark, points)


def test_option_6(benchmark):
    points = generate_random_points(10 ** 7)
    benchmark(for_benchmark, points)
