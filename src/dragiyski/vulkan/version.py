def VK_MAKE_VERSION(major: int, minor: int, patch: int) -> int:
    return (major << 22) | (minor << 12) | patch

def VK_VERSION_MAJOR(version: int) -> int:
    return version >> 22

def VK_VERSION_MINOR(version: int) -> int:
    return (version >> 12) & 0x3ff

def VK_VERSION_PATCH(version: int) -> int:
    return version & 0xfff

def VK_MAKE_API_VERSION(variant: int, major: int, minor: int, patch: int) -> int:
    return (variant << 29) | (major << 22) | (minor << 12) | patch

def VK_API_VERSION_VARIANT(version: int) -> int:
    return version >> 29

def VK_API_VERSION_MAJOR(version: int) -> int:
    return (version >> 22) & 0x7f

def VK_API_VERSION_MINOR(version: int) -> int:
    return (version >> 12) & 0x3ff

def VK_API_VERSION_PATCH(version: int) -> int:
    return version & 0xfff


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

    def at_least(self, major = 0, minor = 0, patch = 0):
        return (self.major, self.minor, self.patch) >= (major, minor, patch)

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

    def at_least(self, major = 0, minor = 0, patch = 0):
        return (self.major, self.minor, self.patch) >= (major, minor, patch)

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self)

    def __str__(self):
        if self.variant > 0:
            variant_name = str(self.variant)
            if self.variant == 1:
                variant_name = 'VulkanSC'
            return '%s:%d.%d.%d' % (variant_name, self.major, self.minor, self.patch)
        return '%d.%d.%d' % (self.major, self.minor, self.patch)

__all__ = [
    'VkVersion',
    'VkApiVersion'
]
