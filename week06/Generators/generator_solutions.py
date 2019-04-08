import subprocess
import pyautogui
import sys
import os
import random
    # Implement a function that takes two iterables and returns another one that concatenate the two iterables.

def chain(iterable_one, iterable_two):
    for elem in iterable_one:
        yield elem
    for elem in iterable_two:
        yield elem


# print(list(chain(range(0, 4), range(4, 8))))

def compress(iterable, mask):
    for elem, flag in zip(iterable,mask):
        if flag == True:
            yield elem


# print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))


def cycle(iterable):
    while True:
        for elem in iterable:
            yield elem

# endless = cycle(range(0,10))
# for item in endless:
#     print(item)

# read a book chapter by chapter
def book(path):
    root,dirnames,filenames = next(os.walk(path))
    for file in sorted(filenames):
        with open(root + '/' + file) as f:
            result_lines = []
            for  line in f:
                if line[0] == '#':
                    old_result = ''.join(result_lines)
                    result_lines = [line]
                    if old_result == '':
                        continue
                    yield old_result
                else:
                    result_lines.append(line)
def main():
    # path = sys.argv[1]
    # gen = book(path)
    # str_input = input()
    # while str_input == ' ':
    #     print(next(gen))
    #     str_input = input()
    chapter_generator(6,40)

def rand_word_generator():
    with open('/etc/dictionaries-common/words') as word_file:
        file_to_list = word_file.readlines()
        random.shuffle(file_to_list)
        for word in file_to_list:
            yield str(word).strip()
def chapter_generator(chapter_count,chap_length):
    with open("myBook.txt",'a') as f:
        wordgen = rand_word_generator()

        for chapter_num in range(chapter_count):
            f.write('#Chapter' + str(chapter_num) + '\n')
            for i in range(chap_length):
                f.write(next(wordgen) + ' ')
                if random.random() > 0.95:
                    f.write('.\n')
            f.write('\n\n')

#if mouse is in upper left corner say Im not ready

def mousegen():
    while True:
        yield pyautogui.position()
def main2():
    stop_input = input()
    gen = mousegen()
    subprocess.call(['speech-dispatcher'])        #start speech dispatcher
    while stop_input != 'q':
        cur_position = next(gen)
        if cur_position[0] < 300 and cur_position[1] < 300:
            subprocess.call(['spd-say', '"You are in the upper right corner"'])
        stop_input = input()

if __name__ == '__main__':
    main()




#generate random book:





