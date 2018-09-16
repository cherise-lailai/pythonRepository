#python与java岗位在福州的最高薪水折线图
from pyecharts import Line
from package.wash import DataWash
import random
javajobNameList,javaMaxSalaryList,pythonjobNameList,pythonMaxSalaryList=DataWash.washMaxSalary()
showNum=len(javajobNameList)
if len(javajobNameList)>len(pythonjobNameList):
    showNum = len(pythonjobNameList)

line = Line("折线图示例")
#      is_smooth=True,mark_point=["average"],
#为了图形展示方便,截取部分，采取随机值的
list=[]
for i in range(len(javajobNameList)):
    list.append((javajobNameList[i],javaMaxSalaryList[i]))
showJavaJob=[]
for i in range(showNum):
    showJavaJob.append(random.choice(list))
# print(showJavaJob)
showjavaJobnameArr=[]
showjavaSalArr=[]
for (job,sal) in showJavaJob:
    showjavaJobnameArr.append(job)
    showjavaSalArr.append(sal)
# print(showjavaJobnameArr)


list=[]
for i in range(len(pythonjobNameList)):
    list.append((pythonjobNameList[i],pythonMaxSalaryList[i]))
showPythonJob=[]
for i in range(showNum):
    showPythonJob.append(random.choice(list))
showpythonJobnameArr=[]
showpythonSalArr=[]
for (job,sal) in showPythonJob:
    showpythonJobnameArr.append(job)
    showpythonSalArr.append(sal)
showlist=[str(i) for i in range(1,showNum+1)]
line.add("java",showlist , showjavaSalArr,  is_smooth=True,mark_point=["average"], mark_line=["max", "average"])
line.add("python", showlist, showpythonSalArr, is_smooth=True,mark_point=["average"],mark_line=["max", "average"])
line.render("maxSalaryLineChart.html")