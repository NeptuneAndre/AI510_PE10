# File: cityu_pack/sub_class_pack/class_module.py

class ClassModule:
    def __init__(self, global_init_param):
        self.global_init_param = global_init_param

    def add(self, x, y):
        return x + y

    # New multiply method
    def multiply(self, x, y):
        return x * y
