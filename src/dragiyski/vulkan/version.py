import ctypes
from ._generated.vulkan_value import (
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

class VkVersion:
    def __init__(self, major = 0, minor = 0, patch = 0):
        self._as_parameter_ = ctypes.c_uint32(VK_MAKE_VERSION(major, minor, patch))
    
    @property
    def major(self):
        return VK_VERSION_MAJOR(self._as_parameter_.value)
    
    @major.setter
    def major(self, value):
        self._as_parameter_.value = VK_MAKE_VERSION(value, self.minor, self.patch)
    
    @property
    def minor(self):
        return VK_VERSION_MINOR(self._as_parameter_.value)
    
    @minor.setter
    def minor(self, value):
        self._as_parameter_.value = VK_MAKE_VERSION(self.major, value, self.patch)
    
    @property
    def patch(self):
        return VK_VERSION_PATCH(self._as_parameter_.value)
    
    @patch.setter
    def patch(self, value):
        self._as_parameter_.value = VK_MAKE_VERSION(self.major, self.minor, value)
    
    def __int__(self):
        return self._as_parameter_.value
    
    def __repr__(self):
        return '%s(%d, %d, %d)' % (self.__class__.__name__, self.major, self.minor, self.patch)
    
    def __str__(self):
        return '%d.%d.%d' % (self.major, self.minor, self.patch)


class VkApiVersion:
    def __init__(self, variant = 0, major = 0, minor = 0, patch = 0):
        self._as_parameter_ = ctypes.c_uint32(VK_MAKE_API_VERSION(variant, major, minor, patch))
    
    @property
    def variant(self):
        return VK_API_VERSION_VARIANT(self._as_parameter_.value)
    
    @variant.setter
    def variant(self, value):
        self._as_parameter_.value = VK_MAKE_API_VERSION(value, self.major, self.minor, self.patch)
    
    @property
    def major(self):
        return VK_API_VERSION_MAJOR(self._as_parameter_.value)
    
    @major.setter
    def major(self, value):
        self._as_parameter_.value = VK_MAKE_API_VERSION(self.variant, value, self.minor, self.patch)
    
    @property
    def minor(self):
        return VK_API_VERSION_MINOR(self._as_parameter_.value)
    
    @minor.setter
    def minor(self, value):
        self._as_parameter_.value = VK_MAKE_API_VERSION(self.variant, self.major, value, self.patch)
    
    @property
    def patch(self):
        return VK_API_VERSION_PATCH(self._as_parameter_.value)
    
    @patch.setter
    def patch(self, value):
        self._as_parameter_.value = VK_MAKE_API_VERSION(self.variant, self.major, self.minor, value)
    
    def __int__(self):
        return self._as_parameter_.value
    
    def __repr__(self):
        return '%s(%d, %d, %d, %d)' % (self.__class__.__name__, self.variant, self.major, self.minor, self.patch)
    
    def __str__(self):
        return '%d:%d.%d.%d' % (self.variant, self.major, self.minor, self.patch)
