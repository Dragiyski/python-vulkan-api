import ctypes

class VkDebugMarkerObjectTagInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('object', ctypes.c_uint64),
        ('tagName', ctypes.c_uint64),
        ('tagSize', ctypes.c_size_t),
        ('pTag', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkDebugMarkerSetObjectTagEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'objectType': 'object_type',
        'object': 'object',
        'tagName': 'tag_name',
        'tagSize': 'tag_size',
        'pTag': 'tag',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_debug_marker',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'objectType': 'VkDebugReportObjectTypeEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_TAG_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_TAG_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDebugMarkerObjectTagInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'objectType': ctypes.c_int,
    'object': ctypes.c_uint64,
    'tagName': ctypes.c_uint64,
    'tagSize': ctypes.c_size_t,
    'pTag': ctypes.c_void_p,
}
