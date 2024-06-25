import ctypes

class VkPhysicalDeviceMeshShaderFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'taskShader': ctypes.c_uint32,
            'meshShader': ctypes.c_uint32,
            'multiviewMeshShader': ctypes.c_uint32,
            'primitiveFragmentShadingRateMeshShader': ctypes.c_uint32,
            'meshShaderQueries': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('taskShader', ctypes.c_uint32),
        ('meshShader', ctypes.c_uint32),
        ('multiviewMeshShader', ctypes.c_uint32),
        ('primitiveFragmentShadingRateMeshShader', ctypes.c_uint32),
        ('meshShaderQueries', ctypes.c_uint32),
    ]
