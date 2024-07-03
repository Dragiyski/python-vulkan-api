from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetDiscardRectangleEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstDiscardRectangle', 'discardRectangleCount', 'pDiscardRectangles']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstDiscardRectangle': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'discardRectangleCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pDiscardRectangles': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'is_string': False,
        'length': [['discardRectangleCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
