import bcrypt
from tqdm import tqdm

with open("data/hash.txt", "r") as f:
    target_hash = f.read().encode()

with open("data/passwords.txt", "r") as f:
    candidates = [line.strip().encode() for line in f]

print("Starting password cracking attempt...\n")

for pwd in tqdm(candidates, desc="Trying passwords"):
    if bcrypt.checkpw(pwd, target_hash):
        print(f"\nPassword found: {pwd.decode()}")
        break
else:
    print("\nNo match found.")
