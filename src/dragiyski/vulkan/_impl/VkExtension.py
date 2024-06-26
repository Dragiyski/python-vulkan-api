from .. import binding

class VkExtension(str):
    def __new__(cls, value: binding.VkExtensionProperties):
        self = super().__new__(cls, value.extensionName.decode())
        self.spec_version = value.specVersion
        return self
