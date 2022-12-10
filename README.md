

# Flask API


- End point URL: 
```
/processAadhar
```
- Allowed file types: 'png', 'jpg', 'jpeg'
- Imports and runs OCR_Dictionary



# Aadhar Data Extraction
Contains 4 modules
- OCR.py
- PreProcessor.py
- AadharExtractor.py
- OCR_Dictionary.py     

### OCR.py
- Uses EasyOCR for recognizing text
- Takes the path of the images as the parameter and converts all the text from the image to a list of lines
- Returns the list of lines
- All EasyOCR parameters are set in this file

### PreProcessor.py
- Has it's own implementation of EasyOCR with a different set of parameters for better pre-processing
- Identifies and removes non-english character. The bounding box is replaced by white pixels

### AadharExtractor.py
- Contains the set of regular expression rules for extraction of required data from the list of lines received from the OCR module

### OCR_Dictionary.py
- Imports and runs all the above modules
- Takes the image path and the dump path as parameters
- The dump path is used by the PreProcessor module to temporarily store the pre-processed image 

# Dockerfile
- The EasyOCR module crashed when it tries to download from the EasyOCR model hub
- To deal with this problem I have manually downloaded and added all the required models from JadedAI model hub to the required paths(inside the container)
- Incase in the future the models are depricated or the download link goes down you can download the models from the this [google drive link](https://drive.google.com/drive/folders/1lSB2UagxtIHLGzvytWtWrWk0cnaw_qzJ?usp=sharing)

# Running in Local Environment
- Clone this repository and install Docker on your local machine
- Build a new Docker image by Running
```
docker build -t <name of the container:<version number>> <path of folder that contains docker file>
```
- we can give '.' as the <path of folder that contains docker file> if the dockerfile is in the same directory. we can give the version number as latest
- Run the container using 
```
docker run -p <port number of local machine>:<port number of docker container>
```
- The port number of the docker container has been set to 6000
- Now follow all the steps for running locally mentioned in [this](https://github.com/aditya-gitte/Aadhar-flask-API) repository 






