import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDispatchGraphCountInfoAMDX import VkDispatchGraphCountInfoAMDX

vkCmdDispatchGraphIndirectAMDX = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(VkDispatchGraphCountInfoAMDX))
