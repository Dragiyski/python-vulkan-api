from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSurfaceFormat2KHR'
_member_list_ = ['sType', 'pNext', 'surfaceFormat']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SURFACE_FORMAT_2_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'surfaceFormat': {
        'type': CComplexType('VkSurfaceFormatKHR'),
        'type_name': 'VkSurfaceFormatKHR',
        'structure': 'VkSurfaceFormatKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkImageCompressionPropertiesEXT',
}
_includes_ = {
    'VkSurfaceFormatKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceSurfaceFormats2KHR',
}
