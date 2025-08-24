# 🔐 Password Hardening Lab

## Objective

In this project, I built a small cybersecurity lab to demonstrate **secure password hashing** and the importance of protecting passwords using bcrypt. The goal was to generate password hashes, simulate brute-force attempts safely on sample passwords, and document all steps in a reproducible format suitable for a portfolio presentation.

---

### 🧠 Skills Learned

* Implemented bcrypt hashing with a fixed salt to create reproducible hashes.
* Created a Python-based password cracker to demonstrate brute-force attacks on hashed passwords.
* Used virtual environments and dependency management in Python.
* Documented reproducible steps for running the lab on macOS.
* Practiced safe handling of sensitive data for educational purposes.

---

### 🛠️ Tools Used

* **Python 3.11** – scripting and hashing library support.
* **bcrypt** – secure password hashing and verification.
* **tqdm** – progress bars for simulated cracking attempts.
* **Visual Studio Code** – code editor.
* **Terminal (macOS)** – command-line interface for running scripts and Git operations.

---

## 🧩 Steps

### Step 1: Set up Environment

* Clone the repository:

```bash
git clone https://github.com/<your-username>/Password-Hardening-Lab.git
cd Password-Hardening-Lab
```

* Create a Python virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install bcrypt tqdm
```

<img width="783" height="665" alt="installs" src="https://github.com/user-attachments/assets/8785b1f1-3425-4136-81b9-67774897ec2d" />


---

### Step 2: Prepare Sample Passwords

* Create a `data/passwords.txt` file with sample passwords:

```
password123
letmein
hunter2
secretword
```

<img width="839" height="298" alt="passwords" src="https://github.com/user-attachments/assets/4acfe906-91cc-435a-9643-20c05c139602" />


---

### Step 3: Generate a Fixed Hash

* Create `src/generate_hash.py` to hash a sample password:

```python
import bcrypt

password = b"secretword"
salt = bcrypt.gensalt(rounds=12)
hashed = bcrypt.hashpw(password, salt)

with open("data/hash.txt", "w") as f:
    f.write(hashed.decode())

print("Hash generated and saved to data/hash.txt")
```

* Run in Terminal:

```bash
python src/generate_hash.py
```

<img width="814" height="279" alt="hash" src="https://github.com/user-attachments/assets/a2afcb42-a23e-44a6-8a5a-06b66c23a786" />


---

### Step 4: Simulate Brute-Force Cracking

* Create `src/cracker.py` to check each candidate password against the hash:

```python
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
```

* Run in Terminal:

```bash
python src/cracker.py
```

<img width="1470" height="165" alt="cracked" src="https://github.com/user-attachments/assets/1f62c2f0-3530-43ef-b38b-28b29aed6de0" />


---

### Step 5: Document Findings

* Observed which passwords could be brute-forced.
* Discussed the impact of salts, bcrypt parameters, and memory-hard functions on password security.
* Captured screenshots of VS Code, Terminal outputs, and files for reproducibility.

---

### Step 6: Push Project to GitHub

* Add, commit, and push changes:

```bash
git add .
git commit -m "Initial working demo: password hashing and cracking"
git push origin main
```

---

## Conclusion

This project provided hands-on experience with password hashing and brute-force simulation, demonstrating the importance of using secure hashing algorithms like bcrypt. By generating fixed hashes, safely attempting cracking on sample passwords, and documenting the steps with reproducible scripts, I gained practical skills in Python scripting, password security, and ethical demonstration of attack scenarios. The project highlights how proper password hardening can protect against real-world attacks, while providing a clean, portfolio-ready example.

