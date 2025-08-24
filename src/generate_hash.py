import bcrypt

password = b"secretword"
salt = bcrypt.gensalt(rounds=12)
hashed = bcrypt.hashpw(password, salt)

with open("data/hash.txt", "w") as f:
    f.write(hashed.decode())

print("Hash generated and saved to data/hash.txt")

