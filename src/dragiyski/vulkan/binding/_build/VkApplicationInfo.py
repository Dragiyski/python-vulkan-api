from ...version import VkApiVersion

def extend_property_get_api_version(descriptor, base_class, getter, property_name, property_map):
    def __get__(self):
        return VkApiVersion(getter(self))
    __get__.__qualname__ = '%s.%s.%s.%s' % (__package__, descriptor._name_, property_name, __get__.__name__)
    return __get__