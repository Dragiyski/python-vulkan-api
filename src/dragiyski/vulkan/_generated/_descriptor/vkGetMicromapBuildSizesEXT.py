from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetMicromapBuildSizesEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'buildType', 'pBuildInfo', 'pSizeInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'buildType': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'pBuildInfo': {
        'type': CPointerType(CComplexType('VkMicromapBuildInfoEXT')),
        'is_string': False,
        'output': False,
    },
    'pSizeInfo': {
        'type': CPointerType(CComplexType('VkMicromapBuildSizesInfoEXT')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
