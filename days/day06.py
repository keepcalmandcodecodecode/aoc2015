from .day import Day

class Day06(Day):
    def part1(self, data):
        result = 0
        count = 1000
        matrix = [[0]*count for i in range(count)]

        commands = data.split("\n")
        for command in commands:
            if command.startswith("turn on"):
                parts = command.split(" ")

                from_part = parts[2].split(",")
                from_x = int(from_part[0])
                from_y = int(from_part[1])

                to_part = parts[4].split(",")
                to_x = int(to_part[0])
                to_y = int(to_part[1])
                for i in range(from_x, to_x+1):
                    for j in range(from_y, to_y+1):
                        matrix[i][j] = 1


            if command.startswith("toggle "):
                parts = command.split(" ")

                from_part = parts[1].split(",")
                from_x = int(from_part[0])
                from_y = int(from_part[1])

                to_part = parts[3].split(",")
                to_x = int(to_part[0])
                to_y = int(to_part[1])
                for i in range(from_x, to_x+1):
                    for j in range(from_y, to_y+1):
                        if matrix[i][j] == 0:
                            matrix[i][j] = 1
                        else:
                            matrix[i][j] = 0

            if command.startswith("turn off "):
                parts = command.split(" ")

                from_part = parts[2].split(",")
                from_x = int(from_part[0])
                from_y = int(from_part[1])

                to_part = parts[4].split(",")
                to_x = int(to_part[0])
                to_y = int(to_part[1])
                for i in range(from_x, to_x+1):
                    for j in range(from_y, to_y+1):
                        matrix[i][j] = 0

        for i in range(count):
            for j in range(count):
                if matrix[i][j] == 1:
                    result = result + 1
        
        print(result)

    def part2(self, data):
        result = 0
        count = 1000
        matrix = [[0]*count for i in range(count)]

        commands = data.split("\n")
        for command in commands:
            if command.startswith("turn on"):
                parts = command.split(" ")

                from_part = parts[2].split(",")
                from_x = int(from_part[0])
                from_y = int(from_part[1])

                to_part = parts[4].split(",")
                to_x = int(to_part[0])
                to_y = int(to_part[1])
                for i in range(from_x, to_x+1):
                    for j in range(from_y, to_y+1):
                        matrix[i][j] = matrix[i][j] + 1


            if command.startswith("toggle "):
                parts = command.split(" ")

                from_part = parts[1].split(",")
                from_x = int(from_part[0])
                from_y = int(from_part[1])

                to_part = parts[3].split(",")
                to_x = int(to_part[0])
                to_y = int(to_part[1])
                for i in range(from_x, to_x+1):
                    for j in range(from_y, to_y+1):
                        matrix[i][j] = matrix[i][j] + 2

            if command.startswith("turn off "):
                parts = command.split(" ")

                from_part = parts[2].split(",")
                from_x = int(from_part[0])
                from_y = int(from_part[1])

                to_part = parts[4].split(",")
                to_x = int(to_part[0])
                to_y = int(to_part[1])
                for i in range(from_x, to_x+1):
                    for j in range(from_y, to_y+1):
                        if matrix[i][j] > 0:
                            matrix[i][j] = matrix[i][j] - 1

        for i in range(count):
            for j in range(count):
                result = result + matrix[i][j]
        
        print(result)