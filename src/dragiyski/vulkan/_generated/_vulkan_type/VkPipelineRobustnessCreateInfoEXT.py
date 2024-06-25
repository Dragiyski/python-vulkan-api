import ctypes

class VkPipelineRobustnessCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'storageBuffers': ctypes.c_int,
            'uniformBuffers': ctypes.c_int,
            'vertexInputs': ctypes.c_int,
            'images': ctypes.c_int,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffers', ctypes.c_int),
        ('uniformBuffers', ctypes.c_int),
        ('vertexInputs', ctypes.c_int),
        ('images', ctypes.c_int),
    ]
