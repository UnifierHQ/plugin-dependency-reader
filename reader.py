import json
import sys

filepath = sys.argv[len(sys.argv)-1] # use last argument as file

if filepath == 'reader.py':
    # default to plugin.json if filepath was probably not provided
    filepath = 'plugin.json'

with open(filepath) as file:
    data = json.load(file)

file = open('requirements.txt', 'w+')
file.write('\n'.join(data.get('requirements', [])))
file.close()
