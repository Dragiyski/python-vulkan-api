from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAccelerationStructureCaptureDescriptorDataInfoEXT'
_member_list_ = ['sType', 'pNext', 'accelerationStructure', 'accelerationStructureNV']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CAPTURE_DESCRIPTOR_DATA_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'accelerationStructure': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'accelerationStructureNV': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetAccelerationStructureOpaqueCaptureDescriptorDataEXT',
}
_output_of_ = set()
