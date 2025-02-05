import psutil
from dotenv import load_dotenv
import os
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

load_dotenv('keys.env')

hashedkey = os.getenv('API_KEY')

def authenticate(token):
    if not token or not token.startswith('Bearer '):
        return False
    token = token.split(' ')[1].encode('utf-8')
    return hashlib.sha256(token).hexdigest() == hashedkey

@app.route("/cpu", methods=["GET"])
def get_cpu():
    if not authenticate(request.headers.get('Authorization')):
        return jsonify({"message": "Authorization Error"}), 401
    return jsonify({
        "CPU_Count": psutil.cpu_count(),
        "CPU_Usage": psutil.cpu_percent(interval=1)
    }), 200

@app.route("/memory", methods=["GET"])
def get_memory():
    if not authenticate(request.headers.get('Authorization')):
        return jsonify({"message": "Authorization Error"}), 401
    return jsonify({
        "Memory_Usage": psutil.virtual_memory().percent
    }), 200

@app.route("/disk", methods=["GET"])
def get_disk():
    if not authenticate(request.headers.get('Authorization')):
        return jsonify({"message": "Authorization Error"}), 401
    return jsonify({
        "Disk_Usage": psutil.disk_usage('/').percent
    }), 200

@app.route("/network", methods=["GET"])
def get_network():
    if not authenticate(request.headers.get('Authorization')):
        return jsonify({"message": "Authorization Error"}), 401
    return jsonify({
        "Network_IO": psutil.net_io_counters()._asdict(),
        "Network_Interfaces": {iface: [addr._asdict() for addr in addrs] for iface, addrs in psutil.net_if_addrs().items()}
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000, debug=True)
