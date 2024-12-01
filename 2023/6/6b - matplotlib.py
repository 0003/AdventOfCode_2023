'--- Day 6: Wait For It ---'
#_the_plot_breaks

from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

def race_d(c_t,t):
    #velo (d/t) = charge_time * time
    v = c_t
    d = np.int64(c_t) * np.int64(t - c_t)
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
    print(f'race_wins: {race_wins}' )

    # Plotting
    print("Plotting-----------------")
    plt.xlabel(r'$c_t$')
    plt.ylabel(r'$d$')
    plt.title('Race Distance Function and Distance Record')

    fraction = 0.001  # Adjust the fraction as needed (e.g., 0.01 for 1% of the values)
    c_t_values = np.arange(0, t, int(1/fraction))

    for c_t in c_t_values:
        trial_distance = race_d(c_t, t)
        plt.plot(c_t, trial_distance, 'bo')  # Plot each point individually
        plt.axhline(y=d_r, color='red', linestyle='--')

        race_wins += race_result(trial_distance, d_r)

    plt.show()

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



