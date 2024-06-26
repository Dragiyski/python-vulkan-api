import ctypes
from collections.abc import Collection
from ..loader import LibraryLoader
from ..error import *
from .. import binding
from ..version import VkVersion, VkApiVersion


class VkLayer(str):
    def __new__(cls, value: binding.VkLayerProperties):
        self = super().__new__(cls, value.layerName.decode())
        self.spec_version = VkApiVersion(value.specVersion)
        self.implementation_version = VkApiVersion(value.implementationVersion)
        self.description = value.description.decode()
        return self


class VkExtension(str):
    def __new__(cls, value: binding.VkExtensionProperties):
        self = super().__new__(cls, value.extensionName.decode())
        self.spec_version = VkApiVersion(value.specVersion)
        return self


class Application:
    def __init__(self, loader: LibraryLoader = LibraryLoader()):
        self._loader_ = loader

    def enumerate_instance_version(self, *, use_api_version = True) -> VkVersion | VkApiVersion:
        version = self._loader_.vkEnumerateInstanceVersion.argtypes[0]._type_()
        VkException.check(self._loader_.vkEnumerateInstanceVersion(ctypes.byref(version)))
        return (VkApiVersion if use_api_version else VkVersion)(version.value)

    def enumerate_instance_layer_properties(self) -> Collection[VkLayer]:
        vkEnumerateInstanceLayerProperties = self._loader_.vkEnumerateInstanceLayerProperties
        length = vkEnumerateInstanceLayerProperties.argtypes[0]._type_(0)
        try:
            VkException.check(vkEnumerateInstanceLayerProperties(ctypes.byref(length), None))
        except VkIncomplete:
            pass
        c_array = []
        while length.value > 0:
            c_array = (vkEnumerateInstanceLayerProperties.argtypes[1]._type_ * length.value)()
            c_ptr = ctypes.cast(c_array, vkEnumerateInstanceLayerProperties.argtypes[1])
            try:
                VkException.check(vkEnumerateInstanceLayerProperties(ctypes.byref(length), c_ptr))
            except VkIncomplete:
                continue
            break
        return list(VkLayer(c_array[i]) for i in range(length.value))

    def enumerate_instance_extension_properties(self, layer: str | bytes = None) -> Collection[VkExtension]:
        if layer is not None:
            if isinstance(layer, str):
                layer = layer.encode()
        vkEnumerateInstanceExtensionProperties = self._loader_.vkEnumerateInstanceExtensionProperties
        length = vkEnumerateInstanceExtensionProperties.argtypes[1]._type_(0)
        try:
            VkException.check(vkEnumerateInstanceExtensionProperties(layer, ctypes.byref(length), None))
        except VkIncomplete:
            pass
        c_array = []
        while length.value > 0:
            c_array = (vkEnumerateInstanceExtensionProperties.argtypes[2]._type_ * length.value)()
            c_ptr = ctypes.cast(c_array, vkEnumerateInstanceExtensionProperties.argtypes[2])
            try:
                VkException.check(vkEnumerateInstanceExtensionProperties(layer, ctypes.byref(length), c_ptr))
            except VkIncomplete:
                continue
            break
        return list(VkExtension(c_array[i]) for i in range(length.value))
