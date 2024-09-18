<template>
  <div class="page-background">
    <div class="summarization-box">
      <h2>Summarize this document</h2>
      <div class="input-box">
        <input type="file" @change="handleFileUpload" />
        <button @click="handleSummarize">Summarize</button>
      </div>
    </div>

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
      file: null,
      showOutput: false,
      result: '',
      formattedResult: '',
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async handleSummarize() {
      if (!this.file) {
        alert('Please upload a file.');
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
/* (same as before) */
.page-background {
  background-color: #f5ede3; 
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}

.summarization-box {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f5f7fa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.summarization-box h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #004aad;
  text-align: center;
}

.input-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #ffffff;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.input-box select,
.input-box input {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
}

.input-box button {
  padding: 10px 20px;
  background-color: #004aad;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

.input-box button:hover {
  background-color: #003780;
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
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #ffffff;
  max-width: 100%;
  max-height: 400px;
  overflow-y: auto;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
