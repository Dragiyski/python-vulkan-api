import ctypes

class VkLayerSettingsCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkInstanceCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkLayerSettingEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'settingCount': 'setting_count',
        'pSettings': 'settings',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_layer_settings',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_LAYER_SETTINGS_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_LAYER_SETTINGS_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkLayerSettingEXT import VkLayerSettingEXT

VkLayerSettingsCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('settingCount', ctypes.c_uint32),
    ('pSettings', ctypes.POINTER(VkLayerSettingEXT)),
]

VkLayerSettingsCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'settingCount': ctypes.c_uint32,
    'pSettings': ctypes.POINTER(VkLayerSettingEXT),
}
