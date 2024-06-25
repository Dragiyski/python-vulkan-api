from typing import List
from collections.abc import Callable
from .. import binding
from ..version import VkVersion, VkApiVersion

class Loader:
    vkGetInstanceProcAddr: binding.vkGetInstanceProcAddr
    vkEnumerateInstanceVersion: binding.vkEnumerateInstanceVersion
    vkEnumerateInstanceLayerProperties: binding.vkEnumerateInstanceLayerProperties
    vkEnumerateInstanceExtensionProperties: binding.vkEnumerateInstanceExtensionProperties
    vkCreateInstance: binding.vkCreateInstance

class VkLayer(str):
    spec_version: VkApiVersion
    implementation_version: VkApiVersion
    description: str

class VkExtension(str):
    spec_version: VkApiVersion

class VkGlobal:
    _loader_: Loader
    def enumerate_instance_version(self, *, use_api_version: bool = True) -> VkVersion|VkApiVersion: ...
    def enumerate_instance_layer_properties(self) -> List[VkLayer]: ...
    def enumerate_instance_extension_properties(self, layer: VkLayer|str|bytes|None) -> List[VkExtension]: ...
