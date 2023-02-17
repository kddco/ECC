import ecdsa
import hashlib

#先hash後簽章
# 產生 ECDSA 金鑰
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()

# 假設待簽名的訊息為 "hello, world!"
message = "hello, world!".encode('utf-8')

# 計算 SHA-256 雜湊值
h = hashlib.sha256(message).digest()

# 使用私鑰對雜湊值進行簽名
signature = sk.sign(h)

# 使用公鑰驗證簽名
assert vk.verify(signature, h)
