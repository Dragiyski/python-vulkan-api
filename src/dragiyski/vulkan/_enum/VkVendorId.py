import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkVendorId(VulkanIntEnum):
    VK_VENDOR_ID_CODEPLAY = 65540
    VK_VENDOR_ID_KAZAN = 65539
    VK_VENDOR_ID_KHRONOS = 65536
    VK_VENDOR_ID_MESA = 65541
    VK_VENDOR_ID_MOBILEYE = 65543
    VK_VENDOR_ID_POCL = 65542
    VK_VENDOR_ID_VIV = 65537
    VK_VENDOR_ID_VSI = 65538

sys.modules[__name__] = VkVendorId

