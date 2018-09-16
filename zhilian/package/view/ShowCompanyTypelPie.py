# java与python 岗位公司类型饼图
from pyecharts import Pie
from package.wash import DataWash
javaCompanyTypeList,javaCompanyTypeNumList,pythonCompanyTypeList,pythonCompanyTypeNumList=DataWash.washCompanyType()

javaPie = Pie("java岗位公司类型饼图", title_pos='center')
javaPie.add(
    "",
    javaCompanyTypeList,
    javaCompanyTypeNumList,
    radius=[25, 55],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
javaPie.render("javaCompanyTypePie.html")

pythonPie = Pie("python岗位公司类型饼图", title_pos='center')
pythonPie.add(
    "",
    pythonCompanyTypeList,
    pythonCompanyTypeNumList,
    radius=[25, 55],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
pythonPie.render("pythonCompanyTypePie.html")