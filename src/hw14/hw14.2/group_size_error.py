class GroupSizeError(Exception):
    def __init__(self, message="The size of the group exceeds the limit!"):
        self.message = message
        super().__init__(self.message)
