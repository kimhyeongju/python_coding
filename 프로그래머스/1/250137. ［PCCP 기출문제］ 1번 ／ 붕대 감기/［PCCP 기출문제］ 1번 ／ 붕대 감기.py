def solution(bandage, health, attacks):
    bandage_time = bandage[0]
    bandage_heal = bandage[1]
    bandage_bonus = bandage[2]
    attack_time = [attacks[i][0] for i in range(len(attacks))]
    attack_damage = [attacks[i][1] for i in range(len(attacks))]
    last_attack_time = attacks[-1][0]
    max_health = health

    heal_time = 0
    for time in range(1, last_attack_time+1):
        # attack
        if time in attack_time:
            idx = attack_time.index(time)
            health -= attack_damage[idx]
            heal_time = 0

        # # no attack
        # else:
        #     heal_time += 1
        #     if health + bandage_heal < max_health and heal_time < bandage_time:
        #         health += bandage_heal
        #     elif health + bandage_heal + bandage_bonus <= max_health and heal_time == bandage_time:
        #         health += bandage_heal + bandage_bonus
        #         heal_time = 0

        else:
            heal_time += 1
            if heal_time < bandage_time:
                health += bandage_heal
            elif heal_time == bandage_time:
                health += bandage_heal + bandage_bonus
                heal_time = 0
            if health > max_health:
                health = max_health

        # dead
        if health <= 0:
            return -1


    return health