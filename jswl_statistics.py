from flask import Flask
import pymysql
import jieba
import jieba.analyse
import xlwt
app = Flask(__name__)

conn = pymysql.connect(
    host='127.0.0.1',  # 主机IP
    port=3306,  # 端口
    user='root',  # 连接数据库用户
    password='root',  # 连接密码
    db='jswl_auto_repair',  # 连接的数据库名称
    charset='utf8'
)


@app.route('/')
def hello_world():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    rs = cursor.execute("select user_remake from customer_survey WHERE 1=1 AND user_remake!=''AND user_remake!='无'")
    _rs = cursor.fetchall()
    data = ""
    for row in _rs:
        print(row['user_remake'])
        data += row['user_remake']
    conn.close()
    with open("E:/python_project/jswl_statistics/word_data.txt", "w") as f:
        f.write(','.join(jieba.cut(data, cut_all=True)))
    statistics()
    return ','.join(jieba.cut(data, cut_all=True))


word_lst = []
word_dict = {}


def statistics():
    with open('E:/python_project/jswl_statistics/word_data.txt') as wf, open(
            "E:/python_project/jswl_statistics/word.txt", 'w') as wf2:
        for word in wf:
            word_lst.append(word.split(','))
            for item in word_lst:
                for item2 in item:
                    if item2 not in word_dict:
                        word_dict[item2] = 1
                    else:
                        word_dict[item2] += 1
            for key in word_dict:
                print(key, word_dict[key])
                wf2.write(key + ' ' + str(word_dict[key]) + '\n')


if __name__ == '__main__':
    app.run()
