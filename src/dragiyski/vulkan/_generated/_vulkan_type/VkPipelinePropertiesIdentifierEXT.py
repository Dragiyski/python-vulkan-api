import ctypes, sys

class VkPipelinePropertiesIdentifierEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]

sys.modules[__name__] = VkPipelinePropertiesIdentifierEXT
