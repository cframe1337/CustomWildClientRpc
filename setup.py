import os

def install_requirements():
    with open('requirements.txt') as r:
        for _ in r:
            os.system('pip install %s' % _)

def start():
    os.system('python3 main.py')
    

if __name__ == '__main__':
    install_requirements()
    start()
