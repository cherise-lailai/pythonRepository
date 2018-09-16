# java与python岗位工作经验要求饼图
from pyecharts import Pie
from package.wash import DataWash
javaWorkingExpList,javaWorkingExpNumList,pythonWorkingExpList,pythonWorkingExpNumList=DataWash.washWorkingExp()

javaPie = Pie("java岗位工作经验饼图", title_pos='center')
javaPie.add(
    "",
    javaWorkingExpList,
    javaWorkingExpNumList,
    radius=[25, 55],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
javaPie.render("javaWorkingExpPie.html")

pythonPie = Pie("python岗位工作经验饼图", title_pos='center')
pythonPie.add(
    "",
    pythonWorkingExpList,
    pythonWorkingExpNumList,
    radius=[25, 55],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
pythonPie.render("pythonWorkingExpPie.html")