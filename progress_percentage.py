# note that this is not threadsafe
# strange artefacts can happen in threaded applications

import random
import time
from random_words import RandomWords  # pip install RandomWords


def progress_bar1(percent, width=30):
    # this one shows a bar and a percentage behind it
    # calling this will update the bar with the new percentage
    # use with run_bar1()
    hashes = width * percent // 100
    blanks = width - hashes
    print(f"\r[{hashes*'#'}{blanks*' '}] {percent:.0f}%", end='', flush=True)


def progress_bar2(filename, percent, width=30):
    # this one shows a bar, a percentage and the current file
    # calling this will update the bar with the new percentage
    # use with run_bar2()
    hashes = width * percent // 100
    blanks = width - hashes
    print(f"\r[{hashes*'#'}{blanks*' '}] {percent:.0f}% File: {filename}",
          end='', flush=True)


def progress_bar3(filename, count, total, longest, percent, width=30):
    # this one shows a bar, a percentage, the current file and a file count
    # calling this will update the bar with the new percentage
    # use with run_bar3()
    hashes = width * percent // 100
    blanks = width - hashes
    cleanup = longest-len(filename)
    print(f"\r[{hashes*'#'}{blanks*' '}] {percent:.0f}% File {count}/{total}: "
          f"{filename}{cleanup*' '}",
          end='', flush=True)


def run_bar1():
    for count, filename in enumerate(filenames, 1):
        percent = int((count / len(filenames)) * 100)
        progress_bar1(percent)
        work_sim = .1  # this and the next line are for simulating workload
        time.sleep(random.random()*work_sim)


def run_bar2(filenames):
    for count, filename in enumerate(filenames, 1):
        percent = int((count / len(filenames)) * 100)
        progress_bar2(filename, percent)
        work_sim = .5  # this and the next line are for simulating workload
        time.sleep(random.random()*work_sim)


def run_bar3(filenames):
    longest = len(max(filenames, key=len))
    for count, filename in enumerate(filenames, 1):
        percent = int((count / len(filenames)) * 100)
        progress_bar3(filename, count, len(filenames), longest, percent)
        work_sim = .5  # this and the next line are for simulating workload
        time.sleep(random.random()*work_sim)


def generate_filenames(count=10):
    # this provides filenames to iterate over, replace with e.g. listdir
    rw = RandomWords()
    filenames = []
    for _ in range(count):
        word = ''.join(rw.random_words(count=3))
        filenames.append(word)
    return filenames


if __name__ == '__main__':
    filenames = generate_filenames(17)
    run_bar3(filenames)
