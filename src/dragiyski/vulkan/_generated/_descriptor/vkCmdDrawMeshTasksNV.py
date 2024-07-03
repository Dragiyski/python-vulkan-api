from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDrawMeshTasksNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'taskCount', 'firstTask']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'taskCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'firstTask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
