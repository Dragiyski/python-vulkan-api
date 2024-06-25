import ctypes

class VkCopyBufferInfo2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'srcBuffer': ctypes.c_void_p,
            'dstBuffer': ctypes.c_void_p,
            'regionCount': ctypes.c_uint32,
            'pRegions': ctypes.POINTER(VkBufferCopy2),
        }


from .VkBufferCopy2 import VkBufferCopy2

VkCopyBufferInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcBuffer', ctypes.c_void_p),
    ('dstBuffer', ctypes.c_void_p),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferCopy2)),
]
