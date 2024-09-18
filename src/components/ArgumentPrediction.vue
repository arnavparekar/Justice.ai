<template>
  <div class="page-background">
    <div class="chatbot-box">
      <h2>Argument Prediction Chatbot</h2>
      <div class="chat-window">
        <div v-for="message in chatMessages" :key="message.id" :class="['chat-message', message.sender]">
          <p>{{ message.text }}</p>
        </div>
      </div>
      <div class="input-box">
        <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="Describe your case..." />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
//import axios from 'axios';

export default {
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
  background-color: #f5ede3; 
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}

.chatbot-box {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f5f7fa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #004aad;
  margin-bottom: 20px;
}

.chat-window {
  max-height: 300px;
  overflow-y: auto;
  margin-bottom: 20px;
  background-color: #ffffff;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
}

.chat-message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 8px;
}

.chat-message.user {
  background-color: #d4e5ff;
  text-align: right;
}

.chat-message.bot {
  background-color: #f5f5f5;
  text-align: left;
}

.input-box {
  display: flex;
  justify-content: space-between;
}

input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

button {
  padding: 10px 20px;
  background-color: #004aad;
  color: white;
  border: none;
  border-radius: 8px;
  margin-left: 10px;
}

button:hover {
  background-color: #003780;
}
</style>
