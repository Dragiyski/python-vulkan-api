import ctypes
from collections.abc import Collection
from .. import binding
from .._util import make_array_ptr_from_iterable, make_c_string_list

class VkInstanceCreateInfo(binding.VkInstanceCreateInfo):
    @classmethod
    def create(
        cls,
        *,
        application_info: 'VkApplicationInfo',
        layers: Collection[str | bytes] = (),
        extensions: Collection[str | bytes] = (),
        flags: binding.VkInstanceCreateFlags | int = 0,
    ) -> 'VkInstanceCreateInfo':
        self = cls()
        self.sType = binding.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO
        self.pNext = None
        self.flags = flags
        self.pApplicationInfo = ctypes.cast(ctypes.pointer(application_info), self._type_['pApplicationInfo'])
        self.enabledLayerCount = len(layers)
        self.ppEnabledLayerNames = make_array_ptr_from_iterable(ctypes.c_char_p, make_c_string_list(layers))
        self.enabledExtensionCount = len(extensions)
        self.ppEnabledExtensionNames = make_array_ptr_from_iterable(ctypes.c_char_p, make_c_string_list(extensions))
        return self

from .VkApplicationInfo import VkApplicationInfo