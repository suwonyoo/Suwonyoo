from cgitb import text
from tracemalloc import start
from parse import *

key_original = []
key_decompile = []


file_path_original_binary = "mcf-amd64-clang-O2.txt"
file_path_decompile = "mcf-amd64-clang-O2_strip_result.txt"

# set original binary
f = open(file_path_original_binary)
num_original = 0
lines = f.readlines()
for line in lines:
    addr = str(line).split(":")[0].strip("[")
    key_original.append(addr)


# set decompile - expecilly in spec2006


num_decompile = 0
g = open(file_path_decompile)
lines_ = g.readlines()
for line in lines_:
    addr_decompile = str(line).strip("\n")
    key_decompile.append(addr_decompile[:2] + '00' + addr_decompile[2:])
    num_decompile = num_decompile + 1


'''

# set decompile - expecilly in utils
num_decompile = 0
g = open(file_path_decompile)
lines_ = g.readlines()
for line in lines_:
    addr_decompile = str(line).strip("\n")
    key_decompile.append(addr_decompile[:2] + '00' + str(int(addr_decompile[2])-4) + addr_decompile[3:])
    num_decompile = num_decompile + 1

# check
'''
num = 0
for i in range(len(key_original)):
    for j in range(len(key_decompile)):
        if str(key_original[i]) == str(key_decompile[j]):
            num = num + 1


print(num)
