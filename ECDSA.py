import ecdsa

# 產生 ECDSA 金鑰
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()

# 假設待簽名的訊息為 "hello, world!"
message = "hello, world!".encode('utf-8')

# 直接使用私鑰對訊息進行簽名
signature = sk.sign(message)

# 使用公鑰驗證簽名
assert vk.verify(signature, message)
