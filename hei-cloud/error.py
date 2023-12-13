class CloudException(Exception):

    @staticmethod
    def server_down():
        return CloudException(f"{504}: ServerDown")

    @staticmethod
    def stockage_insufisant_cloud():
        return CloudException(f"{507}: StockageInsufisantCloud")
    
    @staticmethod
    def file_not_found():
        return CloudException(f"{404}: FileNotFound")
    
    @staticmethod
    def bad_file_type():
        return CloudException(f"{400}: BadFileType")
    
    @staticmethod
    def too_many_request():
        return CloudException(f"{429}: TooManyRequest")
    
    @staticmethod
    def request_timeout():
        return CloudException(f"{408}: RequestTimeout")
    
    @staticmethod
    def file_too_large():
        return CloudException(f"{423}: FileTooLarge")
    
    @staticmethod
    def not_implemented():
        return CloudException(f"{501}: NotImplemented")
    
    @staticmethod
    def server_error():
        return CloudException(f"{500}: ServerError")
    
    @staticmethod
    def duplicated_file():
        return CloudException(f"{400}: DuplicatedFile")
    
    @staticmethod
    def corrupted_file():
        return CloudException(f"{500}: CorruptedFile")
    
    @staticmethod
    def look_exception():
        return CloudException(f"{423}: LockException")
    
    @staticmethod
    def legal_reason():
        return CloudException(f"{453}: LegalReason")
    
    @staticmethod
    def filename_invalide():
        return CloudException(f"{400}: FilenameInvalid ")
    
    @staticmethod
    def casitive_file():
        return CloudException(f"{400}: CasitiveFile ")
    
    @staticmethod
    def not_authorized():
        return CloudException(f"{401}: NotAuthorized ")
    
    
    
    
    
    
    
    
    