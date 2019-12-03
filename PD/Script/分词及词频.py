import jieba
import re
from collections import Counter
cut_words=""
for line in open('/Users/liuxinyi/Desktop/数据/内容/内容/内容.txt',encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", line)
    seg_list=jieba.cut(line,cut_all=False)
    cut_words+=(" ".join(seg_list))
all_words=cut_words.split()
print(all_words)
c=Counter()
for x in all_words:
    if len(x)>1 and x != '\r\n':
        c[x] += 1

print('\n词频统计结果：')
for (k,v) in c.most_common(500):# 输出词频最高的前500个词
    print("%s:%d"%(k,v))



