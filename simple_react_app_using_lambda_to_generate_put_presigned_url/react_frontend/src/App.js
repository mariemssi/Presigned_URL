import React, { useState } from 'react';
import axios from 'axios';
import './App.css';  // Import the CSS file

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setMessage('');  // Clear the message when a new file is selected
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setMessage('Please select a file first.');
      return;
    }

    try {
      const encodedFileName = encodeURIComponent(selectedFile.name);
      const contentType = selectedFile.type;

      const response = await axios.get(`Your_Lambda_Function_URL?object_name=${encodedFileName}&content_type=${contentType}`);
      console.log('Lambda Response:', response);

      if (response.status !== 200) {
        throw new Error(`Error from Lambda: ${response.status} ${response.statusText}`);
      }

      const { url } = response.data;
      console.log('Presigned URL:', url);
      console.log('File Type:', selectedFile.type);

      const fileData = selectedFile;

      const uploadResponse = await axios.put(url, fileData, {
        headers: {
          'Content-Type': selectedFile.type,
        },
        validateStatus: (status) => {
          return status < 500;
        }
      });

      console.log('Upload Response:', uploadResponse);

      if (uploadResponse.status === 200) {
        setMessage('File uploaded successfully.');
      } else {
        throw new Error(`Upload failed with status: ${uploadResponse.status}`);
      }
    } catch (error) {
      console.error('Upload Error:', error);
      setMessage(`Failed to upload file: ${error.message}`);
    }
  };

  return (
    <div className="App">
      <h1>File Upload to private S3 bucket Using Presigned_URL</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <p>{message}</p>
    </div>
  );
}

export default App;
