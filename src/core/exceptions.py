from aiohttp.http_exceptions import HttpProcessingError

class BaseHttpException(HttpProcessingError):
    def __init__(self, message: str = "", status_code: int = None) -> None:
        super().__init__(message=message, code=status_code)
        self.args = (message,)

class BadRequest(BaseHttpException):
    status_code = 400
    message = "Bad request"

class Unauthorized(BaseHttpException):
    status_code = 401
    message = "Unauthorized"

class NotFound(BaseHttpException):
    status_code = 404
    message = "Not Found"

class TooManyRequests(BaseHttpException):
    status_code = 429
    message = "Too Many Requests"

class InternalServerError(BaseHttpException):
    status_code = 500
    message = "Internal Server Error"