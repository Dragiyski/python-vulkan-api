import ctypes

class VkAccelerationStructureMotionInstanceNV(ctypes.Structure):
    pass

from .VkAccelerationStructureMotionInstanceDataNV import VkAccelerationStructureMotionInstanceDataNV

VkAccelerationStructureMotionInstanceNV._fields_ = [
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('data', VkAccelerationStructureMotionInstanceDataNV),
]

VkAccelerationStructureMotionInstanceNV._type_ = {
    'type': ctypes.c_int,
    'flags': ctypes.c_uint32,
    'data': VkAccelerationStructureMotionInstanceDataNV,
}
