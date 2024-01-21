import utils
from Party import Party


class Simulation:
    def __init__(self):
        self.store = utils.dict_skeleton
        self.ticks = 3600

    def run(self):
        for i in range(7):
            for j in range(24):
                num_parties = utils.player_distribution[i][j]        
                parties_per_tick = round(num_parties / self.ticks) 
                for k in range(self.ticks):
                    for l in range(parties_per_tick):
                        day = utils.days[i]
                        hour = utils.hours[j]
                        p = Party(day, hour)

                        self.store[p.get_region()][p.get_platform()][p.get_skill()].append(p)
                    
                    self.matchmaking()
        print("done")

    def matchmaking(self):
        pass


