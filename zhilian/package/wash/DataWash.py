# 数据清洗、处理
import sqlite3
from collections import Counter
conn = sqlite3.connect('D:\\Program Files\\sqlite\\data\\智联招聘福州（java_python）\\jobData.db')

def washCity():
    """比较福州python与java岗位在福州各个地址的占比"""
    pythonCityCursor = conn.execute("select city from recruitment where keyword='python'")
    javaCityCursor = conn.execute("select city from recruitment where keyword='java'")
    pythonCityCounter = Counter(pythonCityCursor)
    pythonTempList=pythonCityCounter.most_common()

    javaCityCounter = Counter(javaCityCursor)
    javaTempList = javaCityCounter.most_common()
    pythonDict={}
    for ((key,),number) in pythonTempList:
        pythonDict[key]=number
    javaDict = {}
    for ((key,), number) in javaTempList:
        javaDict[key] = number
    # print(javaDict)
    # print(pythonDict)
    return javaDict,pythonDict

def washMinSalary():
    """最低薪水处理"""
    pythonSalaryCursor = conn.execute("select salary,jobName from recruitment where keyword='python'")
    javaSalaryCursor = conn.execute("select salary,jobName from recruitment where keyword='java'")
    # 清洗 字段为‘校招’‘薪资面议’
    realSalaryList=[]
    pythonjobNameList=[]
    for salaryRow in pythonSalaryCursor:
        # print(salaryRow)
        find=False
        salaryStr=salaryRow[0]
        # print(salaryStr)
        delStrList=['校招','薪资面议']
        for string in delStrList:
            if string in salaryStr:
                find=True
                break
        if not find:
            realSalaryList.append(salaryStr)
            pythonjobNameList.append(salaryRow[1])
    # print(realSalaryList)   形如：['8K-10K', '8K-16K', '5.9K-11.8K']
    # print(len(realSalaryList))
    pythonMinSalaryList=[]
    for salaryStr in realSalaryList:
        index=salaryStr.find('K')
        pythonMinSalaryList.append(float(salaryStr[0:index]))
    # print(pythonMinSalary)

# 清洗 字段为‘校招’‘薪资面议’
    realSalaryList=[]
    javajobNameList = []
    for salaryRow in javaSalaryCursor:
        # print(salaryRow)
        find=False
        salaryStr=salaryRow[0]
        # print(salaryStr)
        delStrList=['校招','薪资面议']
        for string in delStrList:
            if string in salaryStr:
                find=True
                break
        if not find:
            realSalaryList.append(salaryStr)
            javajobNameList.append(salaryRow[1])
    # print(realSalaryList)   形如：['8K-10K', '8K-16K', '5.9K-11.8K']
    # print(len(realSalaryList))
    javaMinSalaryList=[]
    for salaryStr in realSalaryList:
        index=salaryStr.find('K')
        javaMinSalaryList.append(float(salaryStr[0:index]))
    # print(javaMinSalary)
    # print(javajobNameList)
    # print(pythonjobNameList)
    return javajobNameList,javaMinSalaryList,pythonjobNameList,pythonMinSalaryList

def washMaxSalary():
    """最高薪水处理"""
    pythonSalaryCursor = conn.execute("select salary,jobName from recruitment where keyword='python'")
    javaSalaryCursor = conn.execute("select salary,jobName from recruitment where keyword='java'")
    # 清洗 字段为‘校招’‘薪资面议’
    realSalaryList=[]
    pythonjobNameList=[]
    for salaryRow in pythonSalaryCursor:
        # print(salaryRow)
        find=False
        salaryStr=salaryRow[0]
        # print(salaryStr)
        delStrList=['校招','薪资面议']
        for string in delStrList:
            if string in salaryStr:
                find=True
                break
        if not find:
            realSalaryList.append(salaryStr)
            pythonjobNameList.append(salaryRow[1])
    # print(realSalaryList)   形如：['8K-10K', '8K-16K', '5.9K-11.8K']
    # print(len(realSalaryList))
    pythonMaxSalaryList=[]
    for salaryStr in realSalaryList:
        index=salaryStr.find('-')
        pythonMaxSalaryList.append(float(salaryStr[index+1:-1]))
    # print(pythonMaxSalaryList)

# 清洗 字段为‘校招’‘薪资面议’
    realSalaryList=[]
    javajobNameList = []
    for salaryRow in javaSalaryCursor:
        # print(salaryRow)
        find=False
        salaryStr=salaryRow[0]
        # print(salaryStr)
        delStrList=['校招','薪资面议']
        for string in delStrList:
            if string in salaryStr:
                find=True
                break
        if not find:
            realSalaryList.append(salaryStr)
            javajobNameList.append(salaryRow[1])
    # print(realSalaryList)   形如：['8K-10K', '8K-16K', '5.9K-11.8K']
    # print(len(realSalaryList))
    javaMaxSalaryList=[]
    for salaryStr in realSalaryList:
        index=salaryStr.find('-')
        javaMaxSalaryList.append(float(salaryStr[index+1:-1]))
    # print(javaMaxSalaryList)
    # print(javajobNameList)
    # print(pythonjobNameList)
    return javajobNameList,javaMaxSalaryList,pythonjobNameList,pythonMaxSalaryList

