from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDescriptorSetLayoutSupport'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pCreateInfo', 'pSupport']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkDescriptorSetLayoutCreateInfo')),
        'is_string': False,
        'output': False,
    },
    'pSupport': {
        'type': CPointerType(CComplexType('VkDescriptorSetLayoutSupport')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
