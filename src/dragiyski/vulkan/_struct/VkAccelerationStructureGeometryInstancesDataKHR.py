import ctypes, sys

class VkAccelerationStructureGeometryInstancesDataKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureGeometryInstancesDataKHR

from . import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryInstancesDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('arrayOfPointers', ctypes.c_uint32),
    ('data', VkDeviceOrHostAddressConstKHR),
]
