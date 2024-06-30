from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBlitImage'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'srcImage', 'srcImageLayout', 'dstImage', 'dstImageLayout', 'regionCount', 'pRegions', 'filter']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcImage': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcImageLayout': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'dstImage': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dstImageLayout': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'regionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pRegions': {
        'type': CPointerType(CComplexType('VkImageBlit')),
        'is_string': False,
        'length': [['regionCount']],
    },
    'filter': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
