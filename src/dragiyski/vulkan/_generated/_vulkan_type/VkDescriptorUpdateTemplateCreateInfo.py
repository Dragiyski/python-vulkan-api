import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorUpdateTemplateEntry import CType as VkDescriptorUpdateTemplateEntry

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('descriptorUpdateEntryCount', ctypes.c_uint32),
    ('pDescriptorUpdateEntries', ctypes.POINTER(VkDescriptorUpdateTemplateEntry)),
    ('templateType', ctypes.c_int),
    ('descriptorSetLayout', ctypes.c_void_p),
    ('pipelineBindPoint', ctypes.c_int),
    ('pipelineLayout', ctypes.c_void_p),
    ('set', ctypes.c_uint32),
]