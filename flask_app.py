from flask import Flask, render_template, request
import time
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    text = request.form.get('msg')
    if text is None or text == "":
        pass
    else:
        current = open("/home/AcroniusX/mysite/board.txt", "r").read()
        with open("/home/AcroniusX/mysite/board.txt", "w") as f:
            f.write(time.asctime()+"\n"+text+"\n")
            f.write("\n")
            f.write(current)
        f.close()
    #return "Hi"
    return render_template('index.html')

@app.route('/text')
def text():
    return open("/home/AcroniusX/mysite/board.txt", "r").read()


if __name__ == '__main__':
    app.run()
