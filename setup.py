import os

def install_requirements():
    with open('requirements.txt') as r:
        for _ in r:
            os.system('pip install %s' % _)

def start():
    install_requirements()
    os.system('python3 main.py')
    

if __name__ == '__main__':
    start()
