from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceTransformFeedbackPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'maxTransformFeedbackStreams', 'maxTransformFeedbackBuffers', 'maxTransformFeedbackBufferSize', 'maxTransformFeedbackStreamDataSize', 'maxTransformFeedbackBufferDataSize', 'maxTransformFeedbackBufferDataStride', 'transformFeedbackQueries', 'transformFeedbackStreamsLinesTriangles', 'transformFeedbackRasterizationStreamSelect', 'transformFeedbackDraw']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxTransformFeedbackStreams': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTransformFeedbackBuffers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTransformFeedbackBufferSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxTransformFeedbackStreamDataSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTransformFeedbackBufferDataSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTransformFeedbackBufferDataStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'transformFeedbackQueries': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'transformFeedbackStreamsLinesTriangles': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'transformFeedbackRasterizationStreamSelect': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'transformFeedbackDraw': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
