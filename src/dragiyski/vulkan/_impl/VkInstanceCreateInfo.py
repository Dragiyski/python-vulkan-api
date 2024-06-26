import ctypes
from collections.abc import Iterable
from .. import binding
from .._util import make_array_ptr_from_iterable, make_c_string_list


def init(
    self, *args,
    application_info: binding.VkApplicationInfo,
    layers: Iterable[str | bytes] = (),
    extensions: Iterable[str | bytes] = (),
    flags: binding.VkInstanceCreateFlags | int = 0
):
    layers = make_c_string_list(layers)
    extensions = make_c_string_list(extensions)
    self.enabledLayerCount = len(layers)
    self.enabledExtensionCount = len(extensions)
    self.ppEnabledLayerNames = make_array_ptr_from_iterable(ctypes.c_char_p, layers)
    self.ppEnabledExtensionNames = make_array_ptr_from_iterable(ctypes.c_char_p, extensions)
    self.pApplicationInfo = ctypes.pointer(application_info)
    self.flags = flags


binding.VkInstanceCreateInfo._init_.append(init)
