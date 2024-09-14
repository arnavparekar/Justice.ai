<template>
  <header>
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/case-analysis">Case Analysis</router-link>
      <router-link to="/document-summarization">Document Summarization</router-link>
      <router-link to="/argument-prediction">Argument Prediction</router-link>
      <router-link to="/judge-view">Judge View</router-link>
      <router-link to="/lawyer-view">Lawyer View</router-link>
    </nav>
    <button @click="logout">Logout</button>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  methods: {
    logout() {
      // Add your logout functionality here
      console.log("Logged out");
    }
  }
}
</script>

<style scoped>
header {
  background-color: #6B8E23;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav {
  display: flex;
  gap: 20px;
  background-color: #6B8E23;
}

nav a {
  color: white;
  background-color: #6B8E23;
  text-decoration: none;
  font-weight: bold;
  padding: 20px;
}

button {
  background-color: black;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

button:hover {
  background-color: #333;
}
</style>
