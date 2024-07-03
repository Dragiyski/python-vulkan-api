from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdWriteMicromapsPropertiesEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'micromapCount', 'pMicromaps', 'queryType', 'queryPool', 'firstQuery']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'micromapCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pMicromaps': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['micromapCount']],
        'output': False,
    },
    'queryType': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
