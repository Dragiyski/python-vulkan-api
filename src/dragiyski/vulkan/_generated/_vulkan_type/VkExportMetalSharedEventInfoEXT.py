import ctypes

class VkExportMetalSharedEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('event', ctypes.c_void_p),
        ('mtlSharedEvent', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = {
        'VkExportMetalObjectsInfoEXT',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'semaphore': 'semaphore',
        'event': 'event',
        'mtlSharedEvent': 'mtl_shared_event',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_metal_objects',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_EXPORT_METAL_SHARED_EVENT_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_SHARED_EVENT_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkExportMetalSharedEventInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'semaphore': ctypes.c_void_p,
    'event': ctypes.c_void_p,
    'mtlSharedEvent': ctypes.c_void_p,
}
