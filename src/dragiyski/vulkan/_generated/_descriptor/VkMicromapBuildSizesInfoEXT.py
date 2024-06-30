from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMicromapBuildSizesInfoEXT'
_member_list_ = ['sType', 'pNext', 'micromapSize', 'buildScratchSize', 'discardable']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MICROMAP_BUILD_SIZES_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'micromapSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'buildScratchSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'discardable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetMicromapBuildSizesEXT',
}
