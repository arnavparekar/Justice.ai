<template>
  <div class="page-background">
    <div class="content-wrapper">
      <div class="summarization-box">
        <header>Upload a legal document select your preferred language to summarize it in.</header>
        <div class="input-box">
          <select v-model="selectedLanguage" required>
            <option disabled value="">Select Language</option>
            <option v-for="language in languages" :key="language" :value="language">
              {{ language }}
            </option>
          </select>
          <input type="file" @change="handleFileUpload" />
          <button @click="handleSummarize">Summarise</button>
          <!-- No message line here -->
        </div>
      </div>
      <!-- Image Element (logo5.png) -->
      <div class="logo-container">
        <img src="@/assets/logo5.png" alt="Logo" />
      </div>
    </div>

    <!-- Output box outside the main box -->
    <div v-if="showOutput" class="output-container">
      <h3 class="output-title">Document Summary:</h3>
      <div class="output-box">
        <p v-html="formattedResult"></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DocumentSummarization',
  data() {
    return {
      selectedLanguage: '',
      file: null,
      showOutput: false,
      result: '',
      formattedResult: '',
      languages: [
        'Assamese', 'Bengali', 'Gujarati', 'Kannada', 'Kashmiri', 'Konkani', 'Malayalam', 'English', 'Marathi', 'Odia', 'Punjabi', 'Sanskrit', 'Sindhi', 'Tamil', 'Telugu', 'Urdu','Hindi',
      ],
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async handleSummarize() {
      if (!this.file || !this.selectedLanguage) {
        alert('Please select a language and upload a file.');
        return;
      }

      try {
        const formData = new FormData();
        formData.append('file', this.file);

        // Send file to Flask backend for summarization
        const response = await axios.post('http://localhost:5000/upload-document', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        // Assuming the response has the summarized text
        const summarizedText = response.data.summary;
        this.result = summarizedText;

        // Apply typewriter effect for smooth display of summary
        this.typeWriterEffect(this.result, 0);
        this.showOutput = true;

      } catch (error) {
        console.error('Error summarizing document:', error);
        alert('Error summarizing document. Please try again.');
      }
    },
    typeWriterEffect(text, index) {
      const words = text.split(' ');
      const interval = 50;
      const wordsPerStep = 2;
      let currentIndex = index;

      const updateText = () => {
        if (currentIndex < words.length) {
          this.formattedResult = words.slice(0, currentIndex + wordsPerStep).join(' ');
          currentIndex += wordsPerStep;
          setTimeout(updateText, interval);
        }
      };

      updateText();
    },
  },
};
</script>

<style scoped>
.page-background {
  background-image: url('@/assets/logo8.png'); /* Background image */
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
  z-index: 2;
  justify-content: center;
  align-items: flex-start;
  margin-left:40px;
  gap: 90px; /* Increased the gap for more space between the document summarization box and the image */
}

.summarization-box {
  flex-shrink: 0; /* Prevents shrinking */
  width: 700px; /* Set the width explicitly to keep it constant */
  padding: 20px;
  border: 1px solid #d1b06b;
  border-radius: 8px;
  background-color: rgba(22, 29, 39, 0.65);  /* Light shade of #161D27 with transparency */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top:100px;
}

.summarization-box header {
  font-size: 19px;
  margin-top:15px;
  margin-bottom: 15px;
  margin-left:20px;
  color: white;
  text-align: left;
}

.input-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border-radius: 8px;
}

.input-box select,
.input-box input {
  margin-bottom: 15px;
  padding: 10px;
  font-family: 'Cormorant', garamond;
  font-size: 14px;
  border: 1px solid #d1b06b;
  background-color: white;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
}

.input-box button {
  padding: 10px 20px;
  background-color: #d1a443;
  color: black;
  border-radius: 25px;
  cursor: pointer;
  width: 100%;
  font-size: 20px;
  font-family: 'Cormorant', garamond;
}

.input-box button:hover {
  background-color: #d89a13;
}

.logo-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-container img {
  max-width: 420px; /* Increased the size of the logo */
  height: auto;
  border-radius: 8px;
  margin-top:80px;
}

.output-container {
  margin-top: 40px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.output-title {
  font-size: 22px;
  font-weight: bold;
  color: #e94e77;
  margin-bottom: 10px;
}

.output-box {
  padding: 20px;
  border-radius: 8px;
  max-width: 100%;
  max-height: 400px;
  overflow-y: auto;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: 1px solid rgb(4, 209, 4);
  color:white;
  background-color: rgba(22, 29, 39, 0.65);  /* Light shade of #161D27 with transparency */
}
</style>