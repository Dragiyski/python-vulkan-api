import ctypes

class VkAccelerationStructureGeometryAabbsDataKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'data': VkDeviceOrHostAddressConstKHR,
            'stride': ctypes.c_uint64,
        }


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryAabbsDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('data', VkDeviceOrHostAddressConstKHR),
    ('stride', ctypes.c_uint64),
]
