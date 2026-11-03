import os
import platform
import time
import psutil


def get_system_info():

    #CPU info
    cpu_usage = psutil.cpu_percent(interval=0.1)

    #Memory info
    memory = psutil.virtual_memory()

    #Storage info
    disk = psutil.disk_usage("/")


    #System uptime
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)
    uptime_hours = uptime_seconds // 3600


    #System information
    system_info = {
        "hostname": platform.node(),
        "operating_system": platform.system(),
        "kernel": platform.release(),
        "cpu_usage": cpu_usage,
        "cpu_cores": psutil.cpu_count(),
        "memory_total": round(memory.total / (1024 ** 3), 2),
        "memory_used": round(memory.used / (1024 ** 3), 2),
        "memory_percent": memory.percent,
        "disk_total": round(disk.total / (1024 ** 3), 2),
        "disk_used": round(disk.used / (1024 ** 3), 2),
        "disk_percent": disk.percent,
        "uptime_hours": uptime_hours
    }

    return system_info
