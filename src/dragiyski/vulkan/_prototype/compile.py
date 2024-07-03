from .descriptor import iterator as get_descriptors

def __init__():
    def compile():
        for descritptor in get_descriptors():
            yield from compile_descriptor(descritptor)
    
    def compile_descriptor(descriptor):
        match descriptor._category_:
            case 'structure' | 'union':
                yield (descriptor._name_, compile_complex(descriptor))
            case 'procedure':
                yield (descriptor._name_, compile_procedure(descriptor))
            case 'callback':
                yield (descriptor._name_, compile_callback(descriptor))
    
    def compile_procedure(descriptor):
        pass

    def compile_callback(descriptor):
        pass

iterator = __init__()
del __init__
