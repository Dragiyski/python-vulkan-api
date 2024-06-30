from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetDiscardRectangleEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstDiscardRectangle', 'discardRectangleCount', 'pDiscardRectangles']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstDiscardRectangle': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'discardRectangleCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDiscardRectangles': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'is_string': False,
        'length': [['discardRectangleCount']],
    },
}
_return_type_ = CVoidType()
