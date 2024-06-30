from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeRateControlInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'rateControlMode', 'layerCount', 'pLayers', 'virtualBufferSizeInMs', 'initialVirtualBufferSizeInMs']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeRateControlFlagsKHR',
        'enum': 'VkVideoEncodeRateControlFlagsKHR',
        'is_string': False,
    },
    'rateControlMode': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeRateControlModeFlagBitsKHR',
        'is_string': False,
    },
    'layerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pLayers': {
        'type': CPointerType(CComplexType('VkVideoEncodeRateControlLayerInfoKHR')),
        'type_name': 'VkVideoEncodeRateControlLayerInfoKHR',
        'structure': 'VkVideoEncodeRateControlLayerInfoKHR',
        'length': [['layerCount']],
        'is_string': False,
    },
    'virtualBufferSizeInMs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'initialVirtualBufferSizeInMs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoBeginCodingInfoKHR',
    'VkVideoCodingControlInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkVideoEncodeRateControlLayerInfoKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
