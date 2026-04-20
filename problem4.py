import string  

def load_cipher(file_path):
    with open(file_path, 'r') as f:
        # Read the file, split by commas, convert each value to int, and return as a list
        return list(map(int, f.read().split(',')))

# XOR decryption function
def decrypt(cipher, password):
    password_bytes = [ord(k) for k in password] #ord convert character to integer
    decrypted = []  #to store decrypted numeric values

    # Loop through each number in the cipher
    for i, c in enumerate(cipher):
        # XOR the cipher value with the corresponding password byte
        decrypted_char = c ^ password_bytes[i % len(password_bytes)] # 0,1,2,0,1,2 (i % 3)
        # makes the key repeat.
        decrypted.append(decrypted_char)

    return ''.join(chr(c) for c in decrypted) #chr convert them back to characters , and we join them

def score_text(text):
    common_chars = "abcdefghijklmnopqrstuvwxyz"
    score = 0

    for char in text:
        if char in common_chars:
            score += 1        
        else:
            score -= 1       

    return score

def find_password(cipher):
    best_score = float('-inf')  # Start with lowest possible score
    best_password = ""          # Store best password found
    best_message = ""           # Store best decrypted message

    # Try every combination of 3 lowercase letters (aaa → zzz)
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                password = a + b + c  # Build password

                # Decrypt using current password
                decrypted = decrypt(cipher, password)

                # Score the decrypted text
                score = score_text(decrypted)

                # If this is the best result so far, store it
                if score > best_score:
                    best_score = score
                    best_password = password
                    best_message = decrypted

    # Return the best password and corresponding decrypted message
    return best_password, best_message

# MAIN execution block
if __name__ == "__main__":
    cipher = load_cipher("Files\\p059_cipher.txt")

    password, message = find_password(cipher)

    print("The 3 letters password is:", password)
    print("The Decrypted Message is:", message)
