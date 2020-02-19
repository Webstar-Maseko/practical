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
        else:
            if(dt.hour == 6):
                self.state = Action.Breakfast
            if(dt.weekday() >= 0 and dt.weekday() <= 4):
                
                if(dt.weekday() == 0 or dt.weekday() == 2 or dt.weekday() == 4):
                    
                    if(dt.hour == 7):
                        self.state = Action.Gym
                    elif(dt.hour == 8):
                        self.state = Action.Class
                else:
                    if(dt.hour >= 7 and dt.hour < 13):
                        self.state = Action.Class
            if(dt.hour == 13):
                self.state = Action.Lunch
            else:
                self.state = Action.Class
            if(dt.hour == 17):
                self.state = Action.Television
            else:
                if(dt.hour == 9):
                    self.state = Action.Breakfast
                if(dt.weekday() == 6):
                    if(dt.hour >9 and dt.hour <=10):
                        self.state = Action.Church
                    elif(dt.hour >10 and dt.hour < 14):
                        self.state = Action.River
                    elif(dt.hour == 14):
                        self.state = Action.Lunch

                else:
                    if(dt.hour < 9):
                        self.state = Action.Sleep
                    if(dt.hour > 9 and dt.hour <14):
                        self.state = Action.River
                    if(dt.hour == 14):
                        self.state = Action.Lunch
                if(dt.hour >14):
                    self.state = Action.River

                

            if(dt.hour == 19):
                self.state = Action.Dinner
            if(dt.hour > 19 and dt.hour < 22):
                self.state = Action.Television
            elif(dt.hour > 22):
                self.state = Action.Sleep


        
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
       
        
        
