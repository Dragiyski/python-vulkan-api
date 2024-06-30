from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceSurfaceInfo2KHR'
_member_list_ = ['sType', 'pNext', 'surface']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SURFACE_INFO_2_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'surface': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkSurfaceFullScreenExclusiveInfoEXT',
    'VkSurfaceFullScreenExclusiveWin32InfoEXT',
    'VkSurfacePresentModeEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetDeviceGroupSurfacePresentModes2EXT',
    'vkGetPhysicalDeviceSurfaceCapabilities2KHR',
    'vkGetPhysicalDeviceSurfaceFormats2KHR',
    'vkGetPhysicalDeviceSurfacePresentModes2EXT',
}
_output_of_ = set()
