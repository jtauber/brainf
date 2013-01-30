#!/usr/bin/env python
#
# brainf*** Interpreter in Python
# Copyright (c) 2002 & 2006 & 2012 & 2013, James Tauber
#
# see http://en.wikipedia.org/wiki/Brainfuck

import sys


class brainf:
    
    def __init__(self, program):
        self.mem = [0] * 65536
        self.p = 0
        self.pc = 0
        self.program = program
    
    def run(self, stop=None):
        if stop is None:
            stop = len(self.program)
        
        while self.pc < stop:
            c = self.program[self.pc]
            if c == ">":
                self.p += 1
            elif c == "<":
                self.p -= 1
            elif c == "+":
                self.mem[self.p] += 1
            elif c == "-":
                self.mem[self.p] -= 1
            elif c == ".":
                sys.stdout.write(chr(self.mem[self.p]))
            elif c == ",":
                self.mem[self.p] = ord(sys.stdin.read(1))
            elif c == "[":
                depth = 1
                start = end = self.pc
                while depth:
                    end += 1
                    if self.program[end] == "[":
                        depth += 1
                    if self.program[end] == "]":
                        depth -= 1
                while self.mem[self.p]:
                    self.pc = start + 1
                    self.run(end)
                self.pc = end
            elif c == "]":
                raise "unbalanced ]"
            else:
                pass
            self.pc += 1

# hello world sample

hello_world = """
>+++++++++[<++++++++>-]<.
>+++++++[<++++>-]<+.
+++++++.
.
+++.
[-]>++++++++[<++++>-]<.
>+++++++++++[<++++++++>-]<-.
--------.
+++.
------.
--------.
[-]>++++++++[<++++>-]<+.
[-]++++++++++.
"""

# add two one-digit numbers to make a third (if one-digit)

add = """
,>++++++[<-------->-],[<+>-],<.>.
"""

brainf(hello_world).run()
brainf(add).run()
