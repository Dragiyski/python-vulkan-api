import ctypes

class CType(ctypes.Structure):
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

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxTransformFeedbackStreams': {'python_name': ['max', 'transform', 'feedback', 'streams']},
        'maxTransformFeedbackBuffers': {'python_name': ['max', 'transform', 'feedback', 'buffers']},
        'maxTransformFeedbackBufferSize': {'python_name': ['max', 'transform', 'feedback', 'buffer', 'size']},
        'maxTransformFeedbackStreamDataSize': {'python_name': ['max', 'transform', 'feedback', 'stream', 'data', 'size']},
        'maxTransformFeedbackBufferDataSize': {'python_name': ['max', 'transform', 'feedback', 'buffer', 'data', 'size']},
        'maxTransformFeedbackBufferDataStride': {'python_name': ['max', 'transform', 'feedback', 'buffer', 'data', 'stride']},
        'transformFeedbackQueries': {'python_name': ['transform', 'feedback', 'queries']},
        'transformFeedbackStreamsLinesTriangles': {'python_name': ['transform', 'feedback', 'streams', 'lines', 'triangles']},
        'transformFeedbackRasterizationStreamSelect': {'python_name': ['transform', 'feedback', 'rasterization', 'stream', 'select']},
        'transformFeedbackDraw': {'python_name': ['transform', 'feedback', 'draw']},
    }
}
