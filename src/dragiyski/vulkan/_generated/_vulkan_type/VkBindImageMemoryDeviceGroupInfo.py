import ctypes

class VkBindImageMemoryDeviceGroupInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'deviceIndexCount': ctypes.c_uint32,
            'pDeviceIndices': ctypes.POINTER(ctypes.c_uint32),
            'splitInstanceBindRegionCount': ctypes.c_uint32,
            'pSplitInstanceBindRegions': ctypes.POINTER(VkRect2D),
        }


from .VkRect2D import VkRect2D

VkBindImageMemoryDeviceGroupInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('deviceIndexCount', ctypes.c_uint32),
    ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ('splitInstanceBindRegionCount', ctypes.c_uint32),
    ('pSplitInstanceBindRegions', ctypes.POINTER(VkRect2D)),
]
