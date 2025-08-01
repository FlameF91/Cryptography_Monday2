import hashlib
import secrets

# 参数
p = 73
q = 9
g = 64

# 秘钥对
s = secrets.randbelow(q)
h = pow(g, s, p)

# Prover
r = secrets.randbelow(q)
x = pow(g, r, p)

# 使用 Fiat-Shamir 生成挑战 c = H(g, q, h, x)
def compute_challenge(g, q, h, x):
    message = f"{g},{q},{h},{x}".encode()
    return int(hashlib.sha256(message).hexdigest(), 16) % q

c = compute_challenge(g, q, h, x)
y = (r + s * c) % q

# 验证
def verify_noninteractive(g, q, h, x, c, y):
    expected_c = compute_challenge(g, q, h, x)
    left = pow(g, y, p)
    right = (x * pow(h, c, p)) % p
    return c == expected_c and left == right

print(f"验证结果：{'成功' if verify_noninteractive(g, q, h, x, c, y) else '失败'}")
