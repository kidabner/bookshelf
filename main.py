from flask import Flask,request,render_template
import os

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    # 遍历文件夹，获取所有的文件名，返回一个列表
    bookList = os.listdir('static/book/')
    data = ''
    if request.method == 'POST':
        # 提取传递进服务器的文件名
        book = request.form['book']
        try:
            file = open('static/book/'+book,'r',encoding='utf-8')
            data = file.read()
            file.close()
        except:
            file = open('static/book/'+book,'r',encoding='ANSI')
            data = file.read()
            file.close()
    return render_template('bookshelf.html',data=data,bookList=bookList)
app.run('0.0.0.0',8000)
