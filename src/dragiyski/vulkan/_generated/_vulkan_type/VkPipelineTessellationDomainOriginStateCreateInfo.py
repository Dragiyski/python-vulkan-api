import ctypes

class VkPipelineTessellationDomainOriginStateCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('domainOrigin', ctypes.c_int),
    ]

VkPipelineTessellationDomainOriginStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'domainOrigin': ctypes.c_int,
}
