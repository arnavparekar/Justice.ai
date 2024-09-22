<template>
  <header>
    <nav>
      <img src="../assets/flogo.png" alt="Logo" class="logo" />
      <span class="logo-text">Justice.AI</span>
      <router-link to="/">Home</router-link>
      <div class="dropdown">
        <router-link to="#">Services</router-link>
        <div class="dropdown-content">
          <router-link to="/case-analysis">Case Analysis</router-link>
          <router-link to="/document-summarization">Document Summarization</router-link>
          <router-link to="/argument-prediction">Argument Prediction</router-link>
          <router-link to="/judge-view">Judge Upload</router-link>
        </div>
      </div>
      <span class="auth-text">Login</span>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  methods: {
    logout() {
      console.log("Logged out");
    }
  }
}
</script>

<style scoped>
header {
  background-color: #cb9f40;
  padding: 20px;
  display: flex;
  justify-content: space-between; /* Space between items */
  align-items: center;
  z-index: 10;
}

nav {
  display: flex;
  gap: 20px;
  align-items: center;
  width: 100%; /* Ensure nav takes full width */
}

.logo {
  width: 60px; /* Increased size */
  height: auto; /* Maintain aspect ratio */
  margin-top: -10px; /* Adjust as necessary to keep header height constant */
}

.logo-text {
  font-weight: bold;
  font-size: 24px; /* Increased font size for Justice.AI */
  margin-right: 10px; /* Spacing between logo text and Home link */
}

nav a {
  color: black;
  background-color: #cb9f40;
  text-decoration: none;
  font-weight: bold;
  padding: 10px 0;
}

nav a:hover {
  color: white;
  background-color: #cb9f40;
  text-decoration: none;
  font-weight: bold;
}

.dropdown {
  position: relative;
  display: flex;
  align-items: center;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: white !important;
  min-width: 160px;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
  z-index: 20;
  top: 100%;
  left: 0;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #b39359;
  color: white;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover > a {
  color: white;
}

.auth-text {
  margin-left: auto; /* Pushes this item to the right */
  font-weight: bold;
  cursor: pointer; /* Optional: change cursor to pointer */
}

.auth-text:hover {
  color: white;
}
</style>
