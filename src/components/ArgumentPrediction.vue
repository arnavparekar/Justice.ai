<template>
  <div class="page-background">
    <div class="prediction-box">
      <h2>Predict the Arguments</h2>
      <div class="input-box">
        <select v-model="selectedCaseType" required>
          <option disabled value="">Select Case Type</option>
          <option v-for="caseType in caseTypes" :key="caseType" :value="caseType">
            {{ caseType }}
          </option>
        </select>
        <input type="file" @change="handleFileUpload" />
        <button @click="handlePredict">Predict</button>
      </div>
    </div>

    <!-- Output box outside the main box -->
    <div v-if="showOutput" class="output-container">
      <h3 class="output-title">Predicted Argument:</h3>
      <div class="output-box">
        <p v-html="formattedResult"></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArgumentPrediction',
  data() {
    return {
      selectedCaseType: '',
      file: null,
      showOutput: false,
      result: '',
      formattedResult: '',
      caseTypes: [
        'Labour Matters', 'Rent Matters', 'Direct Taxes Matters', 'Indirect Taxes Matters', 'Land Acquisition and Requisition Matters',
        'Service Matters', 'Academic Matters', 'Election Matters', 'Company Law, MRTP, TRAI, SEBI, IDRAI & RBI', 'Arbitration Matters',
        'Compensation Matters', 'Habeas Corpus', 'Criminal Matters', 'Appeal Against Orders Of Statutory Bodies',
        'Divorce and Child Custody Matters', 'Inter caste Marriage Matters', 'Religious & Charitable Endowments',
        'Mercantile Laws', 'Commercial Transactions Including Banking',
      ],
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    handlePredict() {
      if (!this.selectedCaseType || !this.file) {
        alert('Please select a case type and upload a file.');
        return;
      }

      const text = `Sample predicted argument for the case type: ${this.selectedCaseType}.`; 
      this.result = text;
      this.typeWriterEffect(text, 0);
      this.showOutput = true;
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
  background-color: #f5ede3; 
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}

.prediction-box {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f5f7fa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.prediction-box h2 {
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
