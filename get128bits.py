import secrets

def generate_random_string():
    # 生成 128-bit 長度隨機字串
    num_bytes = 16
    random_bytes = secrets.token_bytes(num_bytes)
    # 將隨機字串轉換為十六進制格式
    hex_string = random_bytes.hex()
    # 只保留英文和數字
    alphanumeric_hex_string = ''.join(c for c in hex_string if c.isalnum())
    return alphanumeric_hex_string

def test():
    for i in range(10000000):
        random_string = generate_random_string()
        print(len(random_string))
        if len(random_string) != 32:
            print(random_string)
