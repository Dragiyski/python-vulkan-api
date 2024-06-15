import ctypes, sys

class VkPipelineTessellationDomainOriginStateCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('domainOrigin', ctypes.c_int),
    ]

sys.modules[__name__] = VkPipelineTessellationDomainOriginStateCreateInfo
