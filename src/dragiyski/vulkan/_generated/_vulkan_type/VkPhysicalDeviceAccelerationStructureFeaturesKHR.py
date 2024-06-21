import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_uint32),
        ('accelerationStructureCaptureReplay', ctypes.c_uint32),
        ('accelerationStructureIndirectBuild', ctypes.c_uint32),
        ('accelerationStructureHostCommands', ctypes.c_uint32),
        ('descriptorBindingAccelerationStructureUpdateAfterBind', ctypes.c_uint32),
    ]
