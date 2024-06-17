import ctypes, sys

class VkPhysicalDeviceDynamicRenderingUnusedAttachmentsFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dynamicRenderingUnusedAttachments', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDynamicRenderingUnusedAttachmentsFeaturesEXT
