"""day 5"""
#works_
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

def get_next(dest, map, dict_of_maps): #no change I think
    mapping = dict_of_maps[map]
    for s in mapping:
        b, a, span = s[0], s[1] , s[2]
        adjustment = abs(b-a) # need to find direction so will play with operator
        if b>a:
            adjustment *= -1
        #print(f"{dest} is between {b} and {b + span}?")       
        if b <= dest <= b + span -1:
            a = dest + adjustment
            #print(f"Yes - completed leg {map} {dest}->{a} -- adjustment {adjustment}")
            return a
        else:
            a = b + adjustment
    #print(f"No - completed leg of our journey using {map} {dest}->{dest}")  
    return dest #since if not found they are same


def de_overlap_tuples(t):
    sorted_tuples = sorted(t,key=lambda x: x[0]) #just to be safe
    res = [sorted_tuples[0]] #initialize 
    for t in sorted_tuples[1:]:
        last_t = res[-1]
        if t[0] > last_t[1]: #what we want
            res.append(t)
        else: #overlap
            res[-1] = (last_t[0],max(last_t[1]),t[1])
    return res
            
def input():
    with open('5/input.txt') as f:
        a = f.readlines()
        a = [i.strip() for i in a]
    return a

def main():
    """Trick is to start from the lowest location and find that seed. Then search if the seed is in there
    by going through each tuple and perform a z < winning seed < x +range

    o start from bottome of maps, find the destination that is the lowest and journey through that to the 
    winning seed. I think I will need to refactor some functions. Overlaps in seeds """

    a = input()
    dict_of_maps = gen_dicts(a)

    seeds_ = [int(x) for x in a[0].split(":")[1].split() if x.isdigit()]
    seed_tuples =  [(seeds_[i], seeds_[i + 1]) for i in range(0, len(seeds_), 2)]
    seed_tuples_bins = [(x,x+y-1) for x,y in seed_tuples]
    seed_tuples_bins = de_overlap_tuples(seed_tuples_bins)
    #order does not matter since the mapping journey is random  
    #print(f"These are the seeds that will be checked. Order does not matter since mapping journy is random: {seed_tuples_bins}")
    #locations to check:
    i = 0
    flip = True
    while flip:
        i += 1
        #print(f"{i} location checking journey~~~~~~~~~~~~~~~~~~~~~~~{i}")
        #if i == 36:
        #    break
        b = i
        for map in reverse_maps:
            b  = get_next(b, map, dict_of_maps)
        location_seed = b
        #print(f"{i} location results in seed {location_seed}")
        for t in seed_tuples_bins:
            #print(f"Testing loc: {i} which is seed: {location_seed} Is seed between {t[0]} and {t[1]}> ")
            if t[0] <= location_seed <= t[1]:
                print(f"YES SOLUTION FOUND after {i} cycles! It's {i}")
                flip = False
                return i

main()