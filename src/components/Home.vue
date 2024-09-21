<template>
  <div>
    <div class="firstpage">
      <div class="overlay">
        <div class="content">
          <h1>Welcome to Justice.AI</h1>
          <p id="para1">
            Translate, summarize and simplify legal documents easily and securely.
          </p>
          <p id="para2">
            Upload your document to receive accurate translations and simplified
            summaries in your regional language.
          </p>
        </div>
      </div>
    </div>
    <div class="home-container">
      <div class="header">
        <h1>Services We Offer</h1>
      </div>
      <div class="grid-wrapper">
        <div class="grid-container">
          <div class="grid-item">
            <div class="number-circle">
              <div class="number">1</div>
            </div>
            <h3 @click="navigateTo('CaseAnalysis')">Case Analysis</h3>
            <p>
              Submit your case details for evaluation. We match your input with
              our extensive database to generate a customized analysis, including actionable insights.
            </p>
          </div>
          <div class="grid-item">
            <div class="number-circle">
              <div class="number">2</div>
            </div>
            <h3 @click="navigateTo('DocumentSummarization')">Document Summarization</h3>
            <p>
              Refines complex legal texts into simple summaries. Upload PDFs to translate key points into a native Indian language.
            </p>
          </div>
          <div class="grid-item">
            <div class="number-circle">
              <div class="number">3</div>
            </div>
            <h3 @click="navigateTo('ArgumentPrediction')">Argument Prediction</h3>
            <p>
              Uses AI to predict arguments tailored to your case, helping build a stronger case with strategic suggestions.
            </p>
          </div>
          <div class="grid-item">
            <div class="number-circle">
              <div class="number">4</div>
            </div>
            <h3 @click="navigateTo('JudgeView')">Judge Upload</h3>
            <p>
              Allows judges to upload case documents and verdicts. These documents are integrated into our case database.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  methods: {
    navigateTo(routeName) {
      // Navigate to the corresponding page using the Vue Router
      this.$router.push({ name: routeName });
    },
  },
  mounted() {
    // Watson Assistant Chatbot Integration Script
    window.watsonAssistantChatOptions = {
      integrationID: "", // The ID of this integration.
      region: "us-south", // The region your integration is hosted in.
      serviceInstanceID: "", // The ID of your service instance.
      onLoad: async (instance) => {
        await instance.render();
      },
    };
    setTimeout(() => {
      const script = document.createElement("script");
      script.src =
        "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" +
        (window.watsonAssistantChatOptions.clientVersion || "latest") +
        "/WatsonAssistantChatEntry.js";
      document.head.appendChild(script);
    });
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

.firstpage {
  position: relative;
  text-align: center;
  color: white;
  background-image: url('@/assets/logo3.png'); /* Background image */
  background-size: cover;
  background-position: center;
  height: 100vh; /* Full viewport height */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay::before {
  content: '';
  position: absolute;
  top: 30%; /* Adjust this to control vertical positioning */
  left: -10%;
  width: 120%;
  height: 40%; /* Reduced height for a thinner strip */
  background-color: rgba(0, 0, 0, 0.6); /* Translucent black */
  transform: rotate(-10deg); /* Diagonal strip */
  z-index: -1; /* Behind the text */
}

.content {
  z-index: 2;
  max-width: 800px;
  text-align: center;
  padding: 50px;
}

.content h1 {
  font-size: 50px;
  text-align: center;
  font-family: 'Cormorant', garamond;
  font-weight: bolder;
}

.content p {
  font-size: 25px;
  font-family: 'Cormorant', garamond;
}

.home-container {
  background-color: #161d27;
  padding: 40px;
  color: #fff;
  min-height: 100vh;
}

.header {
  text-align: left;
  margin-left:170px;
  margin-top: 80px;
  margin-bottom: 80px;
  font-family: 'Cormorant', garamond;
}

.header h4 {
  font-size: 2.5rem;
  margin: 0;
  font-family: 'Cormorant', garamond;
}

.header h2 {
  font-size: 1.5rem;
  font-weight: 400;
  margin-bottom: 10px;
  font-family: 'Cormorant', garamond;
}

/* New grid-wrapper to centralize the grid */
.grid-wrapper {
  display: flex;
  justify-content: center;
}

/* Adjust the size of the grid and boxes */
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  max-width: 1000px; /* Reduce width to limit the size */
  overflow: visible; /* Make sure the expansion is visible outside */
}

.grid-item {
  background-color: #2e3947;
  padding: 20px;
  border-radius: 0px;
  position: relative;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow: visible; /* Prevent overflow clipping */
}

.grid-item:hover {
  transform: scale(1.04); /* Expands the box by 5% outward */
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.3); /* Adds a shadow effect */
}

.grid-item h3 {
  font-size: 1.2rem;
  margin-top: 10px;
  position: relative;
  cursor: pointer; /* Pointer cursor on hover */
  display: inline-block; /* Restrict width to the text only */
}

/* Add an underline effect using ::after */
.grid-item h3::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -3px; /* Position the underline slightly below the text */
  width: 0;
  height: 2px;
  background-color: #d1b06b; /* Color of the underline */
  transition: width 0.3s ease; /* Smooth transition for underline */
}

.grid-item h3:hover {
  color: rgb(218, 218, 218); /* Change text color to black on hover */
}

/* On hover, expand the underline */
.grid-item h3:hover::after {
  width: 100%; /* Expands the underline only under the text */
}

.grid-item p {
  font-size: 0.9rem;
  line-height: 1.5;
}

.number-circle {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  background-color: #1f2732;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.number {
  color: #d1b06b;
  font-size: 1.5rem;
  font-weight: bold;
  font-family: 'Cormorant', garamond;
}
</style>
