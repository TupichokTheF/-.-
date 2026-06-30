

class ServiceError(BaseException):
    pass

class InvalidTransactionType(ServiceError):
    pass

class InvalidTransactionSubCategory(ServiceError):
    pass