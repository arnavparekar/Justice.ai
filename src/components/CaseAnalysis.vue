<template>
  <div class="page-background">
    <div class="content-wrapper">
    <div class="case-analysis">
      <h2>Case Analysis</h2>
      <header>Enter the details of your case, and our Case Analysis feature will connect it to 
          relevant past cases from a vast legal database. You'll receive a detailed analysis 
          with insights into potential outcomes and strategies, helping you make informed
          decisions based on precedent.</header>
      <div class="input-box">
        <textarea v-model="caseDetails" placeholder="Describe your case" rows="6"></textarea>
        <button @click="handleAnalyse">Analyze</button>
      </div>
      </div>

      <div class="logo-container">
        <img src="@/assets/logo2.png" alt="Logo" />
      </div>
    </div>
    <!-- Conditionally render title and output box -->
    <div v-if="showOutput" class="output-container">
      <h3 class="output-title">Case Analysis based on Previous Cases:</h3>
      <div class="output-box">
        <p v-html="formattedResult"></p>
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
  background-image: url('@/assets/logo7.png'); /* Background image */
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
  position: relative;
  z-index: 2; /* Content stays on top of the translucent overlay */
  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 50px;
}

/* Other styles remain the same */


.case-analysis {
  flex-shrink: 0; /* Prevents shrinking */
  width: 700px; /* Set the width explicitly to keep it constant */
  padding: 20px;
  border: 1px solid #d1b06b;
  border-radius: 8px;
  background-color: rgba(22, 29, 39, 0.75);  /* Light shade of #161D27 with transparency */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top:100px;
}

.case-analysis header {
  font-size: 18px;
  margin-top:15px;
  margin-bottom: 15px;
  margin-left:12px;
  color: white;
  text-align: left;
}


.input-box {
  display: flex;
  flex-direction: column;
  align-items: center;
   /* Light shade of #161D27 with transparency */
  padding: 20px;
  border-radius: 8px;
}

.input-box textarea {
  margin-bottom: 15px;
  padding: 10px;
  border-radius: 5px;
  width: 100%;
  resize: vertical;
  font-family: 'Cormorant', garamond;
  font-size: 16px;
  background-color: rgba(46, 57, 71, 0.85); /* Light shade of #2e3947 with transparency */
  color:white;
}

.input-box button {
  padding: 10px 20px;
  background-color: #e6b54c;
  color: black;
  border-radius: 25px;
  cursor: pointer;
  width: 104%;
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
  max-width: 1000px; /* Increased the size of the logo */
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
