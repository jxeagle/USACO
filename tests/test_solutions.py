from solution import perimeter

def test_solution():
    # read the input.txt file
    with open('tests/input.txt', 'r') as f:
        # read the first line
        line = f.readline()
        # split the line into a list of integers
        cows_cnt, connectio_cnt = [int(x) for x in line.split()]

        print(cows_cnt, connectio_cnt)

        # read the next cows_cnt lines into an array
        cows = [[int(x) for x in f.readline().split()] for _ in range(cows_cnt)]
        print(cows)

        # read the next connectio_cnt lines into an array
        connections = [[int(x) for x in f.readline().split()] for _ in range(connectio_cnt)]
        print(connections)

        assert perimeter(cows, connections) == 10
