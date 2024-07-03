from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdClearColorImage'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'image', 'imageLayout', 'pColor', 'rangeCount', 'pRanges']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'imageLayout': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'pColor': {
        'type': CPointerType(CComplexType('VkClearColorValue')),
        'is_string': False,
        'output': False,
    },
    'rangeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pRanges': {
        'type': CPointerType(CComplexType('VkImageSubresourceRange')),
        'is_string': False,
        'length': [['rangeCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
