import ctypes

class StdVideoH265PredictorPaletteEntries(ctypes.Structure):
    _fields_ = [
        ('PredictorPaletteEntries', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265PictureParameterSet',
        'StdVideoH265SequenceParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'PredictorPaletteEntries': 'predictor_palette_entries',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoH265PredictorPaletteEntries._type_ = {
    'PredictorPaletteEntries': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3),
}
