import ctypes, sys

class VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rasterizationOrderColorAttachmentAccess', ctypes.c_uint32),
        ('rasterizationOrderDepthAttachmentAccess', ctypes.c_uint32),
        ('rasterizationOrderStencilAttachmentAccess', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesEXT
