import ctypes, sys

class VkDrawMeshTasksIndirectCommandEXT(ctypes.Structure):
    _fields_ = [
        ('groupCountX', ctypes.c_uint32),
        ('groupCountY', ctypes.c_uint32),
        ('groupCountZ', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDrawMeshTasksIndirectCommandEXT
