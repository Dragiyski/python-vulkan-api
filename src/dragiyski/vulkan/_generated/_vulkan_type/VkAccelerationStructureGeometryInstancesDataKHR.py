import ctypes

class VkAccelerationStructureGeometryInstancesDataKHR(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryInstancesDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('arrayOfPointers', ctypes.c_uint32),
    ('data', VkDeviceOrHostAddressConstKHR),
]

VkAccelerationStructureGeometryInstancesDataKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'arrayOfPointers': ctypes.c_uint32,
    'data': VkDeviceOrHostAddressConstKHR,
}
