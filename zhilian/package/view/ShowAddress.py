#python与java岗位在福州各个地点的占比
from pyecharts import Bar
from package.wash import DataWash
from pyecharts_snapshot.main import make_a_snapshot
javaDict,pythonDict=DataWash.washCity()

# {'福州': 326, '福州-鼓楼区': 53, '福州-仓山区': 15, '福州-台江区': 9, '福州-晋安区': 6, '福州-马尾区': 4, '福州-福清': 3, '福州-闽侯县': 2, '福州-长乐': 1, '福州-闽清县': 1}
# {'福州': 345, '福州-鼓楼区': 34, '福州-仓山区': 9, '福州-晋安区': 4, '福州-台江区': 3, '福州-闽侯县': 3, '福州-长乐': 2, '福州-福清': 1, '福州-闽清县': 1, '福州-马尾区': 1}
javaAddr=[]
javaNum=[]
for key,value in javaDict.items():
    javaAddr.append(key)
    javaNum.append(value)

pythonAddr=[]
pythonNum=[]
for key,value in pythonDict.items():
    pythonAddr.append(key)
    pythonNum.append(value)
print(javaNum)
print(pythonNum)
bar = Bar("福州本科java招聘分布柱状图")
bar.add("java", javaAddr,  javaNum, mark_line=["min", "max"])
bar.add("python", pythonAddr, pythonNum, mark_line=["min", "max"])
bar.render("jobAddress.html")
# make_a_snapshot('jobAddress.html', 'test.pdf')