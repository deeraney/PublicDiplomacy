#coding:utf-8
import paddlehub as hub
senta = hub.Module(name="senta_bilstm")
test_text =  ["文本输入"]
input_dict = {"text": test_text}
results = senta.sentiment_classify(data=input_dict)
for result in results:
 print(result)