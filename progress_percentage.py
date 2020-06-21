import random
import time
from random_words import RandomWords  # pip install RandomWords


def progress_bar(percent, width=30):
    # calling this will update the bar with the new percentage
    hashes = width * percent // 100
    blanks = width - hashes
    print(f"\r[{hashes*'#'}{blanks*' '}] {percent:.0f}%", end='', flush=True)


def progress_bar2(filename, percent, width=30):
    # calling this will update the bar with the new percentage
    hashes = width * percent // 100
    blanks = width - hashes
    print(f"\r[{hashes*'#'}{blanks*' '}] {percent:.0f}% File: {filename}",
          end='', flush=True)


def progress_bar3(filename, count, total, longest, percent, width=30):
    # calling this will update the bar with the new percentage
    hashes = width * percent // 100
    blanks = width - hashes
    cleanup = longest-len(filename)
    print(f"\r[{hashes*'#'}{blanks*' '}] {percent:.0f}% File {count}/{total}: "
          f"{filename}{cleanup*' '}",
          end='', flush=True)


def run_bar():
    for _ in range(101):
        progress_bar(_)
        time.sleep(random.random()*.1)


def run_bar2(filenames):
    for count, filename in enumerate(filenames, 1):
        percent = int((count / len(filenames)) * 100)
        progress_bar2(filename, percent)
        work_sim = .5
        time.sleep(random.random()*work_sim)


def run_bar3(filenames):
    longest = len(max(filenames, key=len))
    for count, filename in enumerate(filenames, 1):
        percent = int((count / len(filenames)) * 100)
        progress_bar3(filename, count, len(filenames), longest, percent)
        work_sim = .5
        time.sleep(random.random()*work_sim)


def generate_filenames(count=10):
    rw = RandomWords()
    filenames = []
    for _ in range(count):
        word = ''.join(rw.random_words(count=3))
        filenames.append(word)
    return filenames


if __name__ == '__main__':
    filenames = generate_filenames(17)
    run_bar3(filenames)
