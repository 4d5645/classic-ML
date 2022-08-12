import re
import numpy as np
from scipy.spatial.distance import cosine
import operator

f = open('sentences.txt', 'r')
data_l = list(f.readlines())
num_lines = 0
num_words = 0
current = 0
words = dict()
for line in data_l:
    num_lines = num_lines + 1
    line_words = re.split('[^a-z]', line.lower())
    for word in line_words:
        if (len(word) != 0) & (not(word in words)):
            words[word] = num_words  #присваивание элементу словаря индекса
            num_words = num_words + 1
matrix = np.zeros((num_lines, num_words))
for line in data_l:
    line_words = re.split('[^a-z]', line.lower())
    for word in line_words:
        if (len(word)!=0):
            matrix[current, words[word]] = matrix[current, words[word]] + 1
    current = current + 1
cos_dict = dict()
ref_raw = matrix[0, :]
for line_num in (range(num_lines)):
    current_raw = matrix[line_num, :]
    cos_dict[line_num] = cosine(ref_raw,current_raw)
cos_dict_sorted = sorted(cos_dict.items(), key = operator.itemgetter(1))
res_file_obj=open('submission_result.txt','w')
i = 0
for line in cos_dict_sorted:
    i = i + 1
    if (i < 2)|(i > 3): continue
    res_file_obj.write(str(line[0]))
    res_file_obj.write(' ')
res_file_obj.close()
print(cos_dict_sorted)
