import ctypes

class VkCopyAccelerationStructureToMemoryInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'src': ctypes.c_void_p,
            'dst': VkDeviceOrHostAddressKHR,
            'mode': ctypes.c_int,
        }


from .VkDeviceOrHostAddressKHR import VkDeviceOrHostAddressKHR

VkCopyAccelerationStructureToMemoryInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', ctypes.c_void_p),
    ('dst', VkDeviceOrHostAddressKHR),
    ('mode', ctypes.c_int),
]
