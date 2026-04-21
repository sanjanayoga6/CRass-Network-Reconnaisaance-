from flask import Flask, render_template, request, send_file
from scanner import scan_target, defense_analysis

app = Flask(__name__)

last_ports = []

@app.route("/", methods=["GET", "POST"])
def index():
    global last_ports
    result = ""

    if request.method == "POST":
        target = request.form["target"]
        scan_type = request.form["scan_type"]
        mode = request.form["mode"]

        if mode == "attack":
            result, last_ports = scan_target(target, scan_type)
        else:
            result = defense_analysis(target, last_ports)

    return render_template("index.html", result=result)

@app.route("/download")
def download():
    return send_file("scan_report.txt", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)