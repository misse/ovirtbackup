#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='backup.log')

# This example will connect to the server and print the names and identifiers of all the virtual machines:

# Create the connection to the server:
def api_connection():

    connection = sdk.Connection(
        url='https://ovirt.total-security.local/ovirt-engine/api',
        username='Misse@internal',
        password='qz}\J4BLkM',
        insecure=True,
        debug=False,
        log=logging.getLogger(),
    )
    return connection

# Print the virtual machine names and identifiers:
def list_all_vms():
    connection = api_connection()
    # Get the reference to the "vms" service:
    vms_service = connection.system_service().vms_service()

    # Use the "list" method of the "vms" service to list all the virtual machines of the system:
    all_vms = vms_service.list()
    connection.close()

    return all_vms

def get_vm(vmid):
    connection = api_connection()
    
    vms_service = connection.system_service().vms_service()
    vm = vms_service.vm_service(vmid).get()
   

    connection.close()

    return vm

