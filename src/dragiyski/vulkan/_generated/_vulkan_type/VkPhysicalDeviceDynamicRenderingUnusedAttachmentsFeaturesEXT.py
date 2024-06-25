import ctypes

class VkPhysicalDeviceDynamicRenderingUnusedAttachmentsFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dynamicRenderingUnusedAttachments', ctypes.c_uint32),
    ]

VkPhysicalDeviceDynamicRenderingUnusedAttachmentsFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'dynamicRenderingUnusedAttachments': ctypes.c_uint32,
}
