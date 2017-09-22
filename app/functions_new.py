import logging
import datetime

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

import config

logging.basicConfig(level=logging.DEBUG, filename='backup.log')

# This example will connect to the server and print the names and identifiers of all the virtual machines:

class MisseVirt():
    def __init__(self):
        self.connection = sdk.Connection(
            url=config.url,
            username=config.username,
            password=config.password,
            insecure=config.insecure,
            debug=config.debug,
            log=logging.getLogger(),
        )
    def __exit__(self):
        return self.connection.close()

    def list_all_vms(self):
        # Get the reference to the "vms" service:
        vms_service = self.connection.system_service().vms_service()

        # Use the "list" method of the "vms" service to list all the virtual machines of the system:
        self.vms = vms_service.list()

    def get_vm(self,vmid):

        vms_service = self.connection.system_service().vms_service()
        vm = vms_service.vm_service(vmid).get()

        return vm

    def create_snapshot(self,vm):
        # Locate the service that manages the snapshots of the virtual machine:
        vms_service = self.connection.system_service().vms_service()
        snapshots_service = vms_service.vm_service(vm.id).snapshots_service()

        vm = vms_service.vm_service(vm.id).get()

        name = vm.name
        result = snapshots_service.add(
            types.Snapshot(
            description='Snapshot to backup {} taken at {}'.format(name,datetime.datetime.now()),
            ),
        )
        return result 

    def delete_snapshot(self,vm,snapshotid):
        vms_service = self.connection.system_service().vms_service()
        snapshots_service = vms_service.vm_service(vm.id).snapshots_service()
        snapshot = snapshots_service.snapshot_service(snapshotid).get()
	results = dir(snapshot.delete_protected)
        return results


