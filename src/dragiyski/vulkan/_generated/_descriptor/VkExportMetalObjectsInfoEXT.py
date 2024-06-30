from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExportMetalObjectsInfoEXT'
_member_list_ = ['sType', 'pNext']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXPORT_METAL_OBJECTS_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkExportMetalBufferInfoEXT',
    'VkExportMetalCommandQueueInfoEXT',
    'VkExportMetalDeviceInfoEXT',
    'VkExportMetalIOSurfaceInfoEXT',
    'VkExportMetalSharedEventInfoEXT',
    'VkExportMetalTextureInfoEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkExportMetalObjectsEXT',
}
