#다시 풀어야하는 문제들을 불러오는 코드

import os
import shutil

origin = 'C:/Users/samsung/Desktop/myPython'
copy = 'C:/Users/samsung/Desktop/retry'
files = os.listdir(origin)
baekjoonfiles = []
for i in range(len(files)):
    if 'Baekjoon' in files[i]:
        baekjoonfiles.append(files[i])

for baekjoon in baekjoonfiles:
    path = origin + '/' + baekjoon
    files = os.listdir(path)
    for file in files:
        filepath = path + '/' + file
        f = open(filepath, 'r', encoding = 'utf8')
        l = f.readline()
        if '#다시' in l:
            shutil.copy(filepath, copy + '/' + file)
        f.close()

