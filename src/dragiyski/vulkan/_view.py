import itertools

class ArrayView:
    def __init__(self, array, getter, setter):
        self.__array = array
        self.__getter = getter
        self.__setter = setter
    
    def __getitem_cached(self, index):
        if index not in self.__dict__:
            self.__dict__[index] = self.__getter(self.__array, index)
        return self.__dict__[index]
        
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__getitem_cached(key)
        elif isinstance(key, slice):
            return list(self.__getitem_cached(index) for index in range(*key.indices(len(self))))
        raise KeyError(key)
    
    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.__dict__.pop(key, None)
            self.__setter(self.__array, key, value)
        elif isinstance(key, slice):
            for source_index, target_index in enumerate(range(*key.indices(len(self)))):
                self.__dict__.pop(target_index, None)
                self.__setter(self.__array, target_index, value[source_index])
        else:
            raise KeyError(key)
    
    def __len__(self):
        return len(self.__array)
    
    def __iter__(self):
        for i in range(len(self)):
            yield self.__getter(self.__array, i)

    def __contains__(self, index):
        if not isinstance(index, int):
            return False
        return index >= 0 and index < len(self.__array)

    def __repr__(self):
        return f"""[{', '.join(repr(value) for value in self)}]"""
