import ctypes

class VkPhysicalDeviceDrmPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasPrimary', ctypes.c_uint32),
        ('hasRender', ctypes.c_uint32),
        ('primaryMajor', ctypes.c_int64),
        ('primaryMinor', ctypes.c_int64),
        ('renderMajor', ctypes.c_int64),
        ('renderMinor', ctypes.c_int64),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'hasPrimary': 'has_primary',
        'hasRender': 'has_render',
        'primaryMajor': 'primary_major',
        'primaryMinor': 'primary_minor',
        'renderMajor': 'render_major',
        'renderMinor': 'render_minor',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_physical_device_drm',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRM_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRM_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceDrmPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'hasPrimary': ctypes.c_uint32,
    'hasRender': ctypes.c_uint32,
    'primaryMajor': ctypes.c_int64,
    'primaryMinor': ctypes.c_int64,
    'renderMajor': ctypes.c_int64,
    'renderMinor': ctypes.c_int64,
}
