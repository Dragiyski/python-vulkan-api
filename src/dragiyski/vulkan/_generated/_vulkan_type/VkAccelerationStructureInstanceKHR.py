import ctypes

class VkAccelerationStructureInstanceKHR(ctypes.Structure):
    pass

from .VkTransformMatrixKHR import VkTransformMatrixKHR

VkAccelerationStructureInstanceKHR._fields_ = [
    ('transform', VkTransformMatrixKHR),
    ('instanceCustomIndex', ctypes.c_uint32, 24),
    ('mask', ctypes.c_uint32, 8),
    ('instanceShaderBindingTableRecordOffset', ctypes.c_uint32, 24),
    ('flags', ctypes.c_uint32, 8),
    ('accelerationStructureReference', ctypes.c_uint64),
]

VkAccelerationStructureInstanceKHR._type_ = {
    'transform': VkTransformMatrixKHR,
    'instanceCustomIndex': ctypes.c_uint32,
    'mask': ctypes.c_uint32,
    'instanceShaderBindingTableRecordOffset': ctypes.c_uint32,
    'flags': ctypes.c_uint32,
    'accelerationStructureReference': ctypes.c_uint64,
}
