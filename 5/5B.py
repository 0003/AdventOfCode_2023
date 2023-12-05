"""day 5"""
import time

maps = ['seed-to-soil map:',
        'soil-to-fertilizer map:',
        'fertilizer-to-water map:',
        'water-to-light map:',
        'light-to-temperature map:',
        'temperature-to-humidity map:',
        'humidity-to-location map:']

#map  soil / destination <- seed / source span

def gen_dicts(a):
    list_of_indexes = []
    dict_of_maps = {}
    for i, string in enumerate(a):
        if string in maps:
            dict_ix = i
            dict_map_name = string #might not do anything with this
            #dict_map_name, dict_ix,
            list_of_indexes.append((dict_map_name,dict_ix))
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
    with open('5/input.txt') as f:
        a = f.readlines()
        a = [i.strip() for i in a]
    return a

def main():
    start_time = time.time()
    a = input()
    #print(a[:])
    dict_of_maps = gen_dicts(a)
    seeds_ = [int(x) for x in a[0].split(":")[1].split() if x.isdigit()]
    seed_tuples =  [(seeds_[i], seeds_[i + 1]) for i in range(0, len(seeds_), 2)]
    locations = []
    len_seeds = (len(seeds_) / 2) + sum([x[1] for x in seed_tuples])
    i = 0
    for seed_beg, span in seed_tuples:
        source = seed_beg
        decermenter = span
        while decermenter > 0:
            if i % 10e5 == 0:
                print(f"Time elapsed as of {i} seeds : {time.time() - start_time}, Percent done: {i/len_seeds} on {len_seeds}")        
            for map in maps:
                source = get_next(source, map, dict_of_maps) #next source is prior desitation
            location = source
            locations.append(location)
            decermenter -= 1
            source = seed_beg + 1
            i += 1
        #map  soil / destination <- seed / source span

        
        print(f"locations: {locations}")
        print(f"min location: {min(locations)}")


main()
