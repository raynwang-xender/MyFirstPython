

#定义MYSAXHandler
from xml.parsers.expat import ParserCreate
class MYSAXHandler(object):
    def start_element(self,name,attrs):
        print("start element: %s,attrs:%s" % (name,attrs))
    def end_element(self,name):
        print("end element:%s" % (name))
    def char_data(slef,data):
        print("text data:%s"%data)

mysaxHandler = MYSAXHandler()
#创建parser
parser = ParserCreate()
#设置开始元素解析句柄
parser.StartElementHandler = mysaxHandler.start_element
#设置结束元素解析句柄
parser.EndElementHandler = mysaxHandler.end_element
#设置data元素解析句柄
parser.CharacterDataHandler = mysaxHandler.char_data
# 前面不能有空格或换行
xml = r'''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <solid android:color="#ffffff" />
    <corners
        android:bottomLeftRadius="360dp"
        android:topLeftRadius="360dp" />
    <size android:height="41dp" />
</shape>

'''
print(type(parser))
parser.Parse(xml)