from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkWriteDescriptorSetInlineUniformBlock'
_member_list_ = ['sType', 'pNext', 'dataSize', 'pData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_INLINE_UNIFORM_BLOCK',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dataSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'length': [['dataSize']],
        'is_string': False,
    },
}
_extends_ = {
    'VkWriteDescriptorSet',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
