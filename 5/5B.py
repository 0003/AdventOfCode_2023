"""day 5"""
#_doesnt work but has multiprocessing

import time
import concurrent.futures
import multiprocessing
import os

workers = multiprocessing.cpu_count() - 1

maps = ['seed-to-soil map:',
        'soil-to-fertilizer map:',
        'fertilizer-to-water map:',
        'water-to-light map:',
        'light-to-temperature map:',
        'temperature-to-humidity map:',
        'humidity-to-location map:']

#map  soil / destination <- seed / source span

def gen_dicts(a):
    dict_of_maps = {}
    for i, string in enumerate(a):
        if string in maps:
            dict_ix = i
            dict_map_name = string #might not do anything with this
            dict_of_maps[dict_map_name] = [] # inititalize the dict
        elif string not in maps and i != 0 and string != '':
            destination, source, span = (int(s) for s in string.split())
            dict_of_maps[dict_map_name].append((destination, source, span))
        elif i == 0 or string == '':
            pass
            #print(f"passing or seeds on blanks {i} {string}")
        else: raise Exception(f"{dict_map_name} {destination} {source} {span} | index: {i}")
    return dict_of_maps

def get_next(source, map, dict_of_maps):
    #print(f"source: {source} in map: {map}")
    mapping = dict_of_maps[map]
    #print(f'mapping: \n {mapping}')
    for i,s in enumerate(mapping):
        dest_beg, source_beg, span = s[0], s[1] , s[2]
        #lot_range = range(source_beg, source_beg + span) numbers wayy too big
        #print(f"Checking if {source} is in {source_beg} - {source_beg + span -1}")
        if source_beg <= source <= source_beg + span - 1:
            if dest_beg < source_beg:
                dif = source_beg - dest_beg
                destination =  source - dif
                #print (f"location found: {destination} in map: {map}")
                return destination
            elif dest_beg > source_beg:
                dif = dest_beg - source_beg
                destination = source + dif
                #print (f"location found: {destination} in map: {map}")
                return destination
            else: raise Exception(f"this string cause problems {s}")
        elif source_beg > source:
            pass
        elif source_beg <= source > source_beg + span - 1:
            pass 
        else:
            pass #not found
    #no mapping
    destination = source
    #print (f"location not found: {destination} equals source {source} in map: {map}")
    return destination

def input():
    with open('5/test.txt') as f:
        a = f.readlines()
        a = [i.strip() for i in a]
    return a

def process_seed(seed_beg, span, dict_of_maps):
    print(f"First Seed in worker: {seed_beg} covering {seed_beg + span -1}, span: {span}")
    min_location = 9999999
    seed = seed_beg #first seed
    for e in range(0,span+1,1):
        seed += e #first e should be zero
        print(f"Starting seed journey: {seed_beg} + {e} =  {seed} ----------{os.getpid()}--------------{seed}")
        source = seed
        for map in maps:
            old_source = source
            source = get_next(source, map, dict_of_maps)
            print(f"Seed {seed} journey: {old_source}->{source}")
        print(f"Ending seed {seed} journey: {source} -----------------------------")
        location = source
        min_location = min(location,min_location)
    
    return [min_location]

def main():
    start_time = time.time()
    a = input()
    #print(a[:])
    dict_of_maps = gen_dicts(a)
    seeds_ = [int(x) for x in a[0].split(":")[1].split() if x.isdigit()]
    seed_tuples =  [(seeds_[i], seeds_[i + 1]) for i in range(0, len(seeds_), 2)]
    print(f"seed tuples: {seed_tuples}")
    locations = []
    len_seeds = (len(seeds_) / 2) + sum([x[1] for x in seed_tuples])
    i = 0

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:  # Use ProcessPoolExecutor for parallel processing
        futures = []

        for seed_beg, span in seed_tuples:
            print( f"Processing seeds {seed_beg} - {seed_beg - 1 + span} ----- FUTURE")
            futures.append(executor.submit(process_seed, seed_beg, span, dict_of_maps))

        for future in concurrent.futures.as_completed(futures):
            locations.extend(future.result())
            i += len(future.result())
            elapsed = time.time() - start_time
            print(f"Time elapsed as of {i} seeds: {elapsed}, Percent done: {i / len_seeds} on {len_seeds} estimated time left: {i/elapsed} seconds")

        #map  soil / destination <- seed / source span

        
        print(f"locations: {locations}")
        print(f"min location: {min(locations)}")


if __name__ == "__main__":
    main()
    multiprocessing.freeze_support()

