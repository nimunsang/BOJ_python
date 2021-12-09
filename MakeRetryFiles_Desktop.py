#다시 풀어야하는 문제들을 불러오는 코드
#다시 풀어야하는 문제로 새로운 파일을 생성하고,
#그 문제의 링크를 불러온다.

import os
import shutil

origin = 'C:/Users/HEESU/Desktop/Baekjoon_Python'
copy = 'C:/Users/HEESU/Desktop/Baekjoon_Python/RetryFiles'
files = os.listdir(origin)
baekjoonfiles = []
for i in range(len(files)):
    if 'Baekjoon' in files[i]:
        baekjoonfiles.append(files[i])


for baekjoon in baekjoonfiles:
    #(ex) path = 'C:/Users/samsung/Desktop/myPython/Baekjoon_S1'   
    path = origin + '/' + baekjoon
    files = os.listdir(path)
    for file in files:
        filepath = path + '/' + file
        f = open(filepath, 'r', encoding = 'utf8')
        l = f.readline()
        #첫번째 줄을 l로 불러온다.
        # '#다시'가 첫번째 줄에 있다면, 모든 줄을 불러온다
        if '#다시' in l:
            lines = f.readlines()
            for line in lines:
                if 'https' in line:
                    with open(copy + '/' + file, 'w') as newfile:
                        newfile.write(line)
                        newfile.close()
                        break
                        
        f.close()