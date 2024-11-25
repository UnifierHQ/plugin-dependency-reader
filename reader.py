import json
import sys

if sys.version_info.major < 3 or sys.version_info.minor < 12:
    print('Unifier needs Python 3.12 or above to run.')
    print('Please remove jobs using Python 3.11 or older from your workflow.')
    sys.exit(1)

filepath = sys.argv[len(sys.argv)-1] # use last argument as file

if filepath == 'reader.py' or filepath.endswith('/reader.py'):
    # default to plugin.json if filepath was probably not provided
    filepath = 'plugin.json'
    print('Reading from plugin.json as no filepath was given')

with open(filepath) as file:
    data = json.load(file)

file = open('requirements.txt', 'w+')
file.write('\n'.join(data.get('requirements', [])))
file.close()
