import subprocess


def djtest():
    cmd = ["python", "ticketing/manage.py", "runserver"]
    subprocess.run(cmd)
