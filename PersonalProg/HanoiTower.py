class Hanoi:
    def __init__(self, size):
        self.size = size
        self.tower = [[], [], []]
        for i in range(size):
            self.tower[0].append(size - i)

    def move(self, source, destination):
        self.tower[destination].append(self.tower[source].pop())

    def hanoi(self, source: int, destination: int, n: int):
        if n == 1:
            self.move(source, destination)
            self.PrintMoves()
        else:
            self.hanoi(source, 3 - source - destination, n - 1)
            self.move(source, destination)
            self.PrintMoves()
            self.hanoi(3 - source - destination, destination, n - 1)

    def PrintMoves(self):
        print(self.tower)


if __name__ == "__main__":
    hanoi = Hanoi(5)
    hanoi.hanoi(0, 2, 5)
    hanoi.PrintMoves()
