class GridPlayer:

    def __init__(self):
        self.resourses_pos = []
        self.closest_resourse = ()

    def tick(self, game_map, your_units, enemy_units, resources, turns_left):
        ans = []
        get_closest_resopurse()
        for unit in your_units:
            if unit.type == "worker":
                if unit.can_mine(game_map):
                    ans.append(unit.mine())
                else:
                    ans.append( unit.move_towards(self.closest_resourse))
            else:
                ans.append(worrior_desisions(your_units, enemy_units, resources))
        return ans

    # def enemy_strats(self):
    #
    #
    def worrior_desisions(self, my_uns, enemy_uns, resours):
        """
        Returns desision based on enemy posision
        """
        general_dist = {}
        moves = []
        workers = my_uns.get_all_unit_of_type("worker")
        worker_pos = [x.posison() for x in workers]
        for i in my_uns:
            if i.type == "melee":
                general_dist[i] = i.nearby_enemies_by_distance(enemy_uns)

        for i in general_dist:
            if general_dist[i][1] >= 4  :
                if i.can_duplicate(resours):
                    moves.append(i.duplicate("UP"))
                else:
                    my_pos = i.position()
                    dst_to_work = [(x[0] - my_pos[0],x[1] - my_pos[1]) for x in worker_pos ]
                    move_to = worker_pos[ dst_to_work.index(min(dst_to_work))]
                    moves.append(i.move_towards(move_to))

            elif general_dist[i][1] == 1:
                continue
            elif general_dist[i][0] == 0:
                attacks =  i.can_attack(enemy_uns)
                if attacks == []:
                    continue
                else:
                    moves.append(i.attack(attacks[0]))

        return  moves





    def get_resourse_pos (self, game_map):
        self.resourses_pos = game_map.find_all_resources()

    def get_closest_resopurse (self, unit, game_map):
        self.closest_resourse = game_map.closest_resources(unit)
