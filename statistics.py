import os
import pandas as pd
import jieba
from collections import defaultdict

# Load business data
# Load norms data
root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
norm2business_path = root_path + '/data/norm2business_100.csv'
norm2business_csv = pd.read_csv(norm2business_path, encoding='gbk', header=None, converters={2: str})
norm2business = norm2business_csv.dropna(axis=0, how='any').values  # Drop 'nan' then to list

count = defaultdict(int)
all = []
max_len = 100000
cur = None
for norm in norm2business:
    words = [word for word in jieba.cut(norm[1])]
    if len(words) < max_len:
        max_len = len(words)
        cur = words
for word in all:
    count[word] += 1
c = sorted(count.items(), key=lambda item: item[1])

root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
questions_path = root_path + '/data/questions.csv'
questions_csv = pd.read_csv(questions_path, encoding='gbk', header=None)
questions = questions_csv.values  # to list
all_text = [question[0] for question in questions]
all_words = []
for text in all_text:
    all_words += [word for word in jieba.cut(text)]
count = defaultdict(int)
for word in all_words:
    count[word] += 1
c = sorted(count.items(), key=lambda item: item[1])
print(c)
