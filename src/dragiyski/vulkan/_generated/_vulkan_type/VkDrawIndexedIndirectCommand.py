import ctypes, sys

class VkDrawIndexedIndirectCommand(ctypes.Structure):
    _fields_ = [
        ('indexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstIndex', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
        ('firstInstance', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDrawIndexedIndirectCommand
