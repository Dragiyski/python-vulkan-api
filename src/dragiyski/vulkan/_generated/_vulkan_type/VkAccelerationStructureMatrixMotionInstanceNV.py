import ctypes

class VkAccelerationStructureMatrixMotionInstanceNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'transformT0': VkTransformMatrixKHR,
            'transformT1': VkTransformMatrixKHR,
            'instanceCustomIndex': ctypes.c_uint32,
            'mask': ctypes.c_uint32,
            'instanceShaderBindingTableRecordOffset': ctypes.c_uint32,
            'flags': ctypes.c_uint32,
            'accelerationStructureReference': ctypes.c_uint64,
        }


from .VkTransformMatrixKHR import VkTransformMatrixKHR

VkAccelerationStructureMatrixMotionInstanceNV._fields_ = [
    ('transformT0', VkTransformMatrixKHR),
    ('transformT1', VkTransformMatrixKHR),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]
