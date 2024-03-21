import os

with open('requirements.txt') as r:
    for _ in r:
        os.system('pip install %s' % _)
