import utils
import random


class Player:
    def __init__(self, day, time):
        self.day = day
        self.time = time

        self.region = self.set_region()
        self.platform = self.set_platform()

        self.skill = self.set_skill()
        self.role = self.set_role()
        self.party = None
        self.id = None

    def get_region(self):
        return self.region

    def set_region(self):
        return utils.regions[round(random.random() * len(utils.regions) - 1)]

    def get_skill(self):
        return self.skill

    def set_skill(self):
        return utils.skills[round(random.random() * len(utils.skills) - 1)]

    def get_role(self):
        return self.role

    def set_role(self):
        n = utils.random_number()
        if n <= 0.3:
            self.role = "killer"
        else:
            self.role = "survivor"

    def get_party(self):
        return self.party

    def set_party(self, party):
        self.party = party

    def get_platform(self):
        return self.platform

    def set_platform(self):
        return utils.platforms[round(random.random() * len(utils.platforms) - 1)]

    def get_id(self):
        return self.id
