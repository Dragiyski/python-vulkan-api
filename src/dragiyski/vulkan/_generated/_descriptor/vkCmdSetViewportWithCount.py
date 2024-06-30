from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetViewportWithCount'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'viewportCount', 'pViewports']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'viewportCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewports': {
        'type': CPointerType(CComplexType('VkViewport')),
        'is_string': False,
        'length': [['viewportCount']],
    },
}
_return_type_ = CVoidType()
