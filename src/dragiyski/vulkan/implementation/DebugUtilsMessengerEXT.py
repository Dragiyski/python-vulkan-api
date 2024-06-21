import ctypes
import sys
from functools import reduce
from operator import or_ as operator_or
from weakref import finalize

from .. import binding
from ..error import *


def _debug_utils_messenger_callback_impl(message_severity, message_type, data, self):
    print('test')
    return 0


_debug_utils_messenger_callback = binding.vkDebugUtilsMessengerCallbackEXT(_debug_utils_messenger_callback_impl)


def _destroy_utils_messenger(vkDestroyDebugUtilsMessengerEXT, instance, handle):
    vkDestroyDebugUtilsMessengerEXT(instance, handle, None)


class DebugUtilsMessengerEXT:
    def __init__(
        self,
        instance,
        loader,
        *,
        message_severity: binding.VkDebugUtilsMessageSeverityFlagsEXT = reduce(operator_or, binding.VkDebugUtilsMessageSeverityFlagsEXT),
        message_type: binding.VkDebugUtilsMessageTypeFlagsEXT = reduce(operator_or, binding.VkDebugUtilsMessageTypeFlagsEXT)
    ):
        if not hasattr(loader, 'vkCreateDebugUtilsMessengerEXT'):
            raise NotImplementedError('Extension VK_EXT_debug_utils is not supported and/or not enabled.')
        create_info = binding.VkDebugUtilsMessengerCreateInfoEXT(
            sType = binding.VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT,
            pNext = None,
            flags = 0,
            messageSeverity = message_severity,
            messageType = message_type,
            pfnUserCallback = ctypes.pointer(_debug_utils_messenger_callback),
            pUserData = ctypes.cast(id(self), ctypes.c_void_p)
        )
        handle = loader.vkCreateDebugUtilsMessengerEXT.argtypes[3]._type_()
        status_check(loader.vkCreateDebugUtilsMessengerEXT(instance, ctypes.byref(create_info), None, ctypes.byref(handle)))
        self.__handle = handle
        self.__loader = loader
        self.instance = instance
        self.__destroy = finalize(self, _destroy_utils_messenger, loader.vkDestroyDebugUtilsMessengerEXT, instance._as_parameter_, handle)

    @property
    def alive(self):
        return self.__destroy.alive

    def destroy(self):
        self.__destroy()


sys.modules[__name__] = DebugUtilsMessengerEXT
