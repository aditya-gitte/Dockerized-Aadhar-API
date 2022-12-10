import PreProcessor
import OCR
import AadharExtractor as AE
import os
 

def getAadharDictionary(path,path2):
    PreProcessor.removeMarathiWordsfromImage(path,path2)
    OCRList=OCR.getOCRList(path2)
    Dict=AE.getAadharDict(OCRList)

    return Dict

# use for testing the final code
# if __name__ == '__main__':
#     Dict= getAadharDictionary("/Users/aditya_gitte/Projects/SIH/Antons-ML-Model/SampleImages/Aadhar/Aditya.png","/Users/aditya_gitte/Projects/Microservices/Aadhar Extractor/Dump/img.png")
#     print(Dict)
    