import ctypes
from ..vulkan_base import VKAPI_PTR

from .vkVoidFunction import vkVoidFunction

vkGetInstanceProcAddrLUNARG = VKAPI_PTR(vkVoidFunction, ctypes.c_void_p, ctypes.c_char_p)
