from .day import Day

class Day01(Day):
    def part1(self, data):
        result = 0
        for c in data:
            if c == "(":
                result = result + 1
            if c == ")":
                result = result - 1
        print(result)

    def part2(self, data):
        position = self.find_basement_position(data)
        print(position)

    def find_basement_position(self,data):
        position = 1
        result = 0
        for c in data:
            if c == "(":
                result = result + 1
            if c == ")":
                result = result - 1
            if result == -1:
                return position
            position = position + 1
        return position

