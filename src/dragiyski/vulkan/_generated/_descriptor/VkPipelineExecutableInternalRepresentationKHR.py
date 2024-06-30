from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineExecutableInternalRepresentationKHR'
_member_list_ = ['sType', 'pNext', 'name', 'description', 'isText', 'dataSize', 'pData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INTERNAL_REPRESENTATION_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'name': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'isText': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'length': [['dataSize']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPipelineExecutableInternalRepresentationsKHR',
}
