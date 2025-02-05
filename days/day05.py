from .day import Day

class Day05(Day):

    def is_nice_part_one(self, string):
        length = len(string)
        vowels = "aeiou"
        vowels_count = 0
        contains_double = False
        for idx, x in enumerate(string):
            #check naughty substrings: ab, cd, pq, or xy
            if x == "a" and idx < (length-1):
                if string[idx+1] == "b":
                    return False
            if x == "p" and idx < (length-1):
                if string[idx+1] == "q":
                    return False
            if x == "c" and idx < (length-1):
                if string[idx+1] == "d":
                    return False
            if x == "x" and idx < (length-1):
                if string[idx+1] == "y":
                    return False
            #check vowels
            if vowels.find(x) != -1:
                vowels_count = vowels_count + 1
            #check double letters
            if idx > 0 and x == string[idx-1]:
                contains_double = contains_double or True
        return vowels_count >= 3 and contains_double

    def part1(self, data):
        result = 0
        substrings = data.split("\n")
        for substring in substrings:
            if self.is_nice_part_one(substring):
                result = result + 1
        print(result)

    def is_nice_part_two(self, string):
        length = len(string)
        contains_pair = False
        contains_letter_between = False
        for idx, x in enumerate(string):
            if contains_pair == False:
                if idx != length-1:
                    substr = x + string[idx+1]
                    if string.find(substr, idx+2) != -1:
                        contains_pair = True
            if contains_letter_between == False:
                if idx != length-1 and idx != 0:
                    if string[idx-1] == string[idx+1]:
                        contains_letter_between = True
            if contains_pair and contains_letter_between:
                return True
        return contains_pair and contains_letter_between
    
    def part2(self, data):
        result = 0
        substrings = data.split("\n")
        for substring in substrings:
            if self.is_nice_part_two(substring):
                result = result + 1
        print(result)