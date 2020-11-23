import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    #
    s.connect(('127.0.0.1', 50007))
    # サーバにメッセージを送る
    s.sendall(b'1')
