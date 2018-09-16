# java与python岗位名称词云图
from pyecharts import WordCloud
from package.wash import DataWash
javaDistinctJobDict,pythonDistinctJobDict=DataWash.washJobName()
# print(jobWordDict)
javaJobName=[k for (k,v) in javaDistinctJobDict.items()]
javaJobNameNum=[v for (k,v) in javaDistinctJobDict.items()]
pythonJobName=[k for (k,v) in pythonDistinctJobDict.items()]
pythonJobNameNum=[v for (k,v) in pythonDistinctJobDict.items()]

javaWordcloud = WordCloud(width=1300, height=620)
javaWordcloud.add("", javaJobName, javaJobNameNum, word_size_range=[20, 100])
javaWordcloud.render('javaJobNameWordCloud.html')
pythonWordcloud = WordCloud(width=1300, height=620)
pythonWordcloud.add("", pythonJobName, pythonJobNameNum, word_size_range=[20, 100])
pythonWordcloud.render('pythonJobNameWordCloud.html')
