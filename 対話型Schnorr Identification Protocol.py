import secrets

# Schnorr 参数设置
p = 73                 # 一个素数
q = 9                 # q 是 p-1 的因子（G 的阶）
g = 64                  # 生成元

# 用户密钥
s = secrets.randbelow(q)  # 私钥 s
h = pow(g, s, p)           # 公钥 h = g^s mod p

# Prover 生成提交值
r = secrets.randbelow(q)
x = pow(g, r, p)

# Verifier 发出挑战
c = secrets.randbelow(q)

# Prover 计算响应
y = (r + s * c) % q

# Verifier 验证等式
left = pow(g, y, p)
right = (x * pow(h, c, p)) % p

print(f"验证结果：{'成功' if left == right else '失败'}")
