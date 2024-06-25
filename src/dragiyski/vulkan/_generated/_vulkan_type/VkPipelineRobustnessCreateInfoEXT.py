import ctypes

class VkPipelineRobustnessCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffers', ctypes.c_int),
        ('uniformBuffers', ctypes.c_int),
        ('vertexInputs', ctypes.c_int),
        ('images', ctypes.c_int),
    ]

VkPipelineRobustnessCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'storageBuffers': ctypes.c_int,
    'uniformBuffers': ctypes.c_int,
    'vertexInputs': ctypes.c_int,
    'images': ctypes.c_int,
}
