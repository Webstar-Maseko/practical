from datetime import datetime
from enum import Enum, IntEnum

class Action(IntEnum):
    Breakfast = 1
    Lunch = 2
    Dinner = 3
    Sleep = 4
    Gym = 5
    Class = 6
    Church = 7
    Television = 8
    River = 9

class Agent:

    def __init__(self, initialstate):
        self.state = initialstate
        pass

    def sense_world(self, dt, sick):
        # first decide what state you should be in when the details of the environment are known, then set self.state to that
        if sick:
            self.state = Action.Sleep
        if dt.hour == 13:
            self.state = Action.Lunch
        return self.state

    def perform_action(self):
        
        if self.state == Action.Breakfast:
            return "I am eating breakfast"
        elif( self.state == Action.Lunch):
            return "I am eating lunch"
        elif(self.state == Action.Dinner):
            return "I am eating dinner"
        elif(self.state == Action.Sleep):
            return "I am sleeping"
        elif(self.state == Action.Class):
            return "I am in class"
        elif(self.state == Action.Gym):
            return "I am at the gym"
        elif(self.state == Action.Church):
            return "I am at church"
        elif(self.state == Action.Television):
            return "I am watching television"
        elif(self.state == Action.River):
            return "I am next to the river"
       
        
        
