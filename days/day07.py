from .day import Day

class Day07(Day):

    def normalize(self, op, wires):
        if op.isdigit():
            return int(op)
        if op in wires:
            return wires[op]
        return 0
    
    def isnormal(self, op, wires):
        if op.isdigit():
            return True
        if op in wires:
            return True
        return False

    def part1(self, data):
        wires = {}
        commands_list = data.split("\n")
        length = len(commands_list)
        while len(commands_list) > 0:
            commands = commands_list
            for command in commands:
                operands = command.split(" ")
                if "AND" in command:
                    if self.isnormal(operands[0], wires) and self.isnormal(operands[2], wires):
                        op1 = self.normalize(operands[0], wires)
                        op2 = self.normalize(operands[2], wires)
                        res = operands[4]
                        wires[res] = op1 & op2
                        commands_list.remove(command)
                elif "OR" in command:
                    if self.isnormal(operands[0], wires) and self.isnormal(operands[2], wires):
                        op1 = self.normalize(operands[0], wires)
                        op2 = self.normalize(operands[2], wires)
                        res = operands[4]
                        wires[res] = op1 | op2
                        commands_list.remove(command)
                elif "LSHIFT" in command:
                    if self.isnormal(operands[0], wires) and self.isnormal(operands[2], wires):
                        op1 = self.normalize(operands[0], wires)
                        op2 = self.normalize(operands[2], wires)
                        res = operands[4]
                        wires[res] = op1 << op2
                        commands_list.remove(command)
                elif "RSHIFT" in command:
                    if self.isnormal(operands[0], wires) and self.isnormal(operands[2], wires):
                        op1 = self.normalize(operands[0], wires)
                        op2 = self.normalize(operands[2], wires)
                        res = operands[4]
                        wires[res] = op1 >> op2
                        commands_list.remove(command)
                elif "NOT" in command:
                    if self.isnormal(operands[1], wires):
                        op1 = self.normalize(operands[1], wires)
                        res = operands[3]
                        wires[res] = ~ op1
                        commands_list.remove(command)
                elif self.isnormal(operands[0], wires):
                    wires[operands[2]] = self.normalize(operands[0], wires)
                    commands_list.remove(command)
   

        result = wires['a'] & 0xffff
        self.a = result
        print(result)

    def part2(self, data):
        wires = {}
        commands_list = data.split("\n")
        while len(commands_list) > 0:
            commands = commands_list
            for command in commands:
                operands = command.split(" ")
                if "AND" in command:
                    if self.isnormal(operands[0], wires) and self.isnormal(operands[2], wires):
                        op1 = self.normalize(operands[0], wires)
                        op2 = self.normalize(operands[2], wires)
                        res = operands[4]
                        wires[res] = op1 & op2
                        commands_list.remove(command)
                elif "OR" in command:
                    if self.isnormal(operands[0], wires) and self.isnormal(operands[2], wires):
                        op1 = self.normalize(operands[0], wires)
                        op2 = self.normalize(operands[2], wires)
                        res = operands[4]
                        wires[res] = op1 | op2
                        commands_list.remove(command)
                elif "LSHIFT" in command:
                    if self.isnormal(operands[0], wires) and self.isnormal(operands[2], wires):
                        op1 = self.normalize(operands[0], wires)
                        op2 = self.normalize(operands[2], wires)
                        res = operands[4]
                        wires[res] = op1 << op2
                        commands_list.remove(command)
                elif "RSHIFT" in command:
                    if self.isnormal(operands[0], wires) and self.isnormal(operands[2], wires):
                        op1 = self.normalize(operands[0], wires)
                        op2 = self.normalize(operands[2], wires)
                        res = operands[4]
                        wires[res] = op1 >> op2
                        commands_list.remove(command)
                elif "NOT" in command:
                    if self.isnormal(operands[1], wires):
                        op1 = self.normalize(operands[1], wires)
                        res = operands[3]
                        wires[res] = ~ op1
                        commands_list.remove(command)
                elif self.isnormal(operands[0], wires):
                    if operands[2] == 'b':
                        wires[operands[2]] = self.a
                    else:
                        wires[operands[2]] = self.normalize(operands[0], wires)
                    commands_list.remove(command)

        result = wires['a'] & 0xffff
        print(result)