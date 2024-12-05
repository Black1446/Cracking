import hashlib
import itertools
import string

def crack_hash_from_wordlist(password_hash, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            for password in file:
                password = password.strip()
                if hashlib.sha256(password.encode()).hexdigest() == password_hash:
                    return password
        return None
    except FileNotFoundError:
        print(f"Faylka '{wordlist_file}' lama helin!")
        return None

def crack_hash_bruteforce(password_hash, max_length=4):
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt_str = ''.join(attempt)
            if hashlib.sha256(attempt_str.encode()).hexdigest() == password_hash:
                return attempt_str
    return None

if __name__ == "__main__":
    print("""
    #######################################################
    #                                                     #
    #             🇸🇴 SOMALI FLAG (ASCII ART) 🇸🇴            #
    #      ██████████████████████████████████████████     #
    #      ██████████████████████████████████████████     #
    #      ███████████   🟦   🌟   🟦   ████████████     #
    #      ██████████████████████████████████████████     #
    #                                                     #
    #            ** EDUCATIONAL PURPOSE ONLY **           #
    #######################################################
    
    CODED BY BLACK1446
    """)
    hashed_password = input("Gali sha256 password hash-ka: ")
    choice = input("Ma rabtaa inaad isticmaasho (1) Wordlist ama (2) Brute-force? Doorasho: ")
    
    if choice == "1":
        wordlist_file = "passwords.txt"  # Ku qor faylka password-ka
        password = crack_hash_from_wordlist(hashed_password, wordlist_file)
    elif choice == "2":
        max_length = int(input("Gali dhererka ugu badan ee password-ka (tusaale: 4): "))
        password = crack_hash_bruteforce(hashed_password, max_length)
    else:
        print("Doorasho khaldan! Dib isku day.")
        exit()

    if password:
        print(f"\nPassword-ka la helay waa: {password}")
    else:
        print("\nPassword lama helin!")
