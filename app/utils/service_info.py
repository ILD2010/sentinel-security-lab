import subprocess


def get_services():

    command = ["systemctl", "list-units", "--type=service", "--all", "--no-pager", "--no-legend", "--plain"]

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

    except (subprocess.SubprocessError, OSError) as error:
        print("service monitering error: ", error)
        return []

    services = []

    for line in result.stdout.splitlines():

        parts = line.split(maxsplit=4)

        if len(parts) < 5:
            continue

        name, loaded, active, substate,  description = parts

        services.append({
            "name": name,
            "loaded": loaded,
            "active": active,
            "substate": substate,
            "description": description
        })

    return services