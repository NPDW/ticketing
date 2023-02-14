import subprocess


def server():
    cmd = ["python", "ticketing/manage.py", "runserver"]
    subprocess.run(cmd)
