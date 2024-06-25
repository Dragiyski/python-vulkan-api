import ctypes

class VkPushDescriptorSetWithTemplateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorUpdateTemplate', ctypes.c_void_p),
        ('layout', ctypes.c_void_p),
        ('set', ctypes.c_uint32),
        ('pData', ctypes.c_void_p),
    ]

VkPushDescriptorSetWithTemplateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'descriptorUpdateTemplate': ctypes.c_void_p,
    'layout': ctypes.c_void_p,
    'set': ctypes.c_uint32,
    'pData': ctypes.c_void_p,
}
