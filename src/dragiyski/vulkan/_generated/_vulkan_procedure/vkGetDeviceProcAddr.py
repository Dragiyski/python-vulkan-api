import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_callback.vkVoidFunction import vkVoidFunction

vkGetDeviceProcAddr = VKAPI_CALL(vkVoidFunction, ctypes.c_void_p, ctypes.c_char_p)
