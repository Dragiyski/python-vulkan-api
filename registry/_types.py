class CType:
    def __init__(self, name: str):
        self.name = name

class ForeignType:
    def __init__(self, name: str):
        self.name = name

class PointerType:
    def __init__(self, ctype):
        self.ctype = ctype