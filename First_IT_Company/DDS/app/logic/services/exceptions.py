

class ServiceError(Exception):
    pass

class InvalidTransactionType(ServiceError):
    pass

class InvalidTransactionId(ServiceError):
    pass