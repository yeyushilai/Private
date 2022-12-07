#!/usr/bin/python
# -*- coding: utf-8 -*-

import atexit
import ssl

import pyVmomi
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

ssl._create_default_https_context = ssl._create_unverified_context


# Shamelessly borrowed from:
# https://github.com/dnaeon/py-vconnector/blob/master/src/vconnector/core.py
def collect_properties(si, view_ref, obj_type, path_set=None,
                       include_mors=False):
    """
    Collect properties for managed objects from a view ref

    Check the vSphere API documentation for example on retrieving
    object properties:

        - http://goo.gl/erbFDz

    Args:
        si          (ServiceInstance): ServiceInstance connection
        view_ref (pyVmomi.vim.view.*): Starting point of inventory navigation
        obj_type      (pyVmomi.vim.*): Type of managed object
        path_set               (list): List of properties to retrieve
        include_mors           (bool): If True include the managed objects
                                       refs in the result

    Returns:
        A list of properties for the managed objects

    """
    collector = si.content.propertyCollector

    # Create object specification to define the starting point of
    # inventory navigation
    obj_spec = pyVmomi.vmodl.query.PropertyCollector.ObjectSpec()
    obj_spec.obj = view_ref
    obj_spec.skip = True

    # Create a traversal specification to identify the path for collection
    traversal_spec = pyVmomi.vmodl.query.PropertyCollector.TraversalSpec()
    traversal_spec.name = 'traverseEntities'
    traversal_spec.path = 'view'
    traversal_spec.skip = False
    traversal_spec.type = view_ref.__class__
    obj_spec.selectSet = [traversal_spec]

    # Identify the properties to the retrieved
    property_spec = pyVmomi.vmodl.query.PropertyCollector.PropertySpec()
    property_spec.type = obj_type

    if not path_set:
        property_spec.all = True

    property_spec.pathSet = path_set

    # Add the object and property specification to the
    # property filter specification
    filter_spec = pyVmomi.vmodl.query.PropertyCollector.FilterSpec()
    filter_spec.objectSet = [obj_spec]
    filter_spec.propSet = [property_spec]

    # Retrieve properties
    props = collector.RetrieveContents([filter_spec])

    data = []
    for obj in props:
        properties = {}
        for prop in obj.propSet:
            properties[prop.name] = prop.val

        if include_mors:
            properties['obj'] = obj.obj

        data.append(properties)
    return data


def get_container_view(si, obj_type, container=None):
    """
    Get a vSphere Container View reference to all objects of type 'obj_type'

    It is up to the caller to take care of destroying the View when no longer
    needed.

    Args:
        obj_type (list): A list of managed object types

    Returns:
        A container view ref to the discovered managed objects
    """
    if not container:
        container = si.content.rootFolder

    view_ref = si.content.viewManager.CreateContainerView(
        container=container,
        type=obj_type,
        recursive=True
    )
    return view_ref


def search_for_obj(content, vim_type, name, folder=None, recurse=True):
    """
    Search the managed object for the name and type specified

    Sample Usage:

    get_obj(content, [vim.Datastore], "Datastore Name")
    """
    if folder is None:
        folder = content.rootFolder

    obj = None
    container = content.viewManager.CreateContainerView(folder, vim_type,
                                                        recurse)

    for managed_object_ref in container.view:
        if managed_object_ref.name == name:
            obj = managed_object_ref
            break
    container.Destroy()
    return obj


def get_all_obj(content, vim_type, folder=None, recurse=True):
    """
    Search the managed object for the name and type specified

    Sample Usage:

    get_obj(content, [vim.Datastore], "Datastore Name")
    """
    if not folder:
        folder = content.rootFolder

    obj = {}
    container = content.viewManager.CreateContainerView(folder, vim_type,
                                                        recurse)

    for managed_object_ref in container.view:
        obj[managed_object_ref] = managed_object_ref.name

    container.Destroy()
    return obj


def get_obj(content, vim_type, name, folder=None, recurse=True):
    """
    Retrieves the managed object for the name and type specified
    Throws an exception if of not found.

    Sample Usage:

    get_obj(content, [vim.Datastore], "Datastore Name")
    """
    obj = search_for_obj(content, vim_type, name, folder, recurse)
    if not obj:
        raise RuntimeError("Managed Object " + name + " not found.")
    return obj


def connect(args):
    """
    Determine the most preferred API version supported by the specified server,
    then connect to the specified server using that API version, login and return
    the service instance object.
    """

    service_instance = None

    # form a connection...
    try:
        service_instance = SmartConnect(host=args["host"],
                                        user=args["user"],
                                        pwd=args["password"],
                                        port=args["port"])

        # doing this means you don't need to remember to disconnect your script/objects
        atexit.register(Disconnect, service_instance)
    except IOError as io_error:
        print(io_error)

    if not service_instance:
        raise SystemExit(
            "Unable to connect to host with supplied credentials.")

    return service_instance


####################################业务函数####################################
def list_resource(content):
    datacenters = get_all_obj(content, [vim.Datacenter])

    datacenter_list = list()
    for datacenter in datacenters:
        dc_dict = dict()
        dc_dict["name"] = datacenter.name
        dc_dict["vm_folder_name"] = datacenter.vmFolder.name
        dc_dict["host_folder_name"] = datacenter.hostFolder.name

        cluster_list = []
        for child in datacenter.hostFolder.childEntity:
            if isinstance(child, vim.ClusterComputeResource):
                cluster_dict = dict()
                cluster_dict["name"] = child.name

                host_list = []
                for host in child.host:
                    host_dict = dict()
                    host_dict["name"] = host.name
                    host_list.append(host_dict)
                cluster_dict["host_list"] = host_list
                cluster_list.append(cluster_dict)

        dc_dict["cluster_list"] = cluster_list
        datacenter_list.append(dc_dict)
    return datacenter_list
####################################业务函数####################################


if __name__ == '__main__':
    account = dict(
        host="192.168.25.35",
        port=443,
        user="administrator@vsphere.locall",
        password="!QAZ2wsx"
    )

    si = connect(account)
    content = si.RetrieveContent()

    # 版本信息
    version = content.about.version
    print(version)

    # 资源信息
    resources = list_resource(content)
    print(resources)

    # 所有的虚拟机
    # vms = get_all_obj(content, [vim.VirtualMachine])
    # print(vms)

    import pdb
    pdb.set_trace()

    # 根据虚拟机名称获取虚拟机对象
    vm_name = "vmware_manager_yangzhuang_test"
    vm_obj = get_obj(content, [vim.VirtualMachine], vm_name)

    # 根据虚拟机ID获取虚拟机对象
    # vm_uuid = "42068804-2d99-5a89-914b-d3d4a299152c"  # vmware_manager_ubuntu_20.04
    # vm_obj = content.searchIndex.FindByUuid(None, vm_uuid, True)
