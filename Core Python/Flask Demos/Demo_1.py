from flask import Flask,render_template

app= Flask(__name__)


@app.route("/signin")
def login():
    return render_template("index.html")

@app.route("/signup")
def register():
    return "in Register page"

if __name__=="__main__":
    app.run()
