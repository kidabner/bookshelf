from flask import Flask,request,render_template
import os
app = Flask(__name__)
textList = os.listdir('static')
textList = [i[:-4] for i in textList]
@app.route('/',methods=['POST','GET'])
def home():
    global textList
    data = ''
    if request.method == 'POST':
        book = request.form['book']
#         print(book)
        if book in textList:
            try:
                file = open('static/book/'+book+'.txt','r',encoding='utf-8')
                data = file.read()
                file.close()
            except:
                file = open('static/book/'+book+'.txt','r',encoding='ANSI')
                data = file.read()
                file.close()
    return render_template('bookshelf.html',data=data,textList=textList)
app.run('0.0.0.0',5050)
