from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMENENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        session["who_win"] = 0
        
    return render_template("game.html", game=session["board"], turn=session["turn"], who_win=session["who_win"])

# 選擇位置
@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    if session["turn"] == "X":
        session["board"][row][col] = "X"
        if (session["board"][row][0] == "X" and
            session["board"][row][1] == "X" and 
            session["board"][row][2] == "X"):
            session["who_win"] = 1
        if (session["board"][0][col] == "X" and
            session["board"][1][col] == "X" and 
            session["board"][2][col] == "X"):
            session["who_win"] = 1
        if (session["board"][0][0] == "X" and
            session["board"][1][1] == "X" and 
            session["board"][2][2] == "X"):
            session["who_win"] = 1
        if (session["board"][0][2] == "X" and
            session["board"][1][1] == "X" and 
            session["board"][2][0] == "X"):
            session["who_win"] = 1
        session["turn"] = "O"
    else:
        session["board"][row][col] = "O"
        if (session["board"][row][0] == "O" and
            session["board"][row][1] == "O" and 
            session["board"][row][2] == "O"):
            session["who_win"] = 2
        if (session["board"][0][col] == "O" and
            session["board"][1][col] == "O" and 
            session["board"][2][col] == "O"):
            session["who_win"] = 2
        if (session["board"][0][0] == "O" and
            session["board"][1][1] == "O" and 
            session["board"][2][2] == "O"):
            session["who_win"] = 2
        if (session["board"][0][2] == "O" and
            session["board"][1][1] == "O" and 
            session["board"][2][0] == "O"):
            session["who_win"] = 2
        session["turn"] = "X"
    return redirect(url_for("index"))

# Reset
@app.route("/reset")
def reset():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["turn"] = "X"
    session["who_win"] = 0
    return redirect(url_for("index"))