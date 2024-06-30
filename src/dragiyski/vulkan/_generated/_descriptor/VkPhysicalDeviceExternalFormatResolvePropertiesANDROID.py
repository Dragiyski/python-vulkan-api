from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceExternalFormatResolvePropertiesANDROID'
_member_list_ = ['sType', 'pNext', 'nullColorAttachmentWithExternalFormatResolve', 'externalFormatResolveChromaOffsetX', 'externalFormatResolveChromaOffsetY']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FORMAT_RESOLVE_PROPERTIES_ANDROID',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'nullColorAttachmentWithExternalFormatResolve': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'externalFormatResolveChromaOffsetX': {
        'type': CIntType('c_int'),
        'type_name': 'VkChromaLocation',
        'enum': 'VkChromaLocation',
        'is_string': False,
    },
    'externalFormatResolveChromaOffsetY': {
        'type': CIntType('c_int'),
        'type_name': 'VkChromaLocation',
        'enum': 'VkChromaLocation',
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
