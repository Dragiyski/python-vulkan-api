import ctypes

class VkPipelineCompilerControlCreateInfoAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('compilerControlFlags', ctypes.c_uint32),
    ]

VkPipelineCompilerControlCreateInfoAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'compilerControlFlags': ctypes.c_uint32,
}
