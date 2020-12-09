from __future__ import annotations
import re
from pprint import pprint
from typing import Dict, List, Tuple
from copy import deepcopy

re_op = r"(nop|acc|jmp) (\+\d+|\-\d+)"

class Program:

    def __init__(self, instructions: Dict[int, Dict[str, int]]) -> None:
        self.instructions = instructions
        self.accumulator = 0
    
    @staticmethod
    def parse_program_from_file(fname: str) -> Program:
        with open(fname, 'r') as f:
            lines = f.readlines()

        program = {}
        for i, l in enumerate(lines):
            operation, value = re.findall(re_op, l)[0]
            program[i] = {'op': operation, 'val': int(value)}
        
        p = Program(instructions=program)
        return p

    def run_instruction(self, instruction_nmbr: int) -> int:
        op, val = self.instructions[instruction_nmbr]['op'], self.instructions[instruction_nmbr]['val']
        if op == 'nop':
            return instruction_nmbr + 1
        elif op == 'acc':
            self.accumulator += val
            return instruction_nmbr + 1
        elif op == 'jmp':
            return instruction_nmbr + val
        else:
            raise Exception(f'ERROR in instruction {instruction_nmbr} - op:{op} val:{val}')
    
    def find_infinite_loop(self) -> Tuple[bool, int, int]:
        self.restart()

        i = 0
        visited = set()
        program_ended = False
        new_i = -1
        while len(visited) < len(self.instructions):
            visited.add(i)
            new_i = self.run_instruction(i)
            if new_i in visited:
                break
            if new_i == len(self.instructions):
                program_ended = True
                break
            i = new_i
        return program_ended, self.accumulator, new_i

    def find_corrupted_instruction(self) -> Tuple[bool, int, int, int]:
        self.restart()
        for i in self.instructions.keys():
            op = self.instructions[i]['op']
            # print(f'{i}: {op}')
            if op in ['jmp', 'nop']:
                if op == 'jmp':
                    new_op = 'nop'
                else:
                    new_op = 'jmp'
                new_instructions = deepcopy(self.instructions)
                new_instructions[i]['op'] = new_op
                new_program = Program(new_instructions)
                completed, accu, i_loop = new_program.find_infinite_loop()
                if completed:
                    return completed, accu, i, i_loop
        
        return False, 0, 0, 0

    def restart(self):
        self.accumulator = 0        


#p = Program('advent_of_code/08_handheld_halting/ex.txt')
p = Program.parse_program_from_file('advent_of_code/08_handheld_halting/input.txt')
# pprint(p.instructions)
print(p.find_corrupted_instruction())
