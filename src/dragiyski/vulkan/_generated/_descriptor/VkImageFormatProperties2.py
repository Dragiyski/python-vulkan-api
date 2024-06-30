from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageFormatProperties2'
_member_list_ = ['sType', 'pNext', 'imageFormatProperties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageFormatProperties': {
        'type': CComplexType('VkImageFormatProperties'),
        'type_name': 'VkImageFormatProperties',
        'structure': 'VkImageFormatProperties',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkAndroidHardwareBufferUsageANDROID',
    'VkExternalImageFormatProperties',
    'VkFilterCubicImageViewImageFormatPropertiesEXT',
    'VkHostImageCopyDevicePerformanceQueryEXT',
    'VkImageCompressionPropertiesEXT',
    'VkSamplerYcbcrConversionImageFormatProperties',
    'VkTextureLODGatherFormatPropertiesAMD',
}
_includes_ = {
    'VkImageFormatProperties',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceImageFormatProperties2',
}
