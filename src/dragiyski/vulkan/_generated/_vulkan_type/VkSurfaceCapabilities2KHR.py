import ctypes

class CType(ctypes.Structure):
    pass

from .VkSurfaceCapabilitiesKHR import CType as VkSurfaceCapabilitiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceCapabilities', VkSurfaceCapabilitiesKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDisplayNativeHdrSurfaceCapabilitiesAMD',
        'VkLatencySurfaceCapabilitiesNV',
        'VkSharedPresentSurfaceCapabilitiesKHR',
        'VkSurfaceCapabilitiesFullScreenExclusiveEXT',
        'VkSurfaceCapabilitiesPresentBarrierNV',
        'VkSurfacePresentModeCompatibilityEXT',
        'VkSurfacePresentScalingCapabilitiesEXT',
        'VkSurfaceProtectedCapabilitiesKHR',
    },
    'includes': {
        'VkSurfaceCapabilitiesKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceSurfaceCapabilities2KHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'surfaceCapabilities': {'python_name': ['surface', 'capabilities'], 'type': 'VkSurfaceCapabilitiesKHR'},
    }
}
