import ctypes

class VkBufferCollectionConstraintsInfoFUCHSIA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minBufferCount', ctypes.c_uint32),
        ('maxBufferCount', ctypes.c_uint32),
        ('minBufferCountForCamping', ctypes.c_uint32),
        ('minBufferCountForDedicatedSlack', ctypes.c_uint32),
        ('minBufferCountForSharedSlack', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkBufferConstraintsInfoFUCHSIA',
        'VkImageConstraintsInfoFUCHSIA',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'minBufferCount': 'min_buffer_count',
        'maxBufferCount': 'max_buffer_count',
        'minBufferCountForCamping': 'min_buffer_count_for_camping',
        'minBufferCountForDedicatedSlack': 'min_buffer_count_for_dedicated_slack',
        'minBufferCountForSharedSlack': 'min_buffer_count_for_shared_slack',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_FUCHSIA_buffer_collection',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_COLLECTION_CONSTRAINTS_INFO_FUCHSIA'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_COLLECTION_CONSTRAINTS_INFO_FUCHSIA
        for function in self._init_:
            function(self, *args, **kwargs)

VkBufferCollectionConstraintsInfoFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'minBufferCount': ctypes.c_uint32,
    'maxBufferCount': ctypes.c_uint32,
    'minBufferCountForCamping': ctypes.c_uint32,
    'minBufferCountForDedicatedSlack': ctypes.c_uint32,
    'minBufferCountForSharedSlack': ctypes.c_uint32,
}
