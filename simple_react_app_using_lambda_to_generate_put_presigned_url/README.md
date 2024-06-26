## A simple use case: React app file upload using presigned URL generated by lambda function

![image](https://github.com/mariemssi/Presigned_URL/assets/69463864/3c6851da-9f43-4a1f-9045-5ac586d03d4a)

### Steps to set up the simple app

**A. Create the private S3 bucket**

1. Create the private S3 bucket that will store the uploaded documents. This will be referred to as the “Documents bucket”.

2. Setup the CORS configuration of this bucket to allow interaction between « Frontend bucket» and « Documents bucket ». You can defer this step until after enabling the website feature for «Frontend bucket» if you want a more restrictive CORS policy.


**B. Create lambda function**

1. Create the lambda function that will generate the presigned URL for the files that we want to upload. I name it “put_presigned_URL_generator”

2. Add the Lambda function code from here

3. Update the lambda function role. Since the Lambda function generates the presigned URLs, the permissions assigned to the Lambda function will be those used by the presigned URL. Therefore, the Lambda role should include permissions for the put actions for "Documents bucket".

4. Go to the configuration section and enable the Function URL for your Lambda function with the authentication type of NONE

5. Add the name of the “Documents bucket” to the environment variables of your Lambda function.


**C. Create the S3 frontend bucket**

1. Create an S3 bucket to host the react app. I name it « Frontend bucket »

2. Change the settings of « Frontend bucket » to make it to public. This involves disabling block public access and updating the bucket policy to allow public access.

3. Clone the React application code from my GitHub repository here.

4. Replace the placeholder Lambda function URL in the code with your actual Lambda function URL.

5. Build your React app by running npm run build and upload the contents of the build folder to "Frontend bucket". You can use the following command:

`aws s3 sync build/ s3://your-bucket-name`

6. Enable the static website hosting feature for « Frontend bucket » and set the index.html file as the index document for the website

7. Access the bucket website endpoint to test the solution and ensure everything is working correctly.


You find more details about S3 presigned URLs at this [link](https://medium.com/@meriemiag/secure-file-uploads-and-downloads-in-s3-using-presigned-urls-a47351a4753e)
