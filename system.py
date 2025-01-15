import psutil
from dotenv import load_dotenv
import os
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

load_dotenv('keys.env')

hashedkey = os.getenv('API_KEY')


@app.route("/system_api")
def home():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        token = token.encode('utf-8')
        hashtoken = hashlib.sha256(token).hexdigest()
        if hashedkey != hashtoken:
            return jsonify({"message": "Invalid Bearer Token"}), 200
        else:
            # Get CPU information
            cpu_count = psutil.cpu_count()
            cpu_usage = psutil.cpu_percent(interval=1)

            # Get Memory information
            memory = psutil.virtual_memory()

            memory_percentage = memory.percent

            # Get Disk information
            disk_usage = psutil.disk_usage('/')

            disk_percentage = disk_usage.percent

            # Network Information
            net_io = psutil.net_io_counters()
            net_if_addrs = psutil.net_if_addrs()

            system_info_dict = {
                "CPU_Count": cpu_count,
                "CPU_Usage": cpu_usage,
                "Memory": memory_percentage,
                "Disk_Usage": disk_percentage,
                "Network": net_io,
                "Network_Interface": net_if_addrs,
            }

            return jsonify(system_info_dict), 200
    return jsonify({"message": "Authorization Error"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000, debug=True)
