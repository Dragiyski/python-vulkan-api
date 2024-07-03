from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetTessellationDomainOriginEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'domainOrigin']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'domainOrigin': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
