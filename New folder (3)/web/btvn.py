from flask import Flask, render_template
app = Flask(__name__)


@app.route('/about_me')
def index():
    name="đạt",
    age="18",
    hobbies="footballl",
    return render_template('my.html',name=name,age=age,hobbies=hobbies)


if __name__ == '__main__':
  app.run( debug=True)
 