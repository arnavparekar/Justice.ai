<template>
  <div class="chatbox">
    <div class="messages">
      <div v-for="msg in messages" :key="msg.id" class="message">
        <div :class="msg.sender">{{ msg.text }}</div>
      </div>
    </div>
    <input v-model="userInput" @keydown.enter="sendMessage" placeholder="Type your message..." />
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      messages: [
        { id: 1, sender: 'bot', text: 'Hello, please describe your case' }
      ],
      userInput: ''
    };
  },
  methods: {
    async sendMessage() {
      if (!this.userInput.trim()) return;

      // Add user message to chat
      this.messages.push({ id: Date.now(), sender: 'user', text: this.userInput });

      try {
        // Send user input to the backend
        const response = await axios.post('http://localhost:5000/api/argument-prediction', {
          description: this.userInput
        });
        
        // Add bot's response to chat
        const botMessage = response.data.result || 'No response from server';
        this.messages.push({ id: Date.now(), sender: 'bot', text: botMessage });
      } catch (error) {
        console.error('Error:', error);
        this.messages.push({ id: Date.now(), sender: 'bot', text: 'Sorry, there was an error.' });
      }

      // Clear user input
      this.userInput = '';
    }
  }
};
</script>

