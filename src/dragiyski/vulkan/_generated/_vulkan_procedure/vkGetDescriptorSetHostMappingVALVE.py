import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetDescriptorSetHostMappingVALVE = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
