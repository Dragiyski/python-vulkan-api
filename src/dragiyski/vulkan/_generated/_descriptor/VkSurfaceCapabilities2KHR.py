from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSurfaceCapabilities2KHR'
_member_list_ = ['sType', 'pNext', 'surfaceCapabilities']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'surfaceCapabilities': {
        'type': CComplexType('VkSurfaceCapabilitiesKHR'),
        'type_name': 'VkSurfaceCapabilitiesKHR',
        'structure': 'VkSurfaceCapabilitiesKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDisplayNativeHdrSurfaceCapabilitiesAMD',
    'VkLatencySurfaceCapabilitiesNV',
    'VkSharedPresentSurfaceCapabilitiesKHR',
    'VkSurfaceCapabilitiesFullScreenExclusiveEXT',
    'VkSurfaceCapabilitiesPresentBarrierNV',
    'VkSurfacePresentModeCompatibilityEXT',
    'VkSurfacePresentScalingCapabilitiesEXT',
    'VkSurfaceProtectedCapabilitiesKHR',
}
_includes_ = {
    'VkSurfaceCapabilitiesKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceSurfaceCapabilities2KHR',
}
