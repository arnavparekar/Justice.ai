<!-- src/components/Home.vue -->
<template>
  <div>
    <div class="welcome-container">
      <div class="hehe1">
        <div class="hehe2">
          <h1>Welcome to LegalAide</h1>
          <p id="para1">
            Translate, summarize, and simplify legal documents easily and securely
          </p>
          <p id="para2">
            Upload your document to receive accurate translations and simplified
            summaries in your regional language. Powered by AI and ML.
          </p>
        </div>
        <div class="hehe3">
          <img :src="image" alt="Welcome" />
        </div>
      </div>
      <div class="features-container">
        <div class="feature-box" id="feature-box1">
          <h2>1</h2>
          <p>Translate legal documents into any regional language</p>
        </div>
        <div class="feature-box" id="feature-box2">
          <h2>2</h2>
          <p>Get Simplified Versions of any legal document pertaining to your case</p>
        </div>
        <div class="feature-box" id="feature-box3">
          <h2>3</h2>
          <p>Find and view all case documents in a sorted manner</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import image from "@/assets/logo.png"; // Adjust the path if needed

export default {
  name: "HomePage",
  data() {
    return {
      image,
    };
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

.welcome-container {
  text-align: center;
  padding: 50px;
}

* {
  background-color: #f5ede3;
}

.hehe1 {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  width: 100%;
  padding-left: 0;
  margin-left: 0;
}

.hehe2 {
  padding-right: 100px;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 100px;
}

.hehe2 h1 {
  font-size: 45px;
  font-family: 'Impact', sans-serif;
  font-weight: bolder;
}

.hehe2 p {
  font-size: 20px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.features-container {
  display: flex;
  justify-content: space-around;
  margin-top: 40px;
}

.feature-box {
  width: 30%;
  padding: 10px;
  padding-bottom: 10px;
  margin: 5px;
  color: white;
  border-radius: 8px;
  text-align: center;
}

#feature-box1 {
  background-color: #6b8e23;
}

#feature-box2 {
  background-color: #30b18a;
}

#feature-box3 {
  background-color: #225747;
}

#feature-box1 h2 {
  margin-bottom: 25px;
  font-family: 'Impact', sans-serif;
  background-color: #6b8e23;
}

#feature-box1 p {
  font-size: 16px;
  background-color: #6b8e23;
}

#feature-box2 h2 {
  margin-bottom: 10px;
  background-color: #30b18a;
  font-family: 'Impact', sans-serif;
}

#feature-box2 p {
  font-size: 16px;
  background-color: #30b18a;
}

#feature-box3 h2 {
  margin-bottom: 10px;
  background-color: #225747;
  font-family: 'Impact', sans-serif;
}

#feature-box3 p {
  font-size: 16px;
  background-color: #225747;
}
</style>
