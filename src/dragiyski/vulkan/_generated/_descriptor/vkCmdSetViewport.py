from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetViewport'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstViewport', 'viewportCount', 'pViewports']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstViewport': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'viewportCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pViewports': {
        'type': CPointerType(CComplexType('VkViewport')),
        'is_string': False,
        'length': [['viewportCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
