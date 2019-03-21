from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:w>/<int:h>')
def bmi(w,h):
    if h>10:
        h1=h/100
    else:
        h1=h
    bmi=w/(h1*h1)
    body=[
        " Severely underweight",
        "Underweight",
        "Normal",
        "Overweight",
        "Obese"

    ]
    if bmi<16:
        condition=body[0]
    if 16<bmi<18.5:
        condition=body[1]
    if 18.5<bmi<25:
        condition=body[2]
    if 25<bmi<30:
        condition=body[3]
    if bmi>30:
        condition=body[4]
        

    return render_template('bmi.html',bmi=bmi,condition=condition)

if __name__ == '__main__':
  app.run( debug=True)
 