from flask import Flask, render_template, request

#Change!!!???

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
    title="姓名判断bot", \
    message="あなたのお名前は？")

@app.route('/', methods=['POST'])
def form():
    field = request.form['field']
    print(len(field))
    if len(field) > 5:
        field = '大吉'
    else: field = '凶'
    return render_template('index.html', \
    title="姓名判断bot", \
    message="あなたの運勢は「%s」です！" % field)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=12345)