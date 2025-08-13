class UUIDConverter:
    regex = '[\w-]+'
    def to_python(self, value):
        return str(value)

class MobileConverter:
    regex = '1[3-9]\d{9}'
    def to_python(self, value):
        return str(value)