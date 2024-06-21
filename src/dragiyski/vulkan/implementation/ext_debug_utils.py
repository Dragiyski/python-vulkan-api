import ctypes
from weakref import finalize

from .instance import VkInstance
from .. import binding
from .._util import create_handle_storage_meta
from ..error import VkException

from .instance import VkInstance

def _py_vkDebugUtilsMessengerCallbackEXT(
    message_severity: binding.vkDebugUtilsMessengerCallbackEXT._argtypes_[0],
    message_type: binding.vkDebugUtilsMessengerCallbackEXT._argtypes_[1],
    data: binding.vkDebugUtilsMessengerCallbackEXT._argtypes_[2],
    ptr_self: binding.vkDebugUtilsMessengerCallbackEXT._argtypes_[3]
):
    listener = ctypes.cast(ptr_self, ctypes.py_object).value
    listener: VkDebugUtilsMessengerListener
    listener.on_message(
        message_severity = message_severity,
        message_type = message_type,
        message = data.contents.pMessage.decode()
    )
    return binding.VK_FALSE

_c_vkDebugUtilsMessengerCallbackEXT = binding.vkDebugUtilsMessengerCallbackEXT(_py_vkDebugUtilsMessengerCallbackEXT)

class VkDebugUtilsMessengerListener:
    def on_message(
            self,
            *,
            message_severity,
            message_type,
            message
        ):
            print(message)
            pass

_handle_map = {}

def _destroy_handle(vkDestroyDebugUtilsMessengerEXT, instance, ptr_messenger, ptr_allocator):
    _handle_map.pop(ptr_messenger, None)
    print('vkDestroyDebugUtilsMessengerEXT(%r, %r, %r)' % (instance, ptr_messenger, ptr_allocator))
    vkDestroyDebugUtilsMessengerEXT(instance, ptr_messenger, ptr_allocator)

class VkDebugUtilsMessenger(binding.VkDebugUtilsMessengerEXT, metaclass=create_handle_storage_meta(binding.VkDebugUtilsMessengerEXT, _handle_map)):
    @classmethod
    def create(
        cls,
        instance: VkInstance | binding.VkInstance,
        listener: VkDebugUtilsMessengerListener,
        message_severity: binding.VkDebugUtilsMessageSeverityFlagsEXT | int = 0,
        message_types: binding.VkDebugUtilsMessageTypeFlagsEXT | int = 0,
    ):
        pyobject_listener = ctypes.py_object(listener)
        c_listener = ctypes.cast(ctypes.c_void_p(ctypes.addressof(pyobject_listener)), ctypes.POINTER(ctypes.c_void_p)).contents.value
        create_info = binding.VkDebugUtilsMessengerCreateInfoEXT(
            sType = binding.VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT,
            pNext = None,
            flags = 0,
            messageSeverity = message_severity,
            messageType = message_types,
            pfnUserCallback = _c_vkDebugUtilsMessengerCallbackEXT,
            pUserData = c_listener
        )
        loader = instance._loader_
        self = binding.VkDebugUtilsMessengerEXT.__new__(cls)
        VkException.check(loader.vkCreateDebugUtilsMessengerEXT(instance, ctypes.byref(create_info), None, ctypes.byref(self)))
        self._loader_ = loader
        self.__listener = listener
        self.__destroy = finalize(self, _destroy_handle, loader.vkDestroyDebugUtilsMessengerEXT, instance, self.value, None)
        return self
    
def vkSubmitDebugUtilsMessage(
    instance: VkInstance,
    message_severity: binding.VkDebugUtilsMessageSeverityFlagsEXT,
    message_types: binding.VkDebugUtilsMessageTypeFlagsEXT,
    message: str | bytes
):
    if isinstance(message, str):
        message = message.encode()
    callback_data = binding.VkDebugUtilsMessengerCallbackDataEXT(
        sType = binding.VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT,
        pNext = None,
        flags = 0,
        pMessageIdName = None,
        messageIdNumber = 0,
        pMessage = message,
        queueLabelCount = 0,
        pQueueLabels = None,
        cmdBufLabelCount = 0,
        pCmdBufLabels = None,
        objectCount = 0,
        pObjects = None
    )
    instance._loader_.vkSubmitDebugUtilsMessageEXT(instance, message_severity, message_types, ctypes.byref(callback_data))
