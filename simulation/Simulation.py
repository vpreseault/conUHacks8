import utils
from Party import Party
import csv


class Simulation:
    def __init__(self):
        self.store = utils.dict_skeleton
        self.ticks = 3600
        
        self.fieldnames = ["day", "time", "region", "platform", "skill", "role", "size", "id", "queue_time"]
        
        


    def run(self):
        with open("output.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
        
        for i in range(7):
            for j in range(24):
                print("day: " + str(i) + " hour: " + str(j))

                num_parties = utils.player_distribution[i][j]
                parties_per_tick = round(num_parties / self.ticks) 
                
                for k in range(self.ticks):
                    for l in range(parties_per_tick):
                        day = utils.days[i]
                        hour = utils.hours[j]
                        ticks = k

                        p = Party(day, hour, ticks)
                        self.store[p.get_region()][p.get_platform()][p.get_skill()][p.get_role()].append(p)

                    time = {"day": day, "time": hour, "ticks": ticks}

                    self.matchmaking(time)

        print("done")

    def calculate_queue_time(self, player, time):
        day = time['day']
        hour = time['time']
        ticks = time['ticks']

        current_hour = int(hour[:2])

        if player.get_day() != day:
            current_hour += 24

        hour_diff = current_hour - int(player.get_time()[:2])

        return (hour_diff * self.ticks) + (ticks - player.get_ticks())

    def matchmaking(self, time):
        for region in self.store:
            for platform in self.store[region]:
                for skill in self.store[region][platform]:
                    for role in self.store[region][platform][skill]:
                        for killer in self.store[region][platform][skill]["killer"]:
                            victims = []
                            total = 0
                            for survivor in self.store[region][platform][skill]["survivor"]:
                                if survivor.get_size() + total <= 4:
                                    victims.append(survivor)
                                    total+=survivor.get_size()
                                    if total == 4:
                                        self.write_to_csv(killer, victims, time)
                                        self.store[region][platform][skill]["killer"].remove(killer)
                                        for victim in victims:
                                            self.store[region][platform][skill]["survivor"].remove(victim)
                                        victims.clear()
    

    def write_to_csv(self, killer, victims, time):
        with open("output.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({"day": killer.get_day(), "time": killer.get_time(), "region": killer.get_region(), "platform": killer.get_platform(), "skill": killer.get_skill(), "role": killer.get_role(), "size": killer.get_size(), "id": killer.get_id(), "queue_time": self.calculate_queue_time(killer, time)})
            for victim in victims:
                writer.writerow({"day": victim.get_day(), "time": victim.get_time(), "region": victim.get_region(), "platform": victim.get_platform(), "skill": victim.get_skill(), "role": victim.get_role(), "size": victim.get_size(), "id": victim.get_id(), "queue_time": self.calculate_queue_time(victim, time)})
                
            csvfile.close()



