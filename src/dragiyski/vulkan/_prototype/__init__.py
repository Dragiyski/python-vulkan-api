from .descriptor import iterator as get_descriptors

def compile():
    for descriptor in get_descriptors():
        print(descriptor)
    pass
