from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageMemoryRequirementsInfo2'
_member_list_ = ['sType', 'pNext', 'image']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_MEMORY_REQUIREMENTS_INFO_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkImagePlaneMemoryRequirementsInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetImageMemoryRequirements2',
}
_output_of_ = set()
