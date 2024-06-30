from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageCompressionPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'imageCompressionFlags', 'imageCompressionFixedRateFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageCompressionFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageCompressionFlagsEXT',
        'enum': 'VkImageCompressionFlagsEXT',
        'is_string': False,
    },
    'imageCompressionFixedRateFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageCompressionFixedRateFlagsEXT',
        'enum': 'VkImageCompressionFixedRateFlagsEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkImageFormatProperties2',
    'VkSubresourceLayout2KHR',
    'VkSurfaceFormat2KHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
