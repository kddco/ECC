from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import socket

def main():
    # 創建 socket 物件
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 連接伺服器
    s.connect(('localhost', 8000))
    print('已連接伺服器')

    # 選擇一條橢圓曲線，例如 secp256r1
    curve = ec.SECP256K1()

    # 從私鑰計算出公鑰
    private_key = ec.generate_private_key(curve, default_backend())
    public_key = private_key.public_key()

    # 從伺服器接收公鑰
    print('正在從伺服器接收公鑰...')
    server_public_key_bytes = s.recv(1024)
    # byte to object
    server_public_key = serialization.load_pem_public_key(
        server_public_key_bytes,
        backend=default_backend()
    )


    # 將自己的公鑰傳送給伺服器
    print('正在傳送公鑰給伺服器...')
    public_key_bytes = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
    s.send(public_key_bytes)

    # 從自己的私鑰和伺服器的公鑰計算出共同的密鑰
    shared_key = private_key.exchange(ec.ECDH(), server_public_key)
    print('共同的密鑰為：', shared_key.hex())

    # 從伺服器接收共同的密鑰
    print('正在從伺服器接收共同的密鑰...')
    shared_key_str = s.recv(1024).decode()
    shared_key = bytes.fromhex(shared_key_str)

    # 關閉連接
    s.close()

if __name__ == '__main__':
    main()
