"""day 5"""
##_works

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
            print(f"passing or seeds on blanks {i} {string}")
        else: raise Exception(f"{dict_map_name} {destination} {source} {span} | index: {i}")
    return dict_of_maps

def get_next(source, map, dict_of_maps):
    print(f"source: {source} in map: {map}")
    mapping = dict_of_maps[map]
    print(f'mapping: \n {mapping}')
    for i,s in enumerate(mapping):
        dest_beg, source_beg, span = s[0], s[1] , s[2]
        #lot_range = range(source_beg, source_beg + span) numbers wayy too big
        print(f"Checking if {source} is in {source_beg} - {source_beg + span -1}")
        if source_beg <= source <= source_beg + span - 1:
            if dest_beg < source_beg:
                dif = source_beg - dest_beg
                destination =  source - dif
                print (f"location found: {destination} in map: {map}")
                return destination
            elif dest_beg > source_beg:
                dif = dest_beg - source_beg
                destination = source + dif
                print (f"location found: {destination} in map: {map}")
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
    print (f"location not found: {destination} equals source {source} in map: {map}")
    return destination

def get_input():
    with open('5/input.txt') as f:
        a = f.readlines()
        a = [i.strip() for i in a]
    return a

def main():
    a = get_input()
    #print(a[:])
    dict_of_maps = gen_dicts(a)
    seeds = [int(x) for x in a[0].split(":")[1].split() if x.isdigit()]
    print(f"seeds: {seeds}")
    locations = []
    #map  soil / destination <- seed / source span
    for seed in seeds:
        source = seed #        
        for map in maps:
           source = get_next(source, map, dict_of_maps) #next source is prior desitation
        location = source
        locations.append(location)
    
    #do
    print(f"locations: {locations}")
    print(f"min location: {min(locations)}")


main()