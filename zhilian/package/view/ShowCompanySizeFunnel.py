# java与python 岗位所在公司规模漏斗图
from pyecharts import Funnel
from package.wash import DataWash
javaCompanySizeList,javaCompanySizeNumList,pythonCompanySizeList,pythonCompanySizeNumList=DataWash.washCompany_size()

javaFunnel = Funnel("java岗位所在公司规模漏斗图", width=1000, height=500, title_pos='center')
javaFunnel.add(
    "公司规模",
    javaCompanySizeList,
    javaCompanySizeNumList,
    s_label_show=True,
    label_pos="outside",
    legend_orient="vertical",
    legend_pos="left",
)
javaFunnel.render("javaCompanySizeFunnel.html")

pythonFunnel = Funnel("python岗位所在公司规模漏斗图", width=1000, height=500, title_pos='center')
pythonFunnel.add(
    "公司规模",
    pythonCompanySizeList,
    pythonCompanySizeNumList,
    s_label_show=True,
    label_pos="outside",
    legend_orient="vertical",
    legend_pos="left",
)
pythonFunnel.render("pythonCompanySizeFunnel.html")

