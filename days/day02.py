from .day import Day

class Day02(Day):

    def part1(self, data):
        result = 0
        strings = data.split("\n")
        for string in strings:
            numberStrings = string.split("x")
            numbers = list(map(lambda n: int(n), numberStrings))
            lw = numbers[0]*numbers[1]
            wh = numbers[0]*numbers[2]
            hl = numbers[1]*numbers[2]
            sum = 2*(lw+wh+hl)
            minside = min(min(lw, wh), hl)
            sum = sum + minside
            result = result + sum
        print(result)

    def part2(self, data):
        result = 0
        strings = data.split("\n")
        for string in strings:
            numberStrings = string.split("x")
            numbers = list(map(lambda n: int(n), numberStrings))
            lw = numbers[0]+numbers[1]
            wh = numbers[0]+numbers[2]
            hl = numbers[1]+numbers[2]
            minside = min(min(lw, wh), hl)
            v = numbers[0]*numbers[1]*numbers[2]
            sum = v + minside*2
            result = result + sum
        print(result)
        