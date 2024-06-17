import ctypes, sys

class VkPhysicalDeviceVulkan13Features(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustImageAccess', ctypes.c_uint32),
        ('inlineUniformBlock', ctypes.c_uint32),
        ('descriptorBindingInlineUniformBlockUpdateAfterBind', ctypes.c_uint32),
        ('pipelineCreationCacheControl', ctypes.c_uint32),
        ('privateData', ctypes.c_uint32),
        ('shaderDemoteToHelperInvocation', ctypes.c_uint32),
        ('shaderTerminateInvocation', ctypes.c_uint32),
        ('subgroupSizeControl', ctypes.c_uint32),
        ('computeFullSubgroups', ctypes.c_uint32),
        ('synchronization2', ctypes.c_uint32),
        ('textureCompressionASTC_HDR', ctypes.c_uint32),
        ('shaderZeroInitializeWorkgroupMemory', ctypes.c_uint32),
        ('dynamicRendering', ctypes.c_uint32),
        ('shaderIntegerDotProduct', ctypes.c_uint32),
        ('maintenance4', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceVulkan13Features
