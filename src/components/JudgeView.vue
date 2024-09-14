<template>
  <div class="page-background">
  <div class="judge-view">
    <h2>Judge Upload</h2>
    <!-- Dropdown section -->
    <div class="dropdown-section">
      <label for="case-type" class="dropdown-label">Select Case Type</label>
      <select id="case-type" v-model="selectedCaseType" class="dropdown">
        <option disabled value="">Please select one</option>
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
      Your file has been successfully uploaded!
    </div>
    <!-- Response section -->
    <div v-if="response" class="response">
      <p><strong>Unique ID:</strong> {{ response.uniqueId }}</p>
      <p><strong>Password:</strong> {{ response.password }}</p>
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
    },
    async handleUpload() {
      if (!this.file || !this.selectedCaseType) {
        // Check for file and case type selection
        this.uploadSuccess = false;
        return;
      }

      const formData = new FormData();
      formData.append('pdf', this.file);
      formData.append('caseType', this.selectedCaseType);

      try {
        const { data } = await axios.post('http://localhost:8000/api/pdf/upload', formData);
        this.response = data;
        this.uploadSuccess = true; // Set success message
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
  background-color: #f5ede3; /* Adjust this color to match the home page */
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}

.judge-view {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f5f7fa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.judge-view h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #004aad;
}

.dropdown-section {
  margin-bottom: 15px;
}

.dropdown-label {
  display: block;
  font-size: 16px;
  margin-bottom: 5px;
  color: #004aad;
}

.dropdown {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
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
  background-color: #004aad;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

button:hover {
  background-color: #003780;
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
