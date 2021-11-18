import numpy as np
import time
from datetime import datetime

class schedule:
    
    def __init__(self) -> None:
        self.schedule = np.zeros(7*96).reshape(7,96)

    def set_action(self,time,day,action):
        self.schedule[day][time]=action


    def __str__(self) -> str:
        print(self.schedule)

a = schedule()
print(a)