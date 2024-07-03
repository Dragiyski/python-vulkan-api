from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkSetHdrMetadataEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchainCount', 'pSwapchains', 'pMetadata']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'swapchainCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pSwapchains': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['swapchainCount']],
        'output': False,
    },
    'pMetadata': {
        'type': CPointerType(CComplexType('VkHdrMetadataEXT')),
        'is_string': False,
        'length': [['swapchainCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
