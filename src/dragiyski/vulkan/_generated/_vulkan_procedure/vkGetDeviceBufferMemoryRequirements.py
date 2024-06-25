import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDeviceBufferMemoryRequirements import VkDeviceBufferMemoryRequirements
from .._vulkan_type.VkMemoryRequirements2 import VkMemoryRequirements2

vkGetDeviceBufferMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceBufferMemoryRequirements), ctypes.POINTER(VkMemoryRequirements2))
