import os as o
import sys as s
import time as t
import calendar as c
import datetime as d

from pypresence import Presence


def handle_rpc(userid: any) -> None:
    if len(userid) != 0: 
        start_rpc(userid)
        o.system('pause')
    else: 
        o.system('clear')


def start_rpc(userid: any -> None):
    rpc.update(
        state=f"User ID: {userid}",
        start=round(t.time()),
        large_image="https://github.com/cframe1337/CustomWildClientRpc/blob/main/wild-icon-new.gif?raw=true",
        large_text=f"Build: {c.month_name[d.datetime.today().month]}"
                    + f" {d.datetime.today().day}, {d.datetime.today().year}",
        buttons=[{"label": "Приобрести", "url": "https://wildclient.org/"},
                 {"label": "ВКонтакте", "url": "https://vk.com/wildclient/"}])

    s.stdout.write('\nНажмите Enter чтобы закрыть программу.\n')

def c_input(input_target: str):
    s.stdout.write(f'Input your {input_target}: ')
    return input()

if __name__ == '__main__':
    rpc = Presence(client_id=1209164668015218718)
    # You can use own client id that you copied from project at Discord Developers Portal
    rpc.connect()

    handle_rpc(c_input('userid'))
