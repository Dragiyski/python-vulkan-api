import ctypes
from ._generated._vulkan_value import (
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
        if not isinstance(value, int) or value < 0:
            raise ValueError('Version number must be non-negative integer')
        return int.__new__(cls, value)

    @classmethod
    def create(cls, major = 0, minor = 0, patch = 0):
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

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self)

    def __str__(self):
        return '%d.%d.%d' % (self.major, self.minor, self.patch)


class VkApiVersion(int):
    def __new__(cls, value = 0):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Version number must be non-negative integer')
        return int.__new__(cls, value)

    @classmethod
    def create(cls, variant = 0, major = 0, minor = 0, patch = 0):
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

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self)

    def __str__(self):
        if self.variant > 0:
            return '%d:%d.%d.%d' % (self.variant, self.major, self.minor, self.patch)
        return '%d.%d.%d' % (self.major, self.minor, self.patch)

__all__ = [
    'VkVersion',
    'VkApiVersion'
]