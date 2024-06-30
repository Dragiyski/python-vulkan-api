from collections import Collection
from typing import Optional

from ..version import VkApiVersion
from ..loader import LibraryLoader

class Application:
    def enumerate_instance_version(self, *, use_api_version: bool = True) -> VkVersion | VkApiVersion: ...
    def enumerate_instance_layer_properties(self) -> Collection[VkLayer]: ...
    def enumerate_instance_extension_properties(self, layer: Optional[str | bytes] = None) -> Collection[VkExtension]: ...
