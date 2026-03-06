from abc import ABC, abstractmethod
from functools import partial
from typing import Callable
import ctypes.util


class _VulkanNotFoundError:
    pass


_vulkan_commands_ = {}
exec('from ._generated._vulkan_command import *', globals(), _vulkan_commands_)

_vulkan_callbacks_ = {}
exec('from ._generated._vulkan_callback import *', globals(), _vulkan_callbacks_)
_vulkan_callbacks_.pop('vkVoidFunction', None)
_vulkan_callbacks_.pop('vkGetInstanceProcAddrLUNARG', None)


class CommandAdapter(ABC):
    __slots__ = ('__dict__', '__weakref__')

    def __getattr__(self, name: str):
        if name.startswith('_'):
            raise AttributeError(name)
        try:
            value = self._get_implementation(name)
        except _VulkanNotFoundError:
            raise AttributeError(name)
        self.__dict__[name] = value
        return value

    def __getitem__(self, name: str):
        if name in self.__dict__:
            return self.__dict__[name]
        try:
            value = self._get_implementation(name)
        except _VulkanNotFoundError:
            raise KeyError(name)
        self.__dict__[name] = value
        return value

    def _get_implementation(self, name: str):
        if name in _vulkan_commands_:
            ptr = self._get_function_address(name)
            if ptr is None:
                raise _VulkanNotFoundError(
                    f'Function {name} is not implemented')
            return _vulkan_commands_[name](ptr)

    @abstractmethod
    def _get_function_address(self, name: str) -> int:
        pass


_SysDLL = ctypes.WinDLL if hasattr(ctypes, 'WinDLL') else ctypes.CDLL


def _default_library_loader():
    vulkan_name = ctypes.util.find_library('vulkan')
    if vulkan_name is None:
        raise RuntimeError('Unable to find vulkan library')
    vulkan = _SysDLL(vulkan_name)
    return ctypes.cast(vulkan.vkGetInstanceProcAddr, ctypes.c_void_p).value


class GlobalCommandAdapter(CommandAdapter):
    __slots__ = ('vkGetInstanceProcAddr')

    def __init__(self, vkGetInstanceProcAddr: Callable | int | None = None):
        super().__init__()
        if vkGetInstanceProcAddr is None:
            vkGetInstanceProcAddr = _default_library_loader()
        if isinstance(vkGetInstanceProcAddr, ctypes._CFuncPtr):
            vkGetInstanceProcAddr = ctypes.cast(
                vkGetInstanceProcAddr, ctypes.c_void_p).value
        if isinstance(vkGetInstanceProcAddr, int):
            from ._generated._vulkan_command import vkGetInstanceProcAddr as binding
            vkGetInstanceProcAddr = binding(vkGetInstanceProcAddr)
        self.vkGetInstanceProcAddr = vkGetInstanceProcAddr

    def _get_function_address(self, name):
        vk_ptr_result = self.vkGetInstanceProcAddr(None, name.encode())
        return ctypes.cast(vk_ptr_result, ctypes.c_void_p).value


class InstanceCommandAdapter(CommandAdapter):
    __slots__ = ('adapter', 'value')

    def __init__(self, adapter: GlobalCommandAdapter, instance: int):
        super().__init__()
        self.adapter = adapter
        self.value = instance

    def _get_function_address(self, name):
        vk_ptr_result = self.adapter.vkGetInstanceProcAddr(self.value, name.encode())
        return ctypes.cast(vk_ptr_result, ctypes.c_void_p).value


class DeviceCommandAdapter(CommandAdapter):
    __slots__ = ('adapter', 'value')

    def __init__(self, adapter: InstanceCommandAdapter, device: int):
        super().__init__()
        self.adapter = adapter
        self.value = device

    def _get_function_address(self, name):
        vk_ptr_result = self.adapter.vkGetDeviceProcAddr(self.value, name.encode())
        return ctypes.cast(vk_ptr_result, ctypes.c_void_p).value


class CallbackAdapter:
    __slots__ = ('__dict__', '__weakref__')
    _callback_map = {}

    def __getattr__(self, name: str):
        if name.startswith('_'):
            raise AttributeError(name)
        try:
            value = self._get_implementation(name)
        except _VulkanNotFoundError:
            raise AttributeError(name)
        self.__dict__[name] = value
        return value

    def __getitem__(self, name: str):
        if name in self.__dict__:
            return self.__dict__[name]
        try:
            value = self._get_implementation(name)
        except _VulkanNotFoundError:
            raise KeyError(name)
        self.__dict__[name] = value
        return value

    def _get_implementation(self, name: str):
        if name not in self._callback_map:
            if name not in _vulkan_callbacks_:
                raise _VulkanNotFoundError(f'Callback {name} does not exist')
            ctype = _vulkan_callbacks_[name]
            if 'pUserData' not in ctype._vulkan_ctype_arguments_:
                raise _VulkanNotFoundError(f'Callback {name} does not have pUserData argument')
            user_data_index = list(ctype._vulkan_ctype_arguments_.keys()).index('pUserData')
            self._callback_map[name] = _unwrap_callback_factory(ctype, user_data_index)
        return partial(_wrap_callback, self._callback_map[name])


def _unwrap_callback_factory(ctype, callback_index):
    def _unwrap_callback(*args):
        nonlocal ctype
        ptr_callback = ctypes.cast(args[callback_index], ctypes.POINTER(ctypes.py_object))
        arguments = args[:callback_index] + args[callback_index+1:]
        return ptr_callback.contents.value(*arguments)

    return ctype(_unwrap_callback)


def _wrap_callback(wrapped_callback, callback: Callable):
    if not callable(callback):
        raise ValueError('Callback must be callable')
    ptr_callback = ctypes.pointer(ctypes.py_object(callback))
    return wrapped_callback, ctypes.cast(ptr_callback, ctypes.c_void_p)
