from abc import ABC, abstractmethod
from typing import Callable, Mapping, Sequence
import ctypes.util

from numpy.strings import index


class ValueAdapter:
    def __init__(self):
        exec('from ._generated._vulkan_enum import *', globals(), self.__dict__)
        exec('from ._generated._vulkan_value import *', globals(), self.__dict__)
        exec('from ._generated._vulkan_type import *', globals(), self.__dict__)
        exec('from ._generated._vulkan_handle import *', globals(), self.__dict__)


class _VulkanNotFoundError:
    pass


_vulkan_commands_ = {}
exec('from ._generated._vulkan_command import *', globals(), _vulkan_commands_)

_vulkan_callbacks_ = {}
exec('from ._generated._vulkan_callback import *', globals(), _vulkan_callbacks_)
_vulkan_callbacks_.pop('vkVoidFunction', None)
_vulkan_callbacks_.pop('vkGetInstanceProcAddrLUNARG', None)


class CommandAdapter:
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

    class VulkanCallback:
        __slots__ = ('binding', 'value', '_args_', '_kwargs_')

        def __init__(self, binding: 'CallbackAdapter.VulkanCallbackBinding', callback: Callable, args: Sequence | None = None, kwargs: Mapping | None = None):
            if not callable(callback):
                raise ValueError('Callback must be callable')

            self.value = callback
            self.binding = binding
            keys = list(binding.ctype._vulkan_ctype_arguments_.keys())
            self._args_ = [keys.index(name) for name in args]
            self._kwargs_ = {k: keys.index(v) for k, v in kwargs.items()} if kwargs is not None else {}

            if len(self._args_) != len(set(self._args_)):
                raise ValueError(f'Arguments in args for callback {binding.name} must be unique')

            if kwargs is not None:
                if len(set(self._kwargs_.values())) != len(kwargs):
                    raise ValueError(f'Arguments in kwargs for callback {binding.name} must be unique')
                if len(args) + len(kwargs) != len(set(self._args_) | set(self._kwargs_.values())):
                    raise ValueError(f'Arguments in args and kwargs for callback {binding.name} must be unique')

        def as_user_data(self) -> ctypes.c_void_p:
            return ctypes.cast(ctypes.pointer(ctypes.py_object(self)), ctypes.c_void_p)

    class VulkanCallbackBinding:
        __slots__ = ('name', 'ctype', 'value', '_index_')

        def __init__(self, name: str, ctype: type[ctypes._CFuncPtr]):
            self.name = name
            self.ctype = ctype
            self.value = ctype(self.invoke)
            self._index_ = list(ctype._vulkan_ctype_arguments_.keys()).index('pUserData')

        def invoke(self, *args, **kwargs):
            callback = ctypes.cast(args[self._index_], ctypes.POINTER(ctypes.py_object)).contents.value
            callback: CallbackAdapter.VulkanCallback
            invoke_args = [args[i] for i in callback._args_]
            invoke_kwargs = {k: args[v] for k, v in callback._kwargs_.items()}
            if self.ctype._vulkan_ctype_return_ is not None:
                return callback.value(*invoke_args, **invoke_kwargs)
            callback.value(*invoke_args, **invoke_kwargs)

        def __call__(self, callback: Callable, /, *args, **kwargs):
            return CallbackAdapter.VulkanCallback(self, callback, args, kwargs)

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
        ctype = _vulkan_callbacks_.get(name, None)
        if ctype is None:
            raise _VulkanNotFoundError(f'Callback {name} does not exist')
        if 'pUserData' not in ctype._vulkan_ctype_arguments_:
            raise _VulkanNotFoundError(f'Callback {name} is not a user data callback')
        if name not in self._callback_map:
            self._callback_map[name] = self.VulkanCallbackBinding(name, ctype)
        return self._callback_map[name]


class VulkanAdapter:
    def __init__(
        self,
        *,
        value: ValueAdapter | None = None,
        callback: CallbackAdapter | None = None,
        base: GlobalCommandAdapter | None = None,
        instance: InstanceCommandAdapter | None = None,
        device: DeviceCommandAdapter | None = None,
    ):
        self.value = value or ValueAdapter()
        self.callback = callback or CallbackAdapter()
        self.base = base or GlobalCommandAdapter()
        self.instance = instance
        self.device = device
