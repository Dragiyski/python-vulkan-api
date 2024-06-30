import ctypes
from collections.abc import Collection
from ... import binding
from ..._pointer import finalize, PointerStorageType
from ...error import *

class VkDebugUtilsLabel(str):
    def __new__(cls, value, *, color = [0.0, 0.0, 0.0, 0.0]):
        self = super().__new__(value)
        self.color = color

class VkDebugUtilsMessengerCallback:
    def on_message(
        self,
        /,
        message_severity: binding.VkDebugUtilsMessageSeverityFlagsEXT,
        message_type: binding.VkDebugUtilsMessageTypeFlagsEXT,
        message: str,
        *,
        message_id: int = 0,
        message_name: str = '',
        queue_labels: Collection[VkDebugUtilsLabel] = (),
        command_buffer_labels: Collection[VkDebugUtilsLabel] = (),
        objects: Collection = ()
    ):
        pass


def _destroy_handle(vkDestroyDebugUtilsMessengerEXT, *args):
    print('vkDestroyDebugUtilsMessengerEXT(0x%016x)' % args[1])
    vkDestroyDebugUtilsMessengerEXT(*args)

def _callback(message_severity, message_type, ptr_callback_data, ptr_user_data):
    pass

_ptr_callback = binding.vkDebugUtilsMessengerCallbackEXT(_callback)

class VkDebugUtilsMessenger(metaclass = PointerStorageType):
    def __init__(self, instance, callback):
        self._loader_ = instance._loader_
        self.instance = instance
        self.callback = callback
        finalize(self._as_parameter_, self, _destroy_handle, self._loader_.vkDestroyDebugUtilsMessengerEXT, instance, self._as_parameter_, None)
    
    @classmethod
    def create(
        cls,
        /,
        instance,
        callback: VkDebugUtilsMessengerCallback,
        *,
        message_severity: binding.VkDebugUtilsMessageSeverityFlagsEXT,
        message_type: binding.VkDebugUtilsMessageTypeFlagsEXT,
        flags = 0,
    ):
        try:
            vkCreateDebugUtilsMessengerEXT = instance._loader_.vkCreateDebugUtilsMessengerEXT
        except AttributeError:
            raise NotImplementedError('vkCreateDebugUtilsMessengerEXT')
        py_callback = ctypes.py_object(callback)
        c_callback = ctypes.cast(ctypes.c_void_p(ctypes.addressof(py_callback)), ctypes.POINTER(ctypes.c_void_p)).contents.value
        create_info = binding.VkDebugUtilsMessengerCreateInfoEXT()
        create_info.flags = flags
        create_info.messageSeverity = message_severity
        create_info.messageType = message_type
        create_info.pfnUserCallback = _ptr_callback
        create_info.pUserData = c_callback

        handle = binding.VkDebugUtilsMessengerEXT()
        VkException.check(vkCreateDebugUtilsMessengerEXT(instance, ctypes.byref(create_info), None, ctypes.byref(handle)))
        return cls(handle.value, instance, callback)
