import ctypes, sys

class VkValidationFlagsEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('disabledValidationCheckCount', ctypes.c_uint32),
        ('pDisabledValidationChecks', ctypes.POINTER(ctypes.c_int)),
    ]

sys.modules[__name__] = VkValidationFlagsEXT