def washEduLevel():
    """学历处理"""
    pythonEduLevelCursor = conn.execute("select eduLevel from recruitment where keyword='python'")
    javaEduLevelCursor = conn.execute("select eduLevel from recruitment where keyword='java'")
    pythonCounter=Counter(pythonEduLevelCursor)
    javaCounter = Counter(javaEduLevelCursor)
    pythonPieList=pythonCounter.most_common()
    javaPieList=javaCounter.most_common()
    print(javaPieList)
    javaEduLevelList=[edulevel for ((edulevel),num) in javaPieList]
    javaEduLevelNumList = [num for ((edulevel), num) in javaPieList]
    print(javaEduLevelList)
    print(javaEduLevelNumList)

    print(pythonPieList)
    pythonEduLevelList=[edulevel for ((edulevel),num) in pythonPieList]
    pythonEduLevelNumList = [num for ((edulevel), num) in pythonPieList]
    print(pythonEduLevelList)
    print(pythonEduLevelNumList)
    return javaEduLevelList,javaEduLevelNumList,pythonEduLevelList,pythonEduLevelNumList

def washWorkingExp():
    """工作经验处理"""
    pythonEduLeworkingExpvelCursor = conn.execute("select workingExp from recruitment where keyword='python'")
    javaEduLevworkingExpelCursor = conn.execute("select workingExp from recruitment where keyword='java'")
    pythonCounter = Counter(pythonEduLeworkingExpvelCursor)
    javaCounter = Counter(javaEduLevworkingExpelCursor)
    pythonPieList = pythonCounter.most_common()
    javaPieList = javaCounter.most_common()

    print(javaPieList)
    javaWorkingExpList = [workingExp for ((workingExp), num) in javaPieList]
    javaWorkingExpNumList = [num for ((workingExp), num) in javaPieList]
    print(javaWorkingExpList)
    print(javaWorkingExpNumList)

    print(pythonPieList)
    pythonWorkingExpList = [workingExp for ((workingExp,), num) in pythonPieList]
    pythonWorkingExpNumList = [num for ((workingExp,), num) in pythonPieList]
    print(pythonWorkingExpList)
    print(pythonWorkingExpNumList)
    return javaWorkingExpList, javaWorkingExpNumList, pythonWorkingExpList, pythonWorkingExpNumList

def washJobName():
    """岗位处理"""
    pythonJobNameCursor = conn.execute("select jobName from recruitment where keyword='python'")
    javaJobNameCursor = conn.execute("select jobName from recruitment where keyword='java'")

    javaJobNameCounter=Counter(javaJobNameCursor)
    jobNameList=javaJobNameCounter.most_common()
    javaDistinctJobDict={}
    for ((a,), b) in jobNameList:
        key = str.upper(a)
        if (key in javaDistinctJobDict.keys()):
            javaDistinctJobDict[key]+=b
        else:
            javaDistinctJobDict[key] = b
    pythonJobNameCounter = Counter(pythonJobNameCursor)
    jobNameList = pythonJobNameCounter.most_common()
    pythonDistinctJobDict = {}
    for ((a,), b) in jobNameList:
        key = str.upper(a)
        if (key in pythonDistinctJobDict.keys()):
            pythonDistinctJobDict[key] += b
        else:
            pythonDistinctJobDict[key] = b
    # print(pythonDistinctJobDict)
    return javaDistinctJobDict,pythonDistinctJobDict

def washCompany_size():
    """学历处理"""
    pythonCompanySizeCursor = conn.execute("select company_size from recruitment where keyword='python'")
    javaCompanySizeCursor = conn.execute("select company_size from recruitment where keyword='java'")
    pythonCounter=Counter(pythonCompanySizeCursor)
    javaCounter = Counter(javaCompanySizeCursor)

    pythonFunnelList=pythonCounter.most_common()
    javaFunnelList=javaCounter.most_common()

    # print(javaFunnelList)
    javaCompanySizeList=[funnel for ((funnel,),num) in javaFunnelList]
    javaCompanySizeNumList = [num for ((funnel,), num) in javaFunnelList]
    #
    # print(javaCompanySizeList)
    # print(javaCompanySizeNumList)
    # print(pythonFunnelList)
    pythonCompanySizeList=[funnel for ((funnel),num) in pythonFunnelList]
    pythonCompanySizeNumList = [num for ((funnel), num) in pythonFunnelList]
    # print(pythonCompanySizeList)
    # print(pythonCompanySizeNumList)
    return javaCompanySizeList,javaCompanySizeNumList,pythonCompanySizeList,pythonCompanySizeNumList

def washCompanyType():
    """公司类型处理"""
    pythonCompanyTypeCursor = conn.execute("select company_type from recruitment where keyword='python'")
    javaCompanyTypeCursor = conn.execute("select company_type from recruitment where keyword='java'")
    pythonCounter=Counter(pythonCompanyTypeCursor)
    javaCounter = Counter(javaCompanyTypeCursor)
    pythonPieList=pythonCounter.most_common()
    javaPieList=javaCounter.most_common()
    # print(javaPieList)
    javaCompanyTypeList=[companyType for ((companyType),num) in javaPieList]
    javaCompanyTypeNumList = [num for ((companyType), num) in javaPieList]
    # print(javaCompanyTypeList)
    # print(javaCompanyTypeNumList)
    #
    # print(pythonPieList)
    pythonCompanyTypeList=[companyType for ((companyType),num) in pythonPieList]
    pythonCompanyTypeNumList = [num for ((companyType), num) in pythonPieList]
    # print(pythonCompanyTypeList)
    # print(pythonCompanyTypeNumList)
    return javaCompanyTypeList,javaCompanyTypeNumList,pythonCompanyTypeList,pythonCompanyTypeNumList

if __name__ == '__main__':
    """main函数"""
    # washCity()
    # washMaxSalary()
    # washEduLevel()
    # washJobName()
    # washCompany_size()
    # washCompanyType()