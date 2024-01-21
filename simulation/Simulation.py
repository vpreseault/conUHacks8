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
                for k in range(self.ticks):
                    self.tick()
        print("done")

    def tick(self):
        num_players = utils.player_distribution[i][j]        
        players_per_tick = round(num_players / self.ticks)

        self.create_players(players_per_tick)
        self.matchmaking()

    def matchmaking(self):
        pass

    def create_players(self, amount):
        for l in range(amount):
            day = utils.days[i]
            hour = utils.hours[j]
            p = Player(day, hour)

            self.store[p.get_region()][p.get_platform()][p.get_skill()].append(p)
