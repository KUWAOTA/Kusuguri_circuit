import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
<<<<<<< HEAD
    s.connect(('127.0.0.1', 50007))
=======
    s.connect(('127.0.0.1', 8080))
>>>>>>> 9853fe3d4f119f94b9d802ceafd84a219d73d21f
    # サーバにメッセージを送る
    s.sendall(b'1')
