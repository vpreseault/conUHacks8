import utils
import random


class Party:
    def __init__(self, day, time, ticks):
        self.day = day
        self.time = time
        self.ticks = ticks

        self.region = self.set_region()
        self.platform = self.set_platform()

        self.skill = self.set_skill()
        self.role = self.set_role()
        self.size = self.set_size()
        self.id = None

    def set_region(self):
        return utils.regions[round(random.random() * len(utils.regions) - 1)]
 
    def set_skill(self):
        return utils.skills[round(random.random() * len(utils.skills) - 1)]
 
    def set_role(self):
        n = utils.random_number()
        
        if n <= 0.3:
            return "killer"
        else:
            return "survivor"
 
    def set_size(self):
        return random.choice(utils.size_probability)

    def set_platform(self):
        return utils.platforms[round(random.random() * len(utils.platforms) - 1)]

    def get_region(self):
        return self.region

    def get_skill(self):
        return self.skill

    def get_role(self):
        return self.role

    def get_size(self):
        return self.size

    def get_platform(self):
        return self.platform
    
    def get_day(self):
        return self.day
    
    def get_time(self):
        return self.time
    
    def get_ticks(self):
        return self.ticks

    def get_id(self):
        return self.id
