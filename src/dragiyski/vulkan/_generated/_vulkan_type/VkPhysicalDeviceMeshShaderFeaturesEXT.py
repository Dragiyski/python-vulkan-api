import ctypes, sys

class VkPhysicalDeviceMeshShaderFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('taskShader', ctypes.c_uint32),
        ('meshShader', ctypes.c_uint32),
        ('multiviewMeshShader', ctypes.c_uint32),
        ('primitiveFragmentShadingRateMeshShader', ctypes.c_uint32),
        ('meshShaderQueries', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMeshShaderFeaturesEXT
