# -*- coding: utf-8 -*-

import os
from turing_machine import TuringMachine

initial_state = "init",
accepting_states = ["final"],
transition_function = {("init", "0"): ("init", "1", "R"),
                       ("init", "1"): ("init", "0", "R"),
                       ("init", " "): ("final", " ", "N"),
                       }
final_states = ["final"]

t = TuringMachine("010011 ",
                  initial_state="init",
                  final_states=final_states,
                  transition_function=transition_function)

print("Input on Tape:")
t.show_tape()

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")
t.show_tape()

os.system("pause")
