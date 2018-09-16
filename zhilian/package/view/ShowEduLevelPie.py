# java与python 岗位在福州的学历要求饼图
from pyecharts import Pie
from package.wash import DataWash
javaEduLevelList,javaEduLevelNumList,pythonEduLevelList,pythonEduLevelNumList=DataWash.washEduLevel()

javaPie = Pie("java岗位学历饼图", title_pos='center')
javaPie.add(
    "",
    javaEduLevelList,
    javaEduLevelNumList,
    radius=[25, 55],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
javaPie.render("javaEduLevelPie.html")

pythonPie = Pie("python岗位学历饼图", title_pos='center')
pythonPie.add(
    "",
    pythonEduLevelList,
    pythonEduLevelNumList,
    radius=[25, 55],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
pythonPie.render("pythonEduLevelPie.html")