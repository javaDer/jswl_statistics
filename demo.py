from flask import Flask
import pymysql
from pyecharts import Pie
from pyecharts import Bar

conn = pymysql.connect(
    host='127.0.0.1',  # 主机IP
    port=3306,  # 端口
    user='root',  # 连接数据库用户
    password='root',  # 连接密码
    db='online_jswly',  # 连接的数据库名称
    charset='utf8'
)


def greate_pie():
    attr = ["有意向入驻", "无意向入驻", "未知意向"]
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    _is_init = cursor.execute("select  count(0) as isSum  from customer_survey where 1=1 AND user_is_intention ='是'")
    is_count = cursor.fetchone()
    _no_init = cursor.execute("select count(0) as noSum  from customer_survey where 1=1 AND user_is_intention ='否'")
    no_count = cursor.fetchone()
    _none_init = cursor.execute("select count(0) as noneSum from customer_survey where 1=1 AND user_is_intention ='未知'")
    none_count = cursor.fetchone()
    print(is_count['isSum'], no_count['noSum'], none_count['noneSum'])
    v1 = [is_count['isSum'], no_count['noSum'], none_count['noneSum']]
    pie = Pie("金沙物流园客户意向图")
    pie.add("金沙物流园客户意向图", attr, v1, is_label_show=True)
    pie.render()


def greate_bar():
    attr = ["幼儿园", "小学", "初中", "未知"]
    bar = Bar("客户子女上学情况")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    _kindergarten = cursor.execute(
        "select  count(0) as kindergartenSum  from customer_survey where 1=1 AND user_children_school_level ='幼儿园'")
    kindergarten_count = cursor.fetchone()
    _primaryschool = cursor.execute(
        "select  count(0) as _primaryschoolSum  from customer_survey where 1=1 AND user_children_school_level ='小学'")
    primaryschool_count = cursor.fetchone()
    _middleschool = cursor.execute(
        "select  count(0) as middleschoolSum  from customer_survey where 1=1 AND user_children_school_level ='中学'")
    middleschool_count = cursor.fetchone()
    _noneschool = cursor.execute(
        "select  count(0) as noneSum  from customer_survey where 1=1 AND user_children_school_level ='未知'")
    none_count = cursor.fetchone()
    v1 = [kindergarten_count["kindergartenSum"], primaryschool_count["_primaryschoolSum"],
          middleschool_count["middleschoolSum"], none_count["noneSum"]]
    bar.add("汽车服务综合市场", attr, v1)
    conn.close()
    bar.render()


if __name__ == '__main__':
    greate_pie(),
    greate_bar()
