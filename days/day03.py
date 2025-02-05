from .day import Day
import copy

class Position:
    x = 0
    y = 0

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return str(self.x) + ":" + str(self.y)

class Day03(Day):
    def get_positions(self, data):
        collection = set()
        cursor = Position()
        collection.add(copy.copy(cursor))
        for element in data:
            if element == ">":
                cursor.x = cursor.x + 1
            if element == "<":
                cursor.x = cursor.x - 1
            if element == "^":
                cursor.y = cursor.y + 1
            if element == "v":
                cursor.y = cursor.y - 1
            collection.add(copy.copy(cursor))
        return collection

    def part1(self, data):
        collection = self.get_positions(data)
        print(len(collection))

    def part2(self, data):
        santa_path = data[0::2]
        robo_path = data[1::2]
        santa_positions = self.get_positions(santa_path)
        robo_positions = self.get_positions(robo_path)
        total_positions = santa_positions.union(robo_positions)
        print(len(total_positions))