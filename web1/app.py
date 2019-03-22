#fapp
from flask import Flask,render_template
app = Flask(__name__)

poems=[
    {
        "title":"thơ con cóc",
        "content":"hôm nay trời nhẹ lên cao",
        "made_by":"quân",
        "gender":"male"
    },
    {
        "title":"thơ con bò",
        "content":"con bò con",
        "made_by":"quân",
        "gender":"female"
    }
]

print(poems[0])
# @app.route('/')
# def index():
#     return "hello c4e28"


# @app.route("/say-hi/<name>")
# def sayhi(name):
#     return "hi {0}".format(name)


# @app.route("/sum/<int:x>/<int:y>")
# def tong(x,y):
#     return str(x+y)

@app.route("/test")
def test():
    return render_template("lap.html",poems=poems)
 #detall


@app.route("/test/<int:index>")
def detail(index):
    print(index)
    poem=poems[index]
    print(poem)
    return render_template("web2.html",poem=poem,index=index)

  
if __name__ == '__main__':
  app.run( debug=True)
 