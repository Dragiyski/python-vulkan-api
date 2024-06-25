import ctypes

class VkLayerSettingsCreateInfoEXT(ctypes.Structure):
    pass

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
