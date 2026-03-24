import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

def evaluate_strength(password):
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1
    return score

passwords = []
for i in range(10):
    pwd = generate_password(14)
    strength = evaluate_strength(pwd)
    passwords.append((pwd, strength))

for p, s in passwords:
    print(p, s)