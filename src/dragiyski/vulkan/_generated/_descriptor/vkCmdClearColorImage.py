from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdClearColorImage'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'image', 'imageLayout', 'pColor', 'rangeCount', 'pRanges']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageLayout': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'pColor': {
        'type': CPointerType(CComplexType('VkClearColorValue')),
        'is_string': False,
    },
    'rangeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pRanges': {
        'type': CPointerType(CComplexType('VkImageSubresourceRange')),
        'is_string': False,
        'length': [['rangeCount']],
    },
}
_return_type_ = CVoidType()
