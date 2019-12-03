import jieba

fR = open('/Users/liuxinyi/Desktop/数据/评论/简/评论简/处理后UTF.txt', 'r', encoding='UTF-8')

sent = fR.read()
sent_list = jieba.cut(sent)

fW = open('评论简分词后.txt', 'w', encoding='UTF-8')
fW.write(' '.join(sent_list))

fR.close()
fW.close()
