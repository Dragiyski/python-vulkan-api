import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkShaderModuleCreateInfo import VkShaderModuleCreateInfo
from .._vulkan_type.VkShaderModuleIdentifierEXT import VkShaderModuleIdentifierEXT

vkGetShaderModuleCreateInfoIdentifierEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkShaderModuleCreateInfo), ctypes.POINTER(VkShaderModuleIdentifierEXT))
