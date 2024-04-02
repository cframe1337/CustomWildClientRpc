import os as o
import sys as s
import time as t
import calendar as c
import datetime as d

from colorama import init, Fore
from pypresence import Presence

init(autoreset=True)

def premain(userid: any):
    assert len(userid) != 0
    main(userid)
    o.system("pause")


def main(userid: any):
    rpc.update(
        state=f"User ID: {userid}",
        start=round(t.time()),
        large_image="https://github.com/cframe1337/CustomWildClientRpc/blob/main/wild-icon-new.gif?raw=true",
        large_text=f"Build: {c.month_name[d.datetime.today().month]}"
                    + f" {d.datetime.today().day}, {d.datetime.today().year}",
        buttons=[{"label": "Приобрести", "url": "https://wildclient.org/"},
                 {"label": "ВКонтакте", "url": "https://vk.com/wildclient/"}])

    s.stdout.write(Fore.YELLOW + '\nНажмите Enter чтобы закрыть программу.\n')


def title(text: str):
    o.system(f'title {text}')


if __name__ == '__main__':
    rpc = Presence(client_id=1209164668015218718)
    # Здесь вы можете использовать свой клиент айди скопированный в проекте на Discord Developers Portal
    # You can use own client id that you copied from project at Discord Developers Portal
    rpc.connect()

    s.stdout.write(Fore.RED + 'Input your uid' + Fore.YELLOW + ':' + Fore.WHITE + ' ')
    uid = input()
    premain(uid)
