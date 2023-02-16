from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import socket
from cryptography.hazmat.primitives import serialization
def main():
    # 創建 socket 物件
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 綁定地址和埠口
    s.bind(('localhost', 8000))
    # 監聽端口，等待客戶端連接
    s.listen(10)
    print('等待客戶端連接...')
    conn, addr = s.accept()
    print('客戶端已連接，地址：', addr)

    # 選擇一條橢圓曲線，例如 secp256r1
    curve = ec.SECP256K1()

    # 產生私鑰
    private_key = ec.generate_private_key(curve, default_backend())
    # 從私鑰計算出公鑰
    public_key = private_key.public_key()

    # 將公鑰傳送給客戶端
    print('正在傳送公鑰給客戶端...')
    public_key_bytes = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
    conn.send(public_key_bytes)

    # 從客戶端接收公鑰
    print('正在從客戶端接收公鑰...')
    other_public_key_bytes = conn.recv(1024)

    # byte to object
    other_public_key = serialization.load_pem_public_key(
        other_public_key_bytes,
        backend=default_backend()
    )

    # 從自己的私鑰和對方的公鑰計算出共同的密鑰
    shared_key = private_key.exchange(ec.ECDH(), other_public_key)
    print('共同的密鑰為：', shared_key.hex())

    # 將共同的密鑰轉換為字串，並傳送給客戶端
    shared_key_str = shared_key.hex()
    print('正在傳送共同的密鑰給客戶端...')
    conn.send(shared_key_str.encode())

    # 關閉連接
    conn.close()
    s.close()

if __name__ == '__main__':
    main()
