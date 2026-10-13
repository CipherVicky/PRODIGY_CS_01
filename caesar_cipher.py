"""
Caesar Cipher Tool
A Python program to encrypt and decrypt text using the Caesar cipher algorithm.
"""

def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    """
    Encrypts or decrypts text using the Caesar cipher algorithm.

    Parameters:
        text (str): The input text to process.
        shift (int): The number of positions to shift characters.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The transformed text.
    """
    # If decrypting, reverse the shift direction
    if mode.lower() == 'decrypt':
        shift = -shift

    result = []

    for char in text:
        if char.isupper():
            # Shift uppercase characters ('A'-'Z')
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted_char)
        elif char.islower():
            # Shift lowercase characters ('a'-'z')
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted_char)
        else:
            # Leave non-alphabetic characters (numbers, punctuation, spaces) unchanged
            result.append(char)

    return "".join(result)


def get_shift_value() -> int:
    """Prompts the user until a valid integer shift value is provided."""
    while True:
        try:
            shift_input = input("Enter shift value (e.g., 3): ").strip()
            return int(shift_input)
        except ValueError:
            print("Invalid input! Please enter a valid integer for the shift value.\n")


def main():
    print("=" * 50)
    print("           CAESAR CIPHER PROGRAM")
    print("=" * 50)

    while True:
        print("\nChoose an option:")
        print("  [1] ENCRYPT")
        print("  [2] DECRYPT")
        print("  [3] EXIT")
        choice = input("Enter your choice (1/2/3 or ENCRYPT/DECRYPT/EXIT): ").strip().lower()

        if choice in ['1', 'encrypt', 'e']:
            mode = 'encrypt'
        elif choice in ['2', 'decrypt', 'd']:
            mode = 'decrypt'
        elif choice in ['3', 'exit', 'q', 'quit']:
            print("\nThank you for using the Caesar Cipher program. Goodbye!")
            break
        else:
            print("\n[!] Invalid selection. Please enter 1, 2, 3 or ENCRYPT, DECRYPT, EXIT.")
            continue

        message = input(f"\nEnter the message to {mode.upper()}: ")
        shift = get_shift_value()

        result = caesar_cipher(message, shift, mode)

        print("-" * 50)
        action_word = "Encrypted" if mode == 'encrypt' else "Decrypted"
        print(f"Original Text  : {message}")
        print(f"Shift Value    : {shift}")
        print(f"{action_word} Text : {result}")
        print("-" * 50)

        # Ask if the user wants to perform another operation
        again = input("\nWould you like to perform another operation? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            print("\nThank you for using the Caesar Cipher program. Goodbye!")
            break


if __name__ == "__main__":
    main()
