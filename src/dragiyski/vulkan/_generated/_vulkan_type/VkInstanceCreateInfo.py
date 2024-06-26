import ctypes

class VkInstanceCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDebugReportCallbackCreateInfoEXT',
        'VkDebugUtilsMessengerCreateInfoEXT',
        'VkDirectDriverLoadingListLUNARG',
        'VkExportMetalObjectCreateInfoEXT',
        'VkLayerSettingsCreateInfoEXT',
        'VkValidationFeaturesEXT',
        'VkValidationFlagsEXT',
    }
    _includes_ = {
        'VkApplicationInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateInstance',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'pApplicationInfo': 'application_info',
        'enabledLayerCount': 'enabled_layer_count',
        'ppEnabledLayerNames': 'enabled_layer_names',
        'enabledExtensionCount': 'enabled_extension_count',
        'ppEnabledExtensionNames': 'enabled_extension_names',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkInstanceCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkApplicationInfo import VkApplicationInfo

VkInstanceCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pApplicationInfo', ctypes.POINTER(VkApplicationInfo)),
    ('enabledLayerCount', ctypes.c_uint32),
    ('ppEnabledLayerNames', ctypes.POINTER(ctypes.c_char_p)),
    ('enabledExtensionCount', ctypes.c_uint32),
    ('ppEnabledExtensionNames', ctypes.POINTER(ctypes.c_char_p)),
]

VkInstanceCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pApplicationInfo': ctypes.POINTER(VkApplicationInfo),
    'enabledLayerCount': ctypes.c_uint32,
    'ppEnabledLayerNames': ctypes.POINTER(ctypes.c_char_p),
    'enabledExtensionCount': ctypes.c_uint32,
    'ppEnabledExtensionNames': ctypes.POINTER(ctypes.c_char_p),
}
