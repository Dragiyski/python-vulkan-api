import ctypes

class VkAccelerationStructureBuildRangeInfoKHR(ctypes.Structure):
    _fields_ = [
        ('primitiveCount', ctypes.c_uint32),
        ('primitiveOffset', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('transformOffset', ctypes.c_uint32),
    ]

VkAccelerationStructureBuildRangeInfoKHR._type_ = {
    'primitiveCount': ctypes.c_uint32,
    'primitiveOffset': ctypes.c_uint32,
    'firstVertex': ctypes.c_uint32,
    'transformOffset': ctypes.c_uint32,
}
