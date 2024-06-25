import ctypes

class VkAccelerationStructureCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'compactedSize': ctypes.c_uint64,
            'info': VkAccelerationStructureInfoNV,
        }


from .VkAccelerationStructureInfoNV import VkAccelerationStructureInfoNV

VkAccelerationStructureCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('compactedSize', ctypes.c_uint64),
    ('info', VkAccelerationStructureInfoNV),
]
