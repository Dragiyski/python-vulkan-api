from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdPushDescriptorSetWithTemplateKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'descriptorUpdateTemplate', 'layout', 'set', 'pData']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'descriptorUpdateTemplate': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'set': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
