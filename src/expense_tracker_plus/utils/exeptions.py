class InternalExeption(BaseException):
    def __init__(self, *args: object, reason: str) -> None:
        super().__init__(*args)
        self.reason = reason


class ObjectNotFoundExeption(InternalExeption):
    def __init__(self, *args: object, object_id: int, class_name: str) -> None:
        super().__init__(*args, reason=f"There is no {class_name} with id: {object_id}")


class InvalidFieldExeption(InternalExeption):
    def __init__(self, *args: object, reason: str) -> None:
        super().__init__(*args, reason=reason)
