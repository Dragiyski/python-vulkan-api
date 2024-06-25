import ctypes

class VkPipelineRepresentativeFragmentTestStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('representativeFragmentTestEnable', ctypes.c_uint32),
    ]

VkPipelineRepresentativeFragmentTestStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'representativeFragmentTestEnable': ctypes.c_uint32,
}
