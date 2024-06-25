import ctypes

class VkAccelerationStructureSRTMotionInstanceNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'transformT0': VkSRTDataNV,
            'transformT1': VkSRTDataNV,
            'instanceCustomIndex': ctypes.c_uint32,
            'mask': ctypes.c_uint32,
            'instanceShaderBindingTableRecordOffset': ctypes.c_uint32,
            'flags': ctypes.c_uint32,
            'accelerationStructureReference': ctypes.c_uint64,
        }


from .VkSRTDataNV import VkSRTDataNV

VkAccelerationStructureSRTMotionInstanceNV._fields_ = [
    ('transformT0', VkSRTDataNV),
    ('transformT1', VkSRTDataNV),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]
