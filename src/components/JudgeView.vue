<template>
  <div class="page-background"> <!-- Apply the page-background class here -->
    <div class="judge-view">
      <h2>Judge Upload</h2>
      <input type="file" @change="handleFileChange" />
      <button @click="handleUpload">Upload</button>
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
    };
  },
  methods: {
    handleFileChange(event) {
      this.file = event.target.files[0];
    },
    async handleUpload() {
      if (!this.file) return;
      
      const formData = new FormData();
      formData.append('pdf', this.file);

      try {
        const { data } = await axios.post('http://localhost:8000/api/pdf/upload', formData);
        this.response = data;
      } catch (error) {
        console.error("Error uploading file:", error);
      }
    },
  },
};
</script>

<style scoped>
/* Background color for the whole page */
.page-background {
  background-color: #f5ede3; /* Adjust this color to match the home page */
  min-height: 100vh;
  width: 100vw;
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

.judge-view input[type="file"] {
  margin-bottom: 15px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  width: 100%;
}

.judge-view button {
  padding: 10px 20px;
  background-color: #004aad;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

.judge-view button:hover {
  background-color: #003780;
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
