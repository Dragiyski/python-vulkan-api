import ctypes

class VkPipelineCreationFeedback(ctypes.Structure):
    _fields_ = [
        ('flags', ctypes.c_uint32),
        ('duration', ctypes.c_uint64),
    ]

VkPipelineCreationFeedback._type_ = {
    'flags': ctypes.c_uint32,
    'duration': ctypes.c_uint64,
}
