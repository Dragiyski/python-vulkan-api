import ctypes

class VkCopyMemoryToAccelerationStructureInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'src': VkDeviceOrHostAddressConstKHR,
            'dst': ctypes.c_void_p,
            'mode': ctypes.c_int,
        }


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkCopyMemoryToAccelerationStructureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', VkDeviceOrHostAddressConstKHR),
    ('dst', ctypes.c_void_p),
    ('mode', ctypes.c_int),
]
