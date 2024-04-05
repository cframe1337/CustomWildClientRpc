import os

def install_requirements():
    with open('requirements.txt') as r:
        for _ in r:
            os.system('pip install %s' % _)

if __name__ == '__main__':
    install_requirements()
