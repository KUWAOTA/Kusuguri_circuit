import socket
import requests
import time
import subprocess
import copy

#state:左手が膨らんでたらtrue、逆はfalse
def event(state):
    api_cmd = ['tplink-smarthome-api', 'setPowerState']
    #LERD:Left_Expand_Right_Deflate：左手膨張右手収縮
    #RELD:Right_Expand_Left_Deflate：右手膨張左手収縮
    if state == None:
        LERD = ['False']
        RELD = ['False']
    else:
        LERD = [chr(state)]
        RELD = [chr(not state)]
    #Left_Expand->Left_Deflate->Right_Expand->Right_Deflate
    Relay_IP= [['192.168.179.14'], [None], [None], [None]]
    subprocess.run(api_cmd + LERD+ Relay_IP[0])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('127.0.0.1', 50007))
    # 1 接続
    s.listen(1)
    # connection するまで待つ
    while True:
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn, addr = s.accept()
        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if data == b'1':
                    #event(True)
                    subprocess.run(['tplink-smarthome-api', 'setPowerState','192.168.179.14','False'])
