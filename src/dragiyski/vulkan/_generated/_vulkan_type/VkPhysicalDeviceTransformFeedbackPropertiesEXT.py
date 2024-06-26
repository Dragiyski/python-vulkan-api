import ctypes

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

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxTransformFeedbackStreams': 'max_transform_feedback_streams',
        'maxTransformFeedbackBuffers': 'max_transform_feedback_buffers',
        'maxTransformFeedbackBufferSize': 'max_transform_feedback_buffer_size',
        'maxTransformFeedbackStreamDataSize': 'max_transform_feedback_stream_data_size',
        'maxTransformFeedbackBufferDataSize': 'max_transform_feedback_buffer_data_size',
        'maxTransformFeedbackBufferDataStride': 'max_transform_feedback_buffer_data_stride',
        'transformFeedbackQueries': 'transform_feedback_queries',
        'transformFeedbackStreamsLinesTriangles': 'transform_feedback_streams_lines_triangles',
        'transformFeedbackRasterizationStreamSelect': 'transform_feedback_rasterization_stream_select',
        'transformFeedbackDraw': 'transform_feedback_draw',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_transform_feedback',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceTransformFeedbackPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxTransformFeedbackStreams': ctypes.c_uint32,
    'maxTransformFeedbackBuffers': ctypes.c_uint32,
    'maxTransformFeedbackBufferSize': ctypes.c_uint64,
    'maxTransformFeedbackStreamDataSize': ctypes.c_uint32,
    'maxTransformFeedbackBufferDataSize': ctypes.c_uint32,
    'maxTransformFeedbackBufferDataStride': ctypes.c_uint32,
    'transformFeedbackQueries': ctypes.c_uint32,
    'transformFeedbackStreamsLinesTriangles': ctypes.c_uint32,
    'transformFeedbackRasterizationStreamSelect': ctypes.c_uint32,
    'transformFeedbackDraw': ctypes.c_uint32,
}
