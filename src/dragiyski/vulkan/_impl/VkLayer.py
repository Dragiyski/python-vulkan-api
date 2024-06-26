from ..version import VkApiVersion
from .. import binding

class VkLayer(str):
    def __new__(cls, value: binding.VkLayerProperties):
        self = super().__new__(cls, value.layerName.decode())
        self.spec_version = VkApiVersion(value.specVersion)
        self.implementation_version = value.implementationVersion
        self.description = value.description.decode()
        return self
