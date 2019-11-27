#! /usr/bin/env python
# coding=utf-8
import lxml
import lxml.html as HTML
import lxml.etree as etree
import codecs

filename = r'C:\Users\Administrator\Desktop\html.txt'
with open(filename, encoding='utf-8') as f:
    data = f.read()

i = 1
hdoc = HTML.fromstring(data)
htree = etree.ElementTree(hdoc)

# 依次打印出hdoc每个元素的文本内容和xpath路径
for t in hdoc.iter():
    print(htree.getpath(t))
    try:
        print(t.text)
    except:
        print(t)
        # print (t.get_attribute())

    print('*************')
    i = i + 1
print(i)

