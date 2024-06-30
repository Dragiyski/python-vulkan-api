from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFrameBoundaryEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'frameID', 'imageCount', 'pImages', 'bufferCount', 'pBuffers', 'tagName', 'tagSize', 'pTag']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_FRAME_BOUNDARY_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFrameBoundaryFlagsEXT',
        'enum': 'VkFrameBoundaryFlagsEXT',
        'is_string': False,
    },
    'frameID': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'imageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pImages': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['imageCount']],
        'is_string': False,
    },
    'bufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBuffers': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['bufferCount']],
        'is_string': False,
    },
    'tagName': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'tagSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pTag': {
        'type': CIntType('c_void_p'),
        'length': [['tagSize']],
        'is_string': False,
    },
}
_extends_ = {
    'VkBindSparseInfo',
    'VkPresentInfoKHR',
    'VkSubmitInfo',
    'VkSubmitInfo2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
