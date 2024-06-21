import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxGeometryCount', ctypes.c_uint64),
        ('maxInstanceCount', ctypes.c_uint64),
        ('maxPrimitiveCount', ctypes.c_uint64),
        ('maxPerStageDescriptorAccelerationStructures', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindAccelerationStructures', ctypes.c_uint32),
        ('maxDescriptorSetAccelerationStructures', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindAccelerationStructures', ctypes.c_uint32),
        ('minAccelerationStructureScratchOffsetAlignment', ctypes.c_uint32),
    ]
