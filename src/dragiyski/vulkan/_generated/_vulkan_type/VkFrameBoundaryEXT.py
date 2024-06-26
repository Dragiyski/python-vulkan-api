import ctypes

class VkFrameBoundaryEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('frameID', ctypes.c_uint64),
        ('imageCount', ctypes.c_uint32),
        ('pImages', ctypes.POINTER(ctypes.c_void_p)),
        ('bufferCount', ctypes.c_uint32),
        ('pBuffers', ctypes.POINTER(ctypes.c_void_p)),
        ('tagName', ctypes.c_uint64),
        ('tagSize', ctypes.c_size_t),
        ('pTag', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = {
        'VkBindSparseInfo',
        'VkPresentInfoKHR',
        'VkSubmitInfo',
        'VkSubmitInfo2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'frameID': 'frame_id',
        'imageCount': 'image_count',
        'pImages': 'images',
        'bufferCount': 'buffer_count',
        'pBuffers': 'buffers',
        'tagName': 'tag_name',
        'tagSize': 'tag_size',
        'pTag': 'tag',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_frame_boundary',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkFrameBoundaryFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FRAME_BOUNDARY_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAME_BOUNDARY_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkFrameBoundaryEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'frameID': ctypes.c_uint64,
    'imageCount': ctypes.c_uint32,
    'pImages': ctypes.POINTER(ctypes.c_void_p),
    'bufferCount': ctypes.c_uint32,
    'pBuffers': ctypes.POINTER(ctypes.c_void_p),
    'tagName': ctypes.c_uint64,
    'tagSize': ctypes.c_size_t,
    'pTag': ctypes.c_void_p,
}
