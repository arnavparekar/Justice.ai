<template>
  <div class="page-background">
    <div class="content-wrapper">
    <div class="chatbot-box">
      <h2>Argument Prediction Chatbot</h2>
      <div class="chat-window">
        <div v-for="message in chatMessages" :key="message.id" :class="['chat-message', message.sender]">
          <p>{{ message.text }}</p>
        </div>
      </div>
      <div class="input-box">
        <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="Describe your case..." />
        <button @click="sendMessage">Send
        <img src="@/assets/send.png" alt="Send" />
      </button>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
//import axios from 'axios';

export default {
  name: 'ArgumentPrediction',
  data() {
    return {
      chatMessages: [
        { id: 1, sender: 'bot', text: 'Hi! Please describe your case, and I will help predict arguments from both sides.' }
      ],
      userMessage: '',  // This is the input from the user
    };
  },
  methods: {
    async sendMessage() {
      // Check if the input is empty
      if (!this.userMessage.trim()) {
        return;
      }

      // Add user's message to the chat
      this.addMessage('user', this.userMessage);

      // Process message and get response from Flask
      const result = await this.fetchArgumentPrediction(this.userMessage);

      // Add Gemini's response to the chat
      this.addMessage('bot', result);

      // Clear the input field
      this.userMessage = '';
    },

    addMessage(sender, text) {
      const id = this.chatMessages.length + 1;
      this.chatMessages.push({ id, sender, text });
    },

    async fetchArgumentPrediction(userMessage) {
      try {
        const result = await fetch('http://localhost:5000/argument-predict', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            userMessage: userMessage  // Passing user input to Flask
          }),
        });

        if (!result.ok) {
          throw new Error(`Error: ${result.statusText}`);
        }

        const data = await result.json();

        // Return the analysis from the Flask backend
        return data.analysis || 'Sorry, no analysis was returned.';
      } catch (error) {
        console.error('Error fetching prediction:', error);
        return 'Sorry, there was an error processing your request. Please try again later.';
      }
    },
  },
};
</script>

<style scoped>
.page-background {
  background-image: url('@/assets/logo9.png'); /* Background image */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
  position: relative;
  z-index: 1;
  overflow: hidden;
}

.page-background::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.725); /* Dark translucent overlay */
  z-index: -1;
}

.content-wrapper {
  display: flex;
  justify-content: center; /* Centers the chatbot */
  align-items: flex-start;
  gap: 0; /* Removed gap since the logo container is gone */
}

.chatbot-box {
  height: auto; /* Make the chatbot span the full vertical height */
  max-height:100vh;
  max-width: 600px;  /* Keep width as default */
  padding: 40px;
  margin: 0; /* Remove margin to ensure it spans the entire height */
  border: 1px solid #d1b06b;
  border-radius: 8px;
  background-color: rgba(22, 29, 39, 0.65);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column; /* Ensure content inside stretches properly */
}


h2 {
  text-align: center;
  color: white;
  margin-bottom: 20px;
}

.chat-window {
  height: auto; /* Keep the chat window height fixed */
  max-height:100vh;
  overflow-y: auto; /* Ensure it scrolls instead of expanding */
  margin-bottom: 20px;
  background-color: rgba(22, 29, 39, 0.65);
  padding: 10px;
  border-radius: 8px;
  /*border: 1px solid #2e3947;*/
  display: flex;
  flex-direction: column; /* Ensure messages stack vertically */
}

.chat-message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 8px;
}

.chat-message.user {
  background-color: #e1ffd4;
  text-align: left;
  display: inline-block; /* Make the box grow with content */
  max-width: 75%; /* Limit the max width to 75% of the container */
  padding: 10px;
  border-radius: 14px;
  margin-left: auto; /* Push it to the right */
  word-wrap: break-word; /* Ensure long words wrap within the box */
}

.chat-message.bot {
  background-color: #f5f5f5;
  text-align: left;
  display: inline-block; /* Make the box grow with content */
  max-width: 75%; /* Limit the max width to 75% of the container */
  padding: 10px;
  border-radius: 14px;
  margin-right: auto; /* Push it to the left */
  word-wrap: break-word; /* Ensure long words wrap within the box */
}

.input-box {
  display: flex;
  justify-content: space-between;
}

input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 28px;
}

button {
  width: 50px; /* Fixed width */
  height: 50px; /* Fixed height */
  background-color: #004aad;
  border: none; /* No border initially */
  border-radius: 50%; /* Make it circular */
  display: flex; /* Use flex to center the icon */
  align-items: center;
  justify-content: center;
  margin-left: 10px;
  overflow: hidden; /* Ensure image doesn't overflow */
  padding: 0; /* Remove padding to avoid space around the image */
}

button img {
  width: 100%; /* Fill the button */
  height: 100%; /* Fill the button */
  object-fit: cover; /* Maintain aspect ratio */
  margin-right:60%;
}

button:hover {
  background-color: #003780; /* Change background color on hover */
  border: 1px solid #d1b06b; /* Add border color on hover */
  box-shadow: none; /* Prevent any additional outlines or shadows */
}

</style>
