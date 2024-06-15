import ctypes, sys

class VkLayerSettingsCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkLayerSettingsCreateInfoEXT

from . import VkLayerSettingEXT

VkLayerSettingsCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('settingCount', ctypes.c_uint32),
    ('pSettings', ctypes.POINTER(VkLayerSettingEXT)),
]
