import utils
from Player import Player


class Simulation:
    def __init__(self):
        self.players = []
        self.store = utils.dict_skeleton
        self.ticks = 3600

    def run(self):
        for i in range(7):
            for j in range(24):
                num_players = utils.player_distribution[i][j]        
                players_per_tick = round(num_players / self.ticks) 
                for k in range(self.ticks):
                    for l in range(players_per_tick):
                        day = utils.days[i]
                        hour = utils.hours[j]
                        p = Player(day, hour)

                        self.store[p.get_region()][p.get_platform()][p.get_skill()].append(p)
                    
                    self.matchmaking()
        print("done")

    def matchmaking(self):
        pass

