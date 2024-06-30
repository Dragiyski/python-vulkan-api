from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceImageDrmFormatModifierInfoEXT'
_member_list_ = ['sType', 'pNext', 'drmFormatModifier', 'sharingMode', 'queueFamilyIndexCount', 'pQueueFamilyIndices']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_DRM_FORMAT_MODIFIER_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'drmFormatModifier': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'sharingMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkSharingMode',
        'enum': 'VkSharingMode',
        'is_string': False,
    },
    'queueFamilyIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pQueueFamilyIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['queueFamilyIndexCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceImageFormatInfo2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
