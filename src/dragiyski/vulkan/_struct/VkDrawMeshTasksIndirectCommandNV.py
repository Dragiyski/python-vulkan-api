import ctypes, sys

class VkDrawMeshTasksIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('taskCount', ctypes.c_uint32),
        ('firstTask', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDrawMeshTasksIndirectCommandNV
