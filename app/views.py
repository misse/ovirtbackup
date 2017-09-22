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
#    snapshot = missevirt.create_snapshot(vm)
    snapshotid = '9cb9bae7-6a30-4283-9cb2-986c6494774a'
    print missevirt.delete_snapshot(vm,snapshotid)
    return render_template("backup.html",
                                   vm=vm,)
