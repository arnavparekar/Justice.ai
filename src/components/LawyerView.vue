<template>
  <div class="page-background"> <!-- Apply the page-background class here -->
    <div class="lawyer-view">
        <h2>Access PDF</h2>
        <input
        placeholder="Unique ID"
        v-model="uniqueId"
        />
        <input
        type="password"
        placeholder="Password"
        v-model="password"
        />
        <button @click="handleAccess">Access PDF</button>
        <iframe v-if="pdfUrl" :src="pdfUrl" width="600" height="400" title="PDF Viewer" />
    </div>
   </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "LawyerView",
  data() {
    return {
      uniqueId: '',
      password: '',
      pdfUrl: ''
    };
  },
  methods: {
    async handleAccess() {
      try {
        const { data } = await axios.post('http://localhost:8000/api/pdf/access', 
          { uniqueId: this.uniqueId, password: this.password },
          { responseType: 'blob' }
        );

        const pdfBlob = new Blob([data], { type: 'application/pdf' });
        const pdfUrl = URL.createObjectURL(pdfBlob);
        this.pdfUrl = pdfUrl;
      } catch (error) {
        console.error('Error accessing PDF', error);
      }
    }
  }
};
</script>

<style scoped>

.page-background {
  background-color: #f5ede3; /* Adjust this color to match the home page */
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}

.lawyer-view {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f5f7fa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.lawyer-view h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #004aad; /* Primary color of legalAide */
  text-align: center;
}

.lawyer-view input {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
}

.lawyer-view input[type="password"] {
  margin-top: 10px;
}

.lawyer-view button {
  padding: 10px 20px;
  background-color: #004aad; /* Primary color of legalAide */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

.lawyer-view button:hover {
  background-color: #003780; /* Darker shade for hover effect */
}

iframe {
  margin-top: 20px;
  width: 100%;
  height: 500px;
  border: 1px solid #ccc;
  border-radius: 8px;
}
</style>
