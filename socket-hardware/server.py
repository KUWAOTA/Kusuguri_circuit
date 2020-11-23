import requests
import time
import subprocess
import asyncio
import websockets

def apihitter(on_off, Relay_IP):
    api_cmd = ['tplink-smarthome-api', 'setPowerState'] + [Relay_IP]
    #npmはtrueだが、pythonはTrueなので
    if on_off :
        api_cmd += ['true']
    else:
        api_cmd += ['false']
    print(api_cmd)
    subprocess.run(api_cmd)

#state:左手が膨らんでたらtrue、逆はfalse
def loop(Relay_IPs):

    #LERD:Left_Expand_Right_Deflate：左手膨張右手収縮
    #RELD:Right_Expand_Left_Deflate：右手膨張左手収縮
    #[Left_Expand->Left_Deflate]->[Right_Expand->Right_Deflate]
    looptimes = 6
    for i in range(looptimes):
        apihitter(i % 2 == 0 and i != 5, Relay_IPs[0][0])
        apihitter(i % 2 == 1 and i != 5, Relay_IPs[0][1])
        apihitter(i % 2 == 1 and i != 5, Relay_IPs[1][0])
        apihitter(i % 2 == 0 and i != 5, Relay_IPs[1][1])
        time.sleep(2)




def notweb_socket(Relay_IPs):
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
                        pass

async def event(websocket, path):
    Relay_IPs = [['192.168.179.14','192.168.179.15'],['192.168.179.16','192.168.179.17']]
    name = await websocket.recv()
    if bool(name):
        loop(Relay_IPs)

def main():
    start_server = websockets.serve(hello, "localhost", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
