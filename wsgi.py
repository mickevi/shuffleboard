from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
application = Flask(__name__)
bootstrap = Bootstrap(application)

@application.route("/")
def hello():
    return "Shuffleboard."

@application.route("/board/<bname>")
def board(bname):
    return render_template("board.html", bname=bname)
    return "Board name:" + bname

@application.route("/board/<bname>/add", methods=['POST'])
def badd(bname):
    note = request.form.get("note", None)
    labels = request.form.get("labels", "").split(",")
    if note:
        return "Got: " + note + "\nLabels:" + str(labels)

    else:
        return "I got nothing! " + str(request.form)


if __name__ == "__main__":
    application.run()
