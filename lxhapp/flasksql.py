#使用pymysql连接MySQL数据库
import pymysql
from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap = Bootstrap(app)

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='db20060101', db='test_db', charset='utf8')

cursor = conn.cursor()

cursor.execute("select * from zjxytypes")



@app.route('/', methods=['GET','POST'])
def index():
    s=None
    n=None
    for row in cursor.fetchall(): #前面不能使用fetchalll（）否则这里会查询不到
        #把每行取的每个值分派到表格中
        s='<tr><td>'+str(row[0])+'</td>'+'<td>'+str(row[1])+'</td>'+'<td>'+str(row[2])+'</td>'+'<td>'+str(row[3])+'</td>'+'<td>'+str(row[4])+'</td>'+'<td>'+str(row[5])+'</td>'+'<td>'+str(row[6])+'</td>'+'<td>'+str(row[7])+'</td></tr>'
        n=str(n)+s
    #print(n)
    return '<title>测试</title><table>%s</table>' % n

@app.route('/zjsql')
def zjsql():
    rows = cursor.fetchall()
    #将查询结果作为参数传递给模板
    return render_template('zjsql.html',rows=rows)

if __name__== '__main__':
    app.run(debug=True)

conn.commit()

conn.close()