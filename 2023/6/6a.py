'--- Day 6: Wait For It ---'
#works

from functools import reduce

def race_d(c_t,t):
    #velo (d/t) = charge_time * time
    v = c_t
    d = c_t * (t-c_t)
    #d = -c_t**2 + c_t * t  
    return d

def race_result(d,d_r):
    #distance and distance_record
    if d > d_r:
        return 1
    else: 
        return 0

def part_a():
    t_rs, d_rs = get_input()
    race_wins = []
    for race_ix in range(len(t_rs)):
        race_ix_wins = 0
        for c_t in range(t_rs[race_ix]):
            d_r = d_rs[race_ix]
            t = t_rs[race_ix]
            trial_distance = race_d(c_t,t)
            race_ix_wins += race_result(trial_distance,d_r)
        race_wins.append(race_ix_wins)
    print(f'race_wins: {race_wins}\n product of wins: {reduce(lambda x,y: x*y,race_wins )}' )
    return reduce(lambda x,y: x*y,race_wins )

def get_input():
    with open('6/input.txt') as f:
        in_ = f.readlines()
        print(in_)
        t_rs =[int(n) for n in in_[0].split(':')[1].strip().split()]
        print(f'time_record: {t_rs}')
        d_rs = [int(n) for n in in_[1].split(':')[1].strip().split()]
        print(f'distance_record: {d_rs}')
        return (t_rs, d_rs)

print(part_a())



