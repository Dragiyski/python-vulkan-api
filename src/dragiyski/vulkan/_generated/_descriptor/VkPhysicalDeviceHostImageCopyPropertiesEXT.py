from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceHostImageCopyPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'copySrcLayoutCount', 'pCopySrcLayouts', 'copyDstLayoutCount', 'pCopyDstLayouts', 'optimalTilingLayoutUUID', 'identicalMemoryTypeRequirements']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_IMAGE_COPY_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'copySrcLayoutCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCopySrcLayouts': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'length': [['copySrcLayoutCount']],
        'is_string': False,
    },
    'copyDstLayoutCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCopyDstLayouts': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'length': [['copyDstLayoutCount']],
        'is_string': False,
    },
    'optimalTilingLayoutUUID': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'identicalMemoryTypeRequirements': {
        'type': CIntType('c_uint32'),
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
