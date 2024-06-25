import ctypes

class VkBindPipelineIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('pipelineAddress', ctypes.c_uint64),
    ]

VkBindPipelineIndirectCommandNV._type_ = {
    'pipelineAddress': ctypes.c_uint64,
}
