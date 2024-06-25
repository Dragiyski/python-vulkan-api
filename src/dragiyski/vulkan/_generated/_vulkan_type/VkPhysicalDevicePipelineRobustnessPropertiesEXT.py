import ctypes

class VkPhysicalDevicePipelineRobustnessPropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'defaultRobustnessStorageBuffers': ctypes.c_int,
            'defaultRobustnessUniformBuffers': ctypes.c_int,
            'defaultRobustnessVertexInputs': ctypes.c_int,
            'defaultRobustnessImages': ctypes.c_int,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('defaultRobustnessStorageBuffers', ctypes.c_int),
        ('defaultRobustnessUniformBuffers', ctypes.c_int),
        ('defaultRobustnessVertexInputs', ctypes.c_int),
        ('defaultRobustnessImages', ctypes.c_int),
    ]
