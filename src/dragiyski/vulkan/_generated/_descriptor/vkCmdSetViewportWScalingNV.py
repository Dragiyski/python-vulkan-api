from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetViewportWScalingNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstViewport', 'viewportCount', 'pViewportWScalings']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstViewport': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'viewportCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewportWScalings': {
        'type': CPointerType(CComplexType('VkViewportWScalingNV')),
        'is_string': False,
        'length': [['viewportCount']],
    },
}
_return_type_ = CVoidType()
