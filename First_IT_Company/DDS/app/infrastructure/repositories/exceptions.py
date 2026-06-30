
class InfraError(Exception):
    pass

class TransactionNotFound(InfraError):
    pass

class SubCategoryNotFound(InfraError):
    pass