import ctypes
from collections.abc import Collection, Iterable
from ..loader import DriverLoader
from ..error import *
from .. import binding
from ..version import VkVersion, VkApiVersion
from .VkLayer import VkLayer
from .VkExtension import VkExtension

from functools import cached_property

def _enumerate_instance_layer_properties(app):
    vkEnumerateInstanceLayerProperties = app._loader_.vkEnumerateInstanceLayerProperties
    length = vkEnumerateInstanceLayerProperties.argtypes[0]._type_(0)
    try:
        VkException.check(vkEnumerateInstanceLayerProperties(ctypes.byref(length), None))
    except VkIncomplete:
        pass
    c_array = []
    while length.value > 0:
        last_value = length.value
        c_array = (vkEnumerateInstanceLayerProperties.argtypes[1]._type_ * length.value)()
        c_ptr = ctypes.cast(c_array, vkEnumerateInstanceLayerProperties.argtypes[1])
        try:
            VkException.check(vkEnumerateInstanceLayerProperties(ctypes.byref(length), c_ptr))
        except VkIncomplete:
            continue
        if length.value > last_value:
            continue
        break
    return ((c_array[i], _enumerate_instance_extension_properties(app, c_array[i].layerName)) for i in range(length.value))

def _enumerate_instance_extension_properties(app, layer = None):
    if layer is not None:
        if isinstance(layer, str):
                layer = layer.encode()
    vkEnumerateInstanceExtensionProperties = app._loader_.vkEnumerateInstanceExtensionProperties
    length = vkEnumerateInstanceExtensionProperties.argtypes[1]._type_(0)
    try:
        VkException.check(vkEnumerateInstanceExtensionProperties(layer, ctypes.byref(length), None))
    except VkIncomplete:
        pass
    c_array = []
    while length.value > 0:
        last_value = length.value
        c_array = (vkEnumerateInstanceExtensionProperties.argtypes[2]._type_ * length.value)()
        c_ptr = ctypes.cast(c_array, vkEnumerateInstanceExtensionProperties.argtypes[2])
        try:
            VkException.check(vkEnumerateInstanceExtensionProperties(layer, ctypes.byref(length), c_ptr))
        except VkIncomplete:
            continue
        if length.value > last_value:
            continue
        break
    return (c_array[i] for i in range(length.value))

class VkApplication:
    def __init__(self, loader: DriverLoader = DriverLoader()):
        self._loader_ = loader

    @cached_property
    def version(self):
        version = self._loader_.vkEnumerateInstanceVersion.argtypes[0]._type_()
        VkException.check(self._loader_.vkEnumerateInstanceVersion(ctypes.byref(version)))
        return VkApiVersion(version.value)
    
    @cached_property
    def layers(self):
        return frozenset(VkLayer(properties, extensions = frozenset(VkExtension(extension) for extension in extensions)) for properties, extensions in _enumerate_instance_layer_properties(self))
    
    @cached_property
    def extensions(self):
        return frozenset(VkExtension(properties) for properties in _enumerate_instance_extension_properties(self))
    
    def make_layer_extension_properties(
        self,
        required_layers: Iterable[str] = (),
        optional_layers: Iterable[str] = (),
        required_extensions: Iterable[str] = (),
        optional_extensions: Iterable[str] = (),
    ):
        enabled_layers = set(required_layers).union(set(optional_layers).intersection(self.layers))
        available_extensions = self.extensions
        for layer in self.layers:
            if layer in enabled_layers:
                available_extensions = available_extensions.union(layer.extensions)
        enabled_extensions = set(required_extensions).union(set(optional_extensions).intersection(available_extensions))
        return enabled_layers, enabled_extensions
