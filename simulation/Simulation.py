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

                        self.store[p.get_region()][p.get_platform()][p.get_skill()][p.get_role()].append(p)
                    
                    self.matchmaking()
        print("done")

    def calculate_queue_time(self, player, day, hour, ticks):
        current_hour = int(hour[:2])

        if player.get_day() != day:
            current_hour += 24

        hour_diff = int(player.get_hour()[:2]) - current_hour

        return (hour_diff * 3600) + ticks

    def matchmaking(self):
        pass


