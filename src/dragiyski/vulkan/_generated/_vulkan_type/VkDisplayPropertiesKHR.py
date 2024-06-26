import ctypes

class VkDisplayPropertiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = {
        'VkDisplayProperties2KHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceDisplayPropertiesKHR',
    }
    _python_name_ = {
        'display': 'display',
        'displayName': 'display_name',
        'physicalDimensions': 'physical_dimensions',
        'physicalResolution': 'physical_resolution',
        'supportedTransforms': 'supported_transforms',
        'planeReorderPossible': 'plane_reorder_possible',
        'persistentContent': 'persistent_content',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_display',
    }
    _vk_enum_ = {
        'supportedTransforms': 'VkSurfaceTransformFlagsKHR',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkDisplayPropertiesKHR._fields_ = [
    ('display', ctypes.c_void_p),
    ('displayName', ctypes.c_char_p),
    ('physicalDimensions', VkExtent2D),
    ('physicalResolution', VkExtent2D),
    ('supportedTransforms', ctypes.c_uint32),
    ('planeReorderPossible', ctypes.c_uint32),
    ('persistentContent', ctypes.c_uint32),
]

VkDisplayPropertiesKHR._type_ = {
    'display': ctypes.c_void_p,
    'displayName': ctypes.c_char_p,
    'physicalDimensions': VkExtent2D,
    'physicalResolution': VkExtent2D,
    'supportedTransforms': ctypes.c_uint32,
    'planeReorderPossible': ctypes.c_uint32,
    'persistentContent': ctypes.c_uint32,
}
