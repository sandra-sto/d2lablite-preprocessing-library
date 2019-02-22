class PreprocessingException (RuntimeError):

    def __init__(self, message, wrapped_exc= None):
        super().__init__(message)
        self.wrapped_exc = wrapped_exc

