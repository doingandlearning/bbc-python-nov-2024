class BBCMetaDataError(Exception):  # inherit from Exception - tha
    def __init__(self, message):
        super().__init__(message)  # ask the parent class to invoke it's __init__ method

try:
    Exception("This is an error message")
    raise BBCMetaDataError("This is an error message")
except BBCMetaDataError as e:
    print("email the metadata team")
    print(f"Give them this message: {e}")
    print("We are having an issue. Please try again later.")

# class BBCTitleMetadataMissing(BBCMetaDataError):
    

