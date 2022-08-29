import itertools

"""
def char_to_binary(c):
    # ord give the integer value of the character, and then we just convert it to binary
    return bin(ord(c))

def binary_to_char(b):
    # convert binary into base 10, and then map it back to its corresponding character
    return chr(int(b, 2))
"""

def get_candidate_for_keys(ciphertext_integers, text_alphabet, key_length, key_alphabet):
    
    # we know from the question that the encryption key consists of exactly 3 lowercase English characters
    # which correspond to ascii integers of [97, 122] inclusive
    possible_integer_values = [list(key_alphabet) for _ in range(key_length)]

    for i in range(key_length):
        for k in key_alphabet:
            for j in range(i, len(ciphertext_integers), key_length):
                n = ciphertext_integers[j]
                if (n^k) not in text_alphabet:
                    possible_integer_values[i].remove(k)
                    break

    return possible_integer_values


def decrypt(s, key):
    # in this particular instance I can skip the converting the string into ascii
    text = ''
    for i in range(0, len(s), len(key)):
        for j in range(len(key)):
            if i+j < len(s):
                text += chr( int(s[i+j]) ^ ord(key[j]) )
    return text

def main(ciphertext_integers, textfile_version):
    
    # https://simple.wikipedia.org/wiki/ASCII gives table for ASCII mapping
    text_alphabet = list(range(32, 123))      # The question tells us that original text contains typical English Characters
    key_length = 3                            # It was given in the problem that the key is length 3
    key_alphabet = list(range(97, 123))       # and that the key contains only lowercase English characters, which correspond to [97, 122] inclusive
    

    # obtain the possibilities for the keys
    possible_integer_values = get_candidate_for_keys(ciphertext_integers, text_alphabet, key_length, key_alphabet)
    key_candidates = ["".join([chr(n) for n in candidate]) for candidate in itertools.product(*possible_integer_values)]
    

    # Normally we would maybe do some Natural Language Processing to see when we get English words
    # In this case, we can manually inspect the resulting text to find the correct key
    """
    for key in key_candidates:
        original_text = decrypt(ciphertext_integers, key)
        print("key:", key)
        print("decrypted text:\n", original_text)
        print()
    """
    
    correct_key_index = [5, 4]
    key = key_candidates[correct_key_index[textfile_version-1]]
    original_text = decrypt(ciphertext_integers, key)
    print("key:", key)
    print("decrypted text:\n", original_text)
    print()

    # calculating result to answer the question
    total = sum([ord(c) for c in original_text])
    print(f"The sum of the ASCII values in the original text is", total)
    return total

if __name__ == "__main__":
    # They changed the textfile for some reason, so there's an old and new version of this question
    #textfile_version = 1
    textfile_version = 2

    with open(f'p059_cipher_v{textfile_version}.txt','r') as f:
        lines = f.readlines()
    
    # obtain the ciphertext from the textfile in the form of ASCII values
    ciphertext_integers = [int(x) for x in lines[0].strip().split(',')]
    
    # This gives the actual ASCII characters, but these are not needed to solve this problem
    ciphertext_characters = [chr(n) for n in ciphertext_integers]

    # we pass in the ASCII integer
    main(ciphertext_integers, textfile_version)