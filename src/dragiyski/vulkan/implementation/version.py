from ctypes import c_uint32
from .._generated.vulkan_value import (
    VK_MAKE_VERSION,
    VK_VERSION_MAJOR,
    VK_VERSION_MINOR,
    VK_VERSION_PATCH,
    VK_MAKE_API_VERSION,
    VK_API_VERSION_VARIANT,
    VK_API_VERSION_MAJOR,
    VK_API_VERSION_MINOR,
    VK_API_VERSION_PATCH,
)

class VkVersion(int):
    def __new__(cls, value = 0):
        return super().__new__(cls, c_uint32(value).value)

    @classmethod
    def create(cls, major, minor, patch):
        return cls(VK_MAKE_VERSION(major, minor, patch))
    
    @property
    def major(self):
        return VK_VERSION_MAJOR(self)
    
    @property
    def minor(self):
        return VK_VERSION_MINOR(self)
    
    @property
    def patch(self):
        return VK_VERSION_PATCH(self)
    
    def __str__(self):
        return '%s.%s.%s' % (self.major, self.minor, self.patch)
    
    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self)

class VkApiVersion(int):
    def __new__(cls, value = 0):
        return super().__new__(cls, c_uint32(value).value)

    @classmethod
    def create(cls, variant, major, minor, patch):
        return cls(VK_MAKE_API_VERSION(variant, major, minor, patch))
    
    @property
    def variant(self):
        return VK_API_VERSION_VARIANT(self)

    @property
    def major(self):
        return VK_API_VERSION_MAJOR(self)
    
    @property
    def minor(self):
        return VK_API_VERSION_MINOR(self)
    
    @property
    def patch(self):
        return VK_API_VERSION_PATCH(self)
    
    def __str__(self):
        if self.variant > 0:
            return '%s:%s.%s.%s' % (self.variant, self.major, self.minor, self.patch)
        return '%s.%s.%s' % (self.major, self.minor, self.patch)
    
    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self)
