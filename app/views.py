# views.py

from flask import render_template
from flask import request

from app import app
from app import functions_new

missevirt = functions_new.MisseVirt()

@app.route('/')
def index():
    missevirt.list_all_vms()
    vms = missevirt.vms
    return render_template("index.html",
                                vms=vms)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/backup')
def backup():
    vmid = request.args.get('vmid').encode('utf-8')
    vm = missevirt.get_vm(vmid)
    print(missevirt.snapshot_vm(vm))

    return render_template("backup.html",
                                   vm=vm,)
