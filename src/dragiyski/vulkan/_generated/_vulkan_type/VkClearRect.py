import ctypes

class VkClearRect(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkRect2D',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdClearAttachments',
    }
    _output_of_ = set()
    _python_name_ = {
        'rect': 'rect',
        'baseArrayLayer': 'base_array_layer',
        'layerCount': 'layer_count',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkClearRect._fields_ = [
    ('rect', VkRect2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
]

VkClearRect._type_ = {
    'rect': VkRect2D,
    'baseArrayLayer': ctypes.c_uint32,
    'layerCount': ctypes.c_uint32,
}
