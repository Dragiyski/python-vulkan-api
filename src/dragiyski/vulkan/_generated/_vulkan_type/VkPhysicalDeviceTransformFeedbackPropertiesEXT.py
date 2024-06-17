import ctypes, sys

class VkPhysicalDeviceTransformFeedbackPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxTransformFeedbackStreams', ctypes.c_uint32),
        ('maxTransformFeedbackBuffers', ctypes.c_uint32),
        ('maxTransformFeedbackBufferSize', ctypes.c_uint64),
        ('maxTransformFeedbackStreamDataSize', ctypes.c_uint32),
        ('maxTransformFeedbackBufferDataSize', ctypes.c_uint32),
        ('maxTransformFeedbackBufferDataStride', ctypes.c_uint32),
        ('transformFeedbackQueries', ctypes.c_uint32),
        ('transformFeedbackStreamsLinesTriangles', ctypes.c_uint32),
        ('transformFeedbackRasterizationStreamSelect', ctypes.c_uint32),
        ('transformFeedbackDraw', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceTransformFeedbackPropertiesEXT
