import sqlite3
from string import ascii_lowercase,ascii_uppercase
low = ''.join(list(ascii_lowercase))
up  = ''.join(list(ascii_uppercase)) 
letters = up + low
import random

import hashlib


def make_it_secret(message):
    return hashlib.md5(message.encode()).hexdigest()

def word_gen():
    word = ''
    for idx in range(5):
        word += letters[random.randint(0,50)]
    return word

def main():
    decoded_words = []
    words = """
    8021f7e4b05dada0ad3d47567e52249e 6864f389d9876436bc8778ff071d1b6c a4757d7419ff3b48e92e90596f0e7548
cae8d14edd025e72c59dbab6f378c95a d78b6f30225cdc811adfe8d4e7c9fd34 b5f3729e5418905ad2b21ce186b1c01d ab86a1e1ef70dff97959067b723c5c24
7e1321b3c8423b30c1cb077a2e3ac4f0 4015e9ce43edfb0668ddaa973ebc7e87 03d59e663c1af9ac33a9949d1193505a a80698366d88c5ebf1357689cc3ca8fe 1952a01898073d1e561b9b4f2e42cbd7 c5af0543407a6e8ba11db6a69f792014 c67fd61e3b7d35f07e3ca92c8a84a5ab 6c92285fa6d3e827b198d120ea3ac674
1666ca77ab75f7d731e645fa6ef4fc60 4ad44a676546464b2c4b8c9e4529bdf0 d4408643ccbd7e83d0c54f42e405d618
90f910a44798e0d68879b43382042a40 0b3b8343a911a6327e7f3d8038fd58a6
dd7536794b63bf90eccfd37f9b147d7f 92159805cf28ee78e13c41ebbbb1aeb4 639bae9ac6b3e1a84cebb7b403297b79 0cc175b9c0f1b6a831c399e269772661 3e1867f5aee83045775fbe355e6a3ce1
"""
    words = words.split(' ')
    count = len(words)
    conn = sqlite3.connect("words.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS words (word  VARCHAR(80) PRIMARY KEY, translation VARCHAR(6))
        """
        )
    while count>0:
        word = word_gen()
        cur_word = make_it_secret(word)
        cursor.execute(
            f"""
            SELECT * FROM words WHERE translation='{word}'
            """)
        if cursor.fetchone() == []:
            #if not in database check
            if cur_word in words:
                count -= 1
                decoded_words.append((cur_word,word))
            cursor.execute(
                """
                INSERT INTO words (word,translation) VALUES(cur_word,word)
                """)
    print(decoded_words)

if __name__ == '__main__':
    main()