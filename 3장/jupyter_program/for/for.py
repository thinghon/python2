from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def loop_test():
    dept_list = ['컴퓨터공학과','전자공학과','기계공학과','화공과']
    return render_template('loop.html',values=dept_list)

if __name__=="__main__":
    app.run(host="211.229.235.191", port="8080")