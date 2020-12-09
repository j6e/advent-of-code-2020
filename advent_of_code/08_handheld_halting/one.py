from __future__ import annotations
import re
from pprint import pprint as print
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
    
    def find_infinite_loop(self) -> Tuple[int, int]:
        self.restart()

        i = 0
        visited = set()
        new_i = -1
        while len(visited) < len(self.instructions):
            visited.add(i)
            new_i = self.run_instruction(i)
            if new_i in visited:
                break
            i = new_i
        
        return self.accumulator, new_i

    def restart(self):
        self.accumulator = 0        


#p = Program('advent_of_code/08_handheld_halting/ex.txt')
p = Program.parse_program_from_file('advent_of_code/08_handheld_halting/input.txt')
print(p.instructions)
print(p.find_infinite_loop())