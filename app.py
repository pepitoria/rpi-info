from flask import Flask, render_template
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET'])
def renderHome():
    return render_template('home.html'
    , uptime = getUptime()
    , myip = getIP()
    , temperature = getTemperature())

def getUptime():
    return runCommand("uptime")

def getIP():
    return runCommand("curl icanhazip.com")

def getTemperature():
    return runCommand("vcgencmd measure_temp")


def runCommand(command: str):
    try:
        normal = subprocess.run(command.split(),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True,
        text=True)
        return normal.stdout
    except:
        return "no data available"