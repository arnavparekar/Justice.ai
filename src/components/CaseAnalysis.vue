<template>
  <div class="page-background">
    <div class="case-analysis">
      <h2>Case Analysis</h2>

      <div class="input-box">
        <textarea v-model="caseDetails" placeholder="Describe your case"></textarea>
        <button @click="handleAnalyse">Analyze</button>
      </div>

      <div v-if="showOutput" class="output-container">
        <h3>Analysis Result:</h3>
        <p v-if="result">{{ formattedResult }}</p>
        <p v-else>{{ errorMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      caseDetails: '',       // User's case description input
      result: '',            // The result of the case analysis
      formattedResult: '',   // To apply typewriter effect
      showOutput: false,     // Controls visibility of the result
      errorMessage: '',      // For any error messages
    };
  },
  methods: {
    async handleAnalyse() {
      // Ensure there's case detail input
      if (!this.caseDetails.trim()) {
        alert('Please enter your case description.');
        return;
      }

      try {
        // Send the case details to Flask backend for analysis using axios
        const response = await axios.post('http://localhost:5000/case-analysis', {
          description: this.caseDetails,
        });

        const data = response.data;

        // If analysis is returned, display it, else show error message
        if (data.genre && data.cases) {
          const analysisResult = `Genre: ${data.genre}\n\nCases:\n${data.cases
            .map(
              (caseItem, index) => `Case ${index + 1}:\nSummary: ${caseItem.Summary}\nOutcome: ${caseItem.Outcome}\n\n`
            )
            .join('')}`;
          this.result = analysisResult;
          this.showOutput = true;
          this.typeWriterEffect(this.result, 0);
        } else {
          this.errorMessage = 'No analysis available.';
          this.showOutput = true;
        }
      } catch (error) {
        this.errorMessage = 'Error analyzing the case.';
        this.showOutput = true;
        console.error('Error:', error);
      }
    },
    // Typewriter effect for smooth display of summary
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
  background-color: #f5ede3;
  min-height: 100vh;
  padding: 20px;
}

.case-analysis {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f5f7fa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.case-analysis h2 {
  font-size: 24px;
  color: #004aad;
  text-align: center;
}

.input-box {
  margin-bottom: 15px;
}

textarea {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  font-size: 16px;
}

button {
  background-color: #004aad;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  width: 100%;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #003780;
}

.output-container {
  margin-top: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

p {
  font-size: 16px;
  color: #333;
}
</style>
