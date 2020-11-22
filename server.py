import socket
import requests
import time
import subprocess
import copy

#state:左手が膨らんでたらtrue、逆はfalse
def event(state):
    api_cmd = ['tplink-smarthome-api', 'setPowerState', None, None]
    #Left_Expand_Right_Deflate：左手膨張右手収縮
    LERD = api_cmd.copy()
    #Right_Expand_Left_Deflate：右手膨張左手収縮
    RELD = api_cmd.copy()
    if state == None:
        LERD[3] = 'False'
        RELD[3] = 'False'
    else:
        LERD[3] = chr(state)
        RELD[3] = chr(not state)
    #Relay IP
    LERD[2] = '192.168.179.14'
    RELD[2] = '192.168.179.15'

    subprocess.run(LERD)
    subprocess.run(RELD)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('127.0.0.1', 12345))
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
                    subprocess.run(['python', '-m', 'http.server', '10000'])
                    time.sleep(2)
                    subprocess.run(['python', '-m', 'http.server', '11000'])
                    time.sleep(2)
                    subprocess.run(['python', '-m', 'http.server', '12000'])
                    time.sleep(2)
