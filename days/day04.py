from .day import Day
import hashlib

class Day04(Day):

    def compute(self, data, starts):
        result = None
        counter = 1
        initial_data = data
        while result == None:
            data = initial_data + str(counter)
            key = data.encode('utf-8')
            digest = hashlib.md5(key).hexdigest()
            if digest.startswith(starts):
                result = counter
            counter = counter + 1
        return result

    def part1(self, data):
        result = self.compute(data, "00000")
        print(result)
    
    def part2(self, data):
        result = self.compute(data, "000000")
        print(result)