import ctypes

class VkPhysicalDeviceAccelerationStructureFeaturesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'accelerationStructure': ctypes.c_uint32,
            'accelerationStructureCaptureReplay': ctypes.c_uint32,
            'accelerationStructureIndirectBuild': ctypes.c_uint32,
            'accelerationStructureHostCommands': ctypes.c_uint32,
            'descriptorBindingAccelerationStructureUpdateAfterBind': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_uint32),
        ('accelerationStructureCaptureReplay', ctypes.c_uint32),
        ('accelerationStructureIndirectBuild', ctypes.c_uint32),
        ('accelerationStructureHostCommands', ctypes.c_uint32),
        ('descriptorBindingAccelerationStructureUpdateAfterBind', ctypes.c_uint32),
    ]
