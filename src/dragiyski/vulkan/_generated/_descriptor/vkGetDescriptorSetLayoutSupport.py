from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDescriptorSetLayoutSupport'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pCreateInfo', 'pSupport']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkDescriptorSetLayoutCreateInfo')),
        'is_string': False,
    },
    'pSupport': {
        'type': CPointerType(CComplexType('VkDescriptorSetLayoutSupport')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
