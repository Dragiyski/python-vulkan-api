from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdPushDescriptorSetWithTemplateKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'descriptorUpdateTemplate', 'layout', 'set', 'pData']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorUpdateTemplate': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'set': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
