import ctypes

class VkAccelerationStructureMotionInstanceNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'type': ctypes.c_int,
            'flags': ctypes.c_uint32,
            'data': VkAccelerationStructureMotionInstanceDataNV,
        }


from .VkAccelerationStructureMotionInstanceDataNV import VkAccelerationStructureMotionInstanceDataNV

VkAccelerationStructureMotionInstanceNV._fields_ = [
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('data', VkAccelerationStructureMotionInstanceDataNV),
]
