'--- Day 6: Wait For It ---'
#works

def race_d(c_t,t):
    #velo (d/t) = charge_time * time
    v = c_t
    d = c_t * (t - c_t)

    return d

def race_result(d,d_r):
    #distance and distance_record
    if d > d_r:
        return 1
    else: 
        return 0

def part_b():
    t, d_r = get_input()
    race_wins = 0
    for c_t in range(t):
        trial_distance = race_d(c_t,t)
        race_wins += race_result(trial_distance,d_r)
    print(f'race_wins: {race_wins}')

    return race_wins

def get_input():
    with open('6/input.txt') as f:
        in_ = f.readlines()
        print(in_)
        t_rs =int(''.join([n for n in in_[0].split(':')[1].strip().split()]))
        print(f'time_record: {t_rs}')
        d_rs = int(''.join([n for n in in_[1].split(':')[1].strip().split()]))
        print(f'distance_record: {d_rs}')

        return (t_rs, d_rs)

print(part_b())



