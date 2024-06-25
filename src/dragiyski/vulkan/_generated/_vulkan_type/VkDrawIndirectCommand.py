import ctypes

class VkDrawIndirectCommand(ctypes.Structure):
    _fields_ = [
        ('vertexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('firstInstance', ctypes.c_uint32),
    ]

VkDrawIndirectCommand._type_ = {
    'vertexCount': ctypes.c_uint32,
    'instanceCount': ctypes.c_uint32,
    'firstVertex': ctypes.c_uint32,
    'firstInstance': ctypes.c_uint32,
}
