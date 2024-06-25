import ctypes

class VkPipelineCoverageToColorStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('coverageToColorEnable', ctypes.c_uint32),
        ('coverageToColorLocation', ctypes.c_uint32),
    ]

VkPipelineCoverageToColorStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'coverageToColorEnable': ctypes.c_uint32,
    'coverageToColorLocation': ctypes.c_uint32,
}
