import ctypes

class VkPipelineCoverageModulationStateCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'coverageModulationMode': ctypes.c_int,
            'coverageModulationTableEnable': ctypes.c_uint32,
            'coverageModulationTableCount': ctypes.c_uint32,
            'pCoverageModulationTable': ctypes.POINTER(ctypes.c_float),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('coverageModulationMode', ctypes.c_int),
        ('coverageModulationTableEnable', ctypes.c_uint32),
        ('coverageModulationTableCount', ctypes.c_uint32),
        ('pCoverageModulationTable', ctypes.POINTER(ctypes.c_float)),
    ]
