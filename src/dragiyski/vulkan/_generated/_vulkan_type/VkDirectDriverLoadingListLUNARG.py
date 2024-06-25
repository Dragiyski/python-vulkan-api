import ctypes

class VkDirectDriverLoadingListLUNARG(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'mode': ctypes.c_int,
            'driverCount': ctypes.c_uint32,
            'pDrivers': ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG),
        }


from .VkDirectDriverLoadingInfoLUNARG import VkDirectDriverLoadingInfoLUNARG

VkDirectDriverLoadingListLUNARG._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mode', ctypes.c_int),
    ('driverCount', ctypes.c_uint32),
    ('pDrivers', ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG)),
]
