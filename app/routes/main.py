from flask import Blueprint, render_template


main = Blueprint("main", __name__)


@main.route("/")
def index():
    lab_status = "Operational"
    
    return render_template("index.html", status=lab_status)

@main.route("/status")
def status():
    return "Sentinel Security Labs - All systems operational!"
