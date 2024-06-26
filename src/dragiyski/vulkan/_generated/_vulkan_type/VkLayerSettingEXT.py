import ctypes

class VkLayerSettingEXT(ctypes.Structure):
    _fields_ = [
        ('pLayerName', ctypes.c_char_p),
        ('pSettingName', ctypes.c_char_p),
        ('type', ctypes.c_int),
        ('valueCount', ctypes.c_uint32),
        ('pValues', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkLayerSettingsCreateInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'pLayerName': 'layer_name',
        'pSettingName': 'setting_name',
        'type': 'type',
        'valueCount': 'value_count',
        'pValues': 'values',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_layer_settings',
    }
    _vk_enum_ = {
        'type': 'VkLayerSettingTypeEXT',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkLayerSettingEXT._type_ = {
    'pLayerName': ctypes.c_char_p,
    'pSettingName': ctypes.c_char_p,
    'type': ctypes.c_int,
    'valueCount': ctypes.c_uint32,
    'pValues': ctypes.c_void_p,
}
