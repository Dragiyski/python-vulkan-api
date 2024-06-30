from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImagePlaneMemoryRequirementsInfo'
_member_list_ = ['sType', 'pNext', 'planeAspect']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_PLANE_MEMORY_REQUIREMENTS_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'planeAspect': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageAspectFlagBits',
        'is_string': False,
    },
}
_extends_ = {
    'VkImageMemoryRequirementsInfo2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
