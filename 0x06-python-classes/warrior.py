#!/usr/bin/python3
import random

class Warrior:
    def __init__ (self, name, health):
        self.name = name
        self.health = health
    
    def print_info(self):
        print("Name: {}\nHealth: {}".format(self.name, self.health))

w = Warrior("Maximus", 100)
w.print_info()