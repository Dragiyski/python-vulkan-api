import ctypes, sys

class VkAccelerationStructureBuildSizesInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructureSize', ctypes.c_uint64),
        ('updateScratchSize', ctypes.c_uint64),
        ('buildScratchSize', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkAccelerationStructureBuildSizesInfoKHR
