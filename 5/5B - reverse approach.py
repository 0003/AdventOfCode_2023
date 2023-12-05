"""day 5"""
maps = ['seed-to-soil map:',
        'soil-to-fertilizer map:',
        'fertilizer-to-water map:',
        'water-to-light map:',
        'light-to-temperature map:',
        'temperature-to-humidity map:',
        'humidity-to-location map:']

reverse_maps = maps[::-1]

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
           # print(f"passing or seeds on blanks {i} {string}")
        else: raise Exception(f"{dict_map_name} {destination} {source} {span} | index: {i}")
    return dict_of_maps

def get_next(source, map, dict_of_maps): #no change I think
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

def de_overlap_tuples(t):
    t = sorted(t,key=lambda x: x[0]) #just to be safe
    no_duplicate_location_tuples = []
    no_overlaps = True
    min_x, max_x = (0, 0)
    for t in t:
        min_y = t[0]
        max_y = t[0] + t[1] - 1
        if max_x >= min_y and max_y > max_x : # 
            """ ------
                    -------"""
            min_y_adjustment = max_x - min_y
            print(f"Overlap found: {max_x} - {min_y} overlaps by {min_y_adjustment}")
            max_y = max(max_x,max_y) #probably not needed
            no_duplicate_location_tuples.append((min_y,max_y))
            min_x, max_x = min_y, max_y

        elif max_y >= min_x and min_y < min_x:
            """      ------
                 -------"""
            max_y = min_x + 1
            min_x, max_x = min_y, max_y
            raise Exception ("This sould not have happened - ovrlap 2. This means something is wrong with sorting")
        
        elif max_y > max_x and min_y > max_x:
            print("The best case no overlap")
            """ -----
                       ------   """
            no_duplicate_location_tuples.append((min_y,max_y))
            min_x, max_x = min_y, max_y

        elif min_y >= min_y and max_y <= max_x:
            print(" total overlap. Do nothing")
            """ -----
                 --   """
            min_x, max_x = min_y, max_y
    print(f"Here is the list of no_duplicate_location_tuples {no_duplicate_location_tuples}")
    return no_duplicate_location_tuples

def input():
    with open('5/test.txt') as f:
        a = f.readlines()
        a = [i.strip() for i in a]
    return a

def main():
    """Trick is to start from the lowest location and find that seed. Then search if the seed is in there
    by going through each tuple and perform a z < winning seed < x +range

    o start from bottome of maps, find the destination that is the lowest and journey through that to the 
    winning seed. I think I will need to refactor some functions."""

    a = input()
    dict_of_maps = gen_dicts(a)

    seeds_ = [int(x) for x in a[0].split(":")[1].split() if x.isdigit()]
    seed_tuples =  [(seeds_[i], seeds_[i + 1]) for i in range(0, len(seeds_), 2)]
    #order does not matter since the mapping journey is random  
    print(f"These are the seeds that will be checked. Order does not matter since mapping journy is random: {seed_tuples}")

    #locations to check:
    location_name = reverse_maps[0]
    print(f"location name: {location_name}")
    location_tuples = dict_of_maps[location_name]
    print(f'location tupes presort: {location_tuples}')
    location_tuples = sorted(location_tuples,key=lambda x: x[0])
    print(f"These are the locations that will be checked. Here order matters: {location_tuples}")
    location_tuples = de_overlap_tuples(location_tuples)
    print(location_tuples)

    a_ = location_tuples
    b_ = de_overlap_tuples(a_)

    print("checking if it overlaps works")
    for x,y in zip(a_,b_):
        print(f"{x},{y} 0's {abs(x[0]) - abs(y[0])} 1's: {abs(x[0]) - abs(y[0])}")
        if abs(x[0]) - abs(y[0]) > 10:
            raise Exception("should not happen")
        if abs(x[1]) - abs(y[1]) > 10:
            raise Exception("should not happen")

    max_loc = 0

    for t in location_tuples:
        candidate_high = t[1]
        max_loc = max(max_loc,candidate_high)
    print(f"Checking {max_loc} locations....................................... {max_loc}")
    
    for t in range(1,max_loc+1):
        #each tuple is min and max
        cycles = 0
        i=t
        cycles += 1
        #i is a location
        print(f"{i} location checking journey~~~~~{i}")
        source = i
        for map in reverse_maps:
            seed = get_next(source, map, dict_of_maps)
            source = seed
        location_seed = seed
        for t in seed_tuples:
            if t[0] <= location_seed <= t[1]:
                print(f"SOLUTION FOUND after {cycles} cycles! It's {i}")
                return i

main()