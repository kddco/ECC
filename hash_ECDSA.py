from ecdsa import SigningKey, VerifyingKey, NIST256p
from hashlib import sha256

# 初始化 curve 和私鑰
curve = NIST256p
private_key = SigningKey.generate(curve=curve)

# 從私鑰產生公鑰
public_key = private_key.get_verifying_key()

# 要簽名的訊息
data = b"Hello, world!"

# 設定 hashfunc 參數為 SHA256
hashfunc = sha256

# 簽名
signature = private_key.sign(data, hashfunc=hashfunc)
int_val = int.from_bytes(signature, "big")
print(int_val)
# 驗證簽名
is_valid = public_key.verify(signature, data, hashfunc=hashfunc)
print(is_valid)
