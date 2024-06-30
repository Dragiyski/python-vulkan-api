from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCudaLaunchInfoNV'
_member_list_ = ['sType', 'pNext', 'function', 'gridDimX', 'gridDimY', 'gridDimZ', 'blockDimX', 'blockDimY', 'blockDimZ', 'sharedMemBytes', 'paramCount', 'pParams', 'extraCount', 'pExtras']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_CUDA_LAUNCH_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'function': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'gridDimX': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'gridDimY': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'gridDimZ': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'blockDimX': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'blockDimY': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'blockDimZ': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sharedMemBytes': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'paramCount': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pParams': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['paramCount']],
        'is_string': False,
    },
    'extraCount': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pExtras': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['extraCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdCudaLaunchKernelNV',
}
_output_of_ = set()
