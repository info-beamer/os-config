import sys, json, re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key[1]) ] 
    return sorted(l, key = alphanum_key)

l = json.load(file(sys.argv[1]))
l = natural_sort(l)
print json.dumps(l)
