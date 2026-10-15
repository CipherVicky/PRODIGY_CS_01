# Prodigy Infotech CS Internship — Task 01

# 🔐 Caesar Cipher Tool

A simple Python-based **Caesar Cipher Encryption and Decryption Tool** that allows users to encrypt and decrypt text using a customizable shift value. This project demonstrates the fundamentals of classical cryptography and text manipulation using Python.

## 📌 Project Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in a message by a specified number of positions in the alphabet.

For example, with a shift value of `3`:

- **Original Text:** `HELLO`
- **Encrypted Text:** `KHOOR`
- **Decrypted Text:** `HELLO`

This tool provides an interactive command-line interface for encrypting and decrypting messages.

## ✨ Features

- 🔒 **Text Encryption** – Encrypt messages using a custom shift value.
- 🔓 **Text Decryption** – Restore encrypted messages using the corresponding shift value.
- 🔄 **Uppercase and Lowercase Support** – Preserves the case of alphabetic characters.
- 🔢 **Flexible Shift Values** – Supports positive, negative, and large integer shifts.
- 📝 **Special Character Preservation** – Keeps spaces, numbers, and punctuation unchanged.
- ✅ **Input Validation** – Handles invalid shift values and menu selections.
- 🔁 **Interactive Interface** – Allows multiple encryption and decryption operations in one session.
- 🐍 **Pure Python** – Uses Python's built-in functionality without requiring external libraries.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Cryptographic Algorithm:** Caesar Cipher
- **Interface:** Command-Line Interface (CLI)
- **Libraries:** Python Standard Library

## 📂 Project Structure

```text
caesar-cipher-tool/
├── caesar_cipher.py
└── README.md
```

## ⚙️ Installation

### Prerequisites

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/caesar-cipher-tool.git
```

Navigate to the project directory:

```bash
cd caesar-cipher-tool
```

## ▶️ How to Run

Execute the Python program using:

```bash
python3 caesar_cipher.py
```

The interactive menu will appear in your terminal.

## 💻 Usage

Choose one of the available operations:

```text
==================================================
           CAESAR CIPHER PROGRAM
==================================================

Choose an option:
  [1] ENCRYPT
  [2] DECRYPT
  [3] EXIT
```

### 🔒 Example: Encryption

Input:

```text
Enter your choice: 1

Enter the message to ENCRYPT: Hello World
Enter shift value (e.g., 3): 3
```

Output:

```text
--------------------------------------------------
Original Text  : Hello World
Shift Value    : 3
Encrypted Text : Khoor Zruog
--------------------------------------------------
```

### 🔓 Example: Decryption

Input:

```text
Enter your choice: 2

Enter the message to DECRYPT: Khoor Zruog
Enter shift value (e.g., 3): 3
```

Output:

```text
--------------------------------------------------
Original Text  : Khoor Zruog
Shift Value    : 3
Decrypted Text : Hello World
--------------------------------------------------
```

## 🧠 How It Works

The Caesar Cipher shifts each alphabetic character by a specified number of positions.

The encryption formula is:

```text
E(x) = (x + k) mod 26
```

The decryption formula is:

```text
D(x) = (x - k) mod 26
```

Where:

- `x` represents the character's position in the alphabet, from 0 to 25.
- `k` represents the shift value.
- `26` represents the number of letters in the English alphabet.
- `mod` ensures that the shift wraps around the alphabet.

For example, shifting `Z` by `3` produces `C`.

The program processes each character individually and preserves non-alphabetic characters without modification.

## 🔐 Security Note

The Caesar Cipher is a **classical substitution cipher intended for educational purposes**.

It is not secure enough for protecting sensitive information because:

- It has only 26 possible effective shifts.
- It is vulnerable to brute-force attacks.
- It does not provide modern cryptographic security.

**Do not use this tool to protect passwords, confidential files, or sensitive personal information.**

For real-world security applications, use established cryptographic algorithms and trusted libraries, such as AES-GCM through a reputable cryptography library.

## 🎯 Learning Objectives

This project helps demonstrate:

- Fundamentals of classical cryptography.
- String manipulation in Python.
- Character encoding using `ord()` and `chr()`.
- Modular arithmetic.
- Functions and conditional statements.
- Loops and exception handling.
- Command-line application development.
- Basic input validation.

## 🚀 Future Improvements

Possible enhancements include:

- [ ] Add a graphical user interface (GUI).
- [ ] Support reading and writing text files.
- [ ] Add automated unit tests.
- [ ] Implement brute-force decryption.
- [ ] Add frequency analysis for cryptanalysis.
- [ ] Create a web-based version of the tool.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

⭐ If you find this project useful, consider giving the repository a star!
