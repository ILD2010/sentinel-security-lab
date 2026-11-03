from flask import Blueprint, render_template
from app.utils.system_info import get_system_info
from app.utils.service_info import get_services


system = Blueprint("system", __name__)


@system.route("/system")
def health():

    system_info = get_system_info()
    return render_template("system.html", system=system_info)


@system.route("/services")
def services():

    service_list = get_services()

    stats = {
        "total": len(service_list),
        "running": 0,
        "stopped": 0,
        "failed": 0,
    }

    for service in service_list:

        if service["active"] == "active":
            stats["running"] += 1

        elif service["active"] == "inactive":
            stats["stopped"] += 1

        elif service["active"] == "failed":
            stats["failed"] += 1


    return render_template("services.html", services=service_list, stats=stats)


@system.route("/logs")
def logs():
    return render_template("logs.html")