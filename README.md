# 🔐 Password Security Analyzer

> 🛡️ A Python-based cybersecurity tool that analyzes password security and provides actionable recommendations.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-red)
![Project](https://img.shields.io/badge/Project-Learning-green)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## 📌 About the Project

**Password Security Analyzer** is a command-line cybersecurity project built with Python.

It analyzes a password using multiple security checks and generates a **security score**, **password rating**, and **recommendations** for improving password security.

This project was created as part of my journey into **Python and Cybersecurity**.

---

## 🚀 Features

| 🔍 Security Check               | ✅ Supported |
| ------------------------------- | ----------- |
| 📏 Password Length              | ✅           |
| 🔠 Uppercase Letters            | ✅           |
| 🔡 Lowercase Letters            | ✅           |
| 🔢 Numbers                      | ✅           |
| 🔣 Special Characters           | ✅           |
| ⚠️ Common Password Detection    | ✅           |
| 🔁 Repeated Character Detection | ✅           |
| 🔢 Sequential Pattern Detection | ✅           |
| 📊 Security Score               | ✅           |
| 💡 Security Recommendations     | ✅           |
| 🔒 Hidden Password Input        | ✅           |

---

## 🧠 How It Works

The analyzer performs several checks on the password:

```text
             🔐 Password
                  │
                  ▼
        ┌───────────────────┐
        │  Password Analyzer │
        └─────────┬─────────┘
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
   📏 Length   🔠 Characters  🔢 Numbers
       │          │          │
       └──────────┼──────────┘
                  ▼
          ⚠️ Weakness Checks
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Common Password      Repeated /
                       Sequential
                        Patterns
        │                   │
        └─────────┬─────────┘
                  ▼
            📊 Security Score
                  │
                  ▼
          💡 Recommendations
```

---

## 🛠️ Technologies Used

* 🐍 **Python 3**
* 🔐 `getpass` module
* 📂 File handling
* 🔄 Loops
* 🧩 Functions
* ✅ Conditional statements
* 📋 Lists
* ⚡ List comprehensions

---

## 📂 Project Structure

```text
password-security-analyzer/
│
├── 🐍 password_analyzer.py
├── 📄 common_passwords.txt
├── 📖 README.md
└── 🚫 .gitignore
```

### 📄 `password_analyzer.py`

Contains the main Python program and password analysis logic.

### 📄 `common_passwords.txt`

Contains a list of commonly used passwords used for basic password comparison.

### 📖 `README.md`

Project documentation.

### 🚫 `.gitignore`

Specifies files that should not be uploaded to GitHub.

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone <your-repository-url>
```

### 2️⃣ Open the project directory

```bash
cd password-security-analyzer
```

### 3️⃣ Run the program

```bash
python password_analyzer.py
```

### 4️⃣ Enter a password

The password will be hidden while you type it.

---

## 🖥️ Example

```text
==================================================
       PASSWORD SECURITY ANALYZER
==================================================

Enter password:

Analyzing password...
--------------------------------------------------
Password length: 12 characters
Password contains uppercase letters.
Password contains lowercase letters.
Password contains numbers.
Password contains special characters.
Password is not in the common password list.
No repeated character pattern detected.
No sequential pattern detected.
--------------------------------------------------
Security Score: 90 / 100
Password Rating: STRONG

RECOMMENDATIONS
--------------------------------------------------
No major weaknesses detected.
Your password meets all basic security checks.
```

---

## 🔎 Security Checks

### 📏 Password Length

Checks whether the password meets the minimum length requirement.

### 🔠 Character Variety

Checks for:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

### ⚠️ Common Password Detection

Compares the password against entries in `common_passwords.txt`.

### 🔁 Repeated Characters

Detects patterns such as:

```text
aaa
111
!!!
```

### 🔢 Sequential Patterns

Detects predictable patterns such as:

```text
1234
abcd
qwer
asdf
```

---

## 🎯 Learning Objectives

This project helped me practice:

* 🐍 Python programming
* 🔐 Basic password-security concepts
* 📂 File handling
* 🔄 Loops and conditions
* 🧩 Functions
* 📋 Lists and list comprehensions
* 🛡️ Basic cybersecurity automation
* 💻 Command-line applications
* 🌐 Git and GitHub

---

## 🚧 Future Improvements

Possible improvements for future versions:

* [ ] 📊 Improve the scoring algorithm
* [ ] 🔑 Password entropy calculation
* [ ] 📚 Expand the common-password database
* [ ] 🌐 Create a web interface
* [ ] 🖥️ Create a graphical user interface
* [ ] 📈 Add detailed security reports
* [ ] 🧪 Add automated tests

---

## ⚠️ Disclaimer

This project is intended for **educational purposes only**.

It provides basic password-strength analysis and should not be considered a professional password-auditing or password-cracking solution.

Never use this tool to test passwords that you do not have permission to analyze.

---

## 👨‍💻 Author

### Aishwarya Bhatt

🔗 **GitHub:** https://github.com/aish01-op

🔗 **LinkedIn:** https://www.linkedin.com/in/aishwarya-bhatt-911301381/

---

⭐ If you found this project useful, consider giving the repository a **star**.

💙 Built with Python while learning **Cybersecurity & Networking**.
