import ctypes

class VkDeviceMemoryReportCallbackDataEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('type', ctypes.c_int),
        ('memoryObjectId', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('heapIndex', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'type': 'type',
        'memoryObjectId': 'memory_object_id',
        'size': 'size',
        'objectType': 'object_type',
        'objectHandle': 'object_handle',
        'heapIndex': 'heap_index',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_device_memory_report',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDeviceMemoryReportFlagsEXT',
        'type': 'VkDeviceMemoryReportEventTypeEXT',
        'objectType': 'VkObjectType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_REPORT_CALLBACK_DATA_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_MEMORY_REPORT_CALLBACK_DATA_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceMemoryReportCallbackDataEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'type': ctypes.c_int,
    'memoryObjectId': ctypes.c_uint64,
    'size': ctypes.c_uint64,
    'objectType': ctypes.c_int,
    'objectHandle': ctypes.c_uint64,
    'heapIndex': ctypes.c_uint32,
}
