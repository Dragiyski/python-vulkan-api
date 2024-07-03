from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdInsertDebugUtilsLabelEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pLabelInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pLabelInfo': {
        'type': CPointerType(CComplexType('VkDebugUtilsLabelEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
