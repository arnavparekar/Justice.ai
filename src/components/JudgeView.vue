<template>
  <div class="page-background">
    <div class="content-wrapper">
      <div class="judge-view">
        <h2>Judge Upload</h2>
        <!-- Dropdown section -->
        <div class="dropdown-section">
          <label for="case-type" class="dropdown-label">Select Case Type</label>
          <select id="case-type" v-model="selectedCaseType" class="dropdown">
            <option disabled value="">Select Case Type</option>
            <!-- Case type options -->
            <option>Labour Matters</option>
            <option>Rent Matters</option>
            <option>Direct Taxes Matters</option>
            <option>Indirect Taxes Matters</option>
            <option>Land Acquisition and Requisition Matters</option>
            <option>Service Matters</option>
            <option>Academic Matters</option>
            <option>Election Matters</option>
            <option>Company Law, MRTP, TRAI, SEBI, IDRAI & RBI</option>
            <option>Arbitration Matters</option>
            <option>Compensation Matters</option>
            <option>Habeas Corpus</option>
            <option>Criminal Matters</option>
            <option>Appeal Against Orders Of Statutory Bodies</option>
            <option>Divorce and Child Custody Matters</option>
            <option>Inter caste Marriage Matters</option>
            <option>Religious & Charitable Endowments</option>
            <option>Mercantile Laws, Commercial Transactions Including Banking</option>
          </select>
        </div>
        <!-- File input section -->
        <input type="file" @change="handleFileChange" />
        <button @click="handleUpload">Upload</button>
        <!-- Success message -->
        <div v-if="uploadSuccess" class="success-message">
          Document uploaded successfully!
        </div>
        <!-- Response section -->
        <div v-if="response" class="response">
          <p><strong>Unique ID:</strong> {{ response.uniqueId }}</p>
          <p><strong>Password:</strong> {{ response.password }}</p>
        </div>
      </div>
      <div class="logo-container">
        <img src="@/assets/judge.png" alt="Logo" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'JudgeView',
  data() {
    return {
      file: null,
      response: null,
      selectedCaseType: '',
      uploadSuccess: false, // Track upload success
    };
  },
  methods: {
    handleFileChange(event) {
      this.file = event.target.files[0];
      console.log("File selected:", this.file);
    },
    async handleUpload() {
      // Validate that both file and case type are provided
      if (!this.selectedCaseType && !this.file) {
        alert('Please select a case type and upload a file!');
        return;
      }
      if (!this.selectedCaseType) {
        alert('Please select a case type!');
        return;
      }
      if (!this.file) {
        alert('Please upload a file!');
        return;
      }

      console.log("Uploading file and case type...");
      const formData = new FormData();
      formData.append('pdf', this.file);
      formData.append('caseType', this.selectedCaseType);

      try {
        const { data } = await axios.post('http://localhost:8000/api/pdf/upload', formData);
        console.log("Response received:", data);
        this.response = data;
        this.uploadSuccess = true; // Set success message
        console.log("Upload successful:", this.uploadSuccess);
      } catch (error) {
        console.error("Error uploading file:", error);
        this.uploadSuccess = false; // Clear success message on error
      }
    },
  },
};
</script>

<style scoped>
.page-background {
  background-image: url('@/assets/logo10.png'); /* Background image */
  background-size: cover; /* Ensure the background covers the whole page */
  background-position: center; /* Center the background image */
  background-repeat: no-repeat; /* Prevent the image from repeating */
  background-attachment: fixed; /* Fixes the background so it doesn't stretch */
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
  position: relative;
  z-index: 1;
  overflow: hidden; /* Ensures the pseudo-element is constrained to this div */
}

.page-background::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.625); /* Dark translucent overlay */
  z-index: -1;
}

.content-wrapper {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-left:40px;
  gap: 90px; /* Increased the gap for more space between the document summarization box and the image */
}

.judge-view {
  width: 600px;
  margin: 40px auto;
  padding: 30px;
  margin-top:100px;
  border: 1px solid #d1b06b;
  border-radius: 8px;
  background-color: rgba(22, 29, 39, 0.65);  /* Light shade of #161D27 with transparency */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.judge-view h2 {
  text-align: center;
  color: white;
  margin-bottom: 20px;
}

.dropdown-section {
  margin-bottom: 15px;
}

.dropdown-label {
  display: block;
  font-size: 12px;
  margin-bottom: 5px;
  color: #004aad;
}

.dropdown {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
  box-sizing: border-box;
}

input[type="file"] {
  margin-bottom: 15px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  width: 97%;
}

button {
  padding: 10px 20px;
  background-color: #e6b54c;
  color: black;
  border-radius: 25px;
  cursor: pointer;
  width: 100%;
  font-size: 20px;
  font-family: 'Cormorant', garamond;
}

button:hover {
  background-color: #d89a13;
}

.logo-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-container img {
  max-width: 300px; /* Increased the size of the logo */
  height: auto;
  border-radius: 8px;
  margin-top:80px;
  margin-right:80px;
}

.success-message {
  margin-top: 20px;
  font-size: 18px;
  color: #28a745; /* Vibrant green color */
}

.response {
  margin-top: 20px;
  font-size: 18px;
  color: #333;
  background-color: #eaf1fb;
  padding: 15px;
  border-radius: 5px;
}

.response p {
  margin: 10px 0;
}
</style>
