from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBuildMicromapsEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'infoCount', 'pInfos']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'infoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pInfos': {
        'type': CPointerType(CComplexType('VkMicromapBuildInfoEXT')),
        'is_string': False,
        'length': [['infoCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
