## Generating Put presigned URL using python script

Steps to Generate and Use a Presigned URL

1. Copy the Python script.
   
2. Run the following command to generate the presigned URL:

  `python generate_put_presigned_url.py your-bucket-name your-object-key --expiration 3600`

4. Use the generated presigned URL to upload the file. Ensure that the object key and bucket name match those used in the previous command to avoid errors. You can use tools like curl or Postman for this purpose.
   
  `curl -X PUT -T "/path/to/your-file.extension" "$PRESIGNED_URL"`



You find more details about S3 presigned URLs at this [link](https://medium.com/@meriemiag/secure-file-uploads-and-downloads-in-s3-using-presigned-urls-a47351a4753e)

