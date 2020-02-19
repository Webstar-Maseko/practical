from Agent import Action, Agent
from datetime import datetime
from enum import Enum, IntEnum

# create the test agent
testAgent = Agent(Action.Breakfast)

# send the agent the details of the environment
d1 = datetime(year = 2020, month = 2, day = 16, hour = 10, minute = 0, second = 0)
print(testAgent.sense_world(d1, False))

# agent outputs results based on the state it is in
print(testAgent.perform_action())