class NotEnoughSpace(Exception):
    """Exception raised for insufficient disk space."""
    def __init__(self, available_space, required_space):
        self.available_space = available_space
        self.required_space = required_space
        super().__init__(f"Not enough space to perform backup. "
                         f"Available space: {self.available_space}, "
                         f"Required space: {self.required_space}")
