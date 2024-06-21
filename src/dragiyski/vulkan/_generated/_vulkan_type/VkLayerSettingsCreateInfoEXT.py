import ctypes

class CType(ctypes.Structure):
    pass

from .VkLayerSettingEXT import CType as VkLayerSettingEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('settingCount', ctypes.c_uint32),
    ('pSettings', ctypes.POINTER(VkLayerSettingEXT)),
]
