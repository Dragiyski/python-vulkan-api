import ctypes

class VkAccelerationStructureGeometryInstancesDataKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'arrayOfPointers': ctypes.c_uint32,
            'data': VkDeviceOrHostAddressConstKHR,
        }


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryInstancesDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('arrayOfPointers', ctypes.c_uint32),
    ('data', VkDeviceOrHostAddressConstKHR),
]
