from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDescriptorEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pDescriptorInfo', 'dataSize', 'pDescriptor']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDescriptorInfo': {
        'type': CPointerType(CComplexType('VkDescriptorGetInfoEXT')),
        'is_string': False,
    },
    'dataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pDescriptor': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['dataSize']],
    },
}
_return_type_ = CVoidType()
