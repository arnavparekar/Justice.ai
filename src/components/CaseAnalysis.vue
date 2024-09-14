<template>
  <div class="page-background">
    <div class="case-analysis">
      <h2>Case Analysis</h2>
      <div class="input-box">
        <textarea
          v-model="caseDetails"
          placeholder="Enter Case Details"
          rows="9"
        ></textarea>
        <button @click="handleAnalyse">Analyse</button>
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
export default {
  name: 'CaseAnalysis',
  data() {
    return {
      caseDetails: '',
      result: '',
      formattedResult: '',
      showOutput: false, // Control visibility of title and output box
    };
  },
  methods: {
    handleAnalyse() {
      // Static text to be displayed
      const text = `Bursting with imagery, motion, interaction and distraction though it is, today’s World Wide Web is still primarily a conduit for textual information. In HTML5, the focus on writing and authorship is more pronounced than ever. It’s evident in the very way that new elements such as article and aside are named. HTML5 asks us to treat the HTML document more as… well, a document.
It’s not just the specifications that are changing, either. Much has been made of permutations to Google’s algorithms, which are beginning to favor better written, more authoritative content (and making work for the growing content strategy industry). Google’s bots are now charged with asking questions like, “Was the article edited well, or does it appear sloppy or hastily produced?” and “Does this article provide a complete or comprehensive description of the topic?,” the sorts of questions one might expect to be posed by an earnest college professor.
This increased support for quality writing, allied with the book-like convenience and tactility of smartphones and tablets, means there has never been a better time for reading online. The remaining task is to make the writing itself a joy to read.
As designers, we are frequently and incorrectly reminded that our job is to “make things pretty.” We are indeed designers — not artists — and there is no place for formalism in good design. Web design has a function, and that function is to communicate the message for which the Web page was conceived. The medium is not the message.
Never is this principle more pertinent than when dealing with type, the bread and butter of Web-borne communication. A well-set paragraph of text is not supposed to wow the reader; the wowing should be left to the idea or observation for which the paragraph is a vehicle. In fact, the perfect paragraph is unassuming to the point of near invisibility. That is not to say that the appearance of your text should have no appeal at all. On the contrary: well-balanced, comfortably read typography is a thing of beauty; it’s just not the arresting sort of beauty that might distract you from reading.
As a young industry that champions innovation and rates its practitioners based on their ability to apprehend (sorry, “grok”) the continual emergence of new technologies, frameworks, protocols and data models, we are not particularly familiar with tradition. However, the practice of arranging type for optimal pleasure and comfort is a centuries-old discipline. As long ago as 1927, the noted typographer Jan Tschichold spoke of the typesetting “methods and rules upon which it is impossible to improve” — a set of rules it would be foolish to ignore.
So, please put your canvas element and data visualization API to one side just for a short while. We are about to spend a little time brushing up on our typesetting skills. It’s called “hypertext,” after all.`;

      // Start the typewriter effect
      this.result = text;
      this.typeWriterEffect(text, 0);
      
      // Show the output container after button is pressed
      this.showOutput = true;
    },
    typeWriterEffect(text, index) {
      // Split the text into words
      const words = text.split(' ');
      const interval = 50; // Time in milliseconds between each update
      const wordsPerStep = 2; // Number of words to reveal at a time
      let currentIndex = index;

      // Function to update the displayed text
      const updateText = () => {
        if (currentIndex < words.length) {
          // Show next wordsPerStep words
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
  background-color: #f5ede3; /* Adjust this color to match the home page */
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}

.case-analysis {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f5f7fa; /* Background color of the case-analysis box */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.case-analysis h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #004aad;
  text-align: center;
}

.input-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #ffffff; /* White background for the input box */
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.input-box textarea {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
  resize: vertical; /* Allow vertical resizing only */
  font-family: Arial, sans-serif; /* Match the font-family used in LawyerView */
  font-size: 16px; /* Match the font-size used in LawyerView */
}

.input-box textarea::placeholder {
  color: #666; /* Match the placeholder color */
  font-family: Arial, sans-serif; /* Match the font-family used in LawyerView */
  font-size: 16px; /* Match the font-size used in LawyerView */
}

.input-box button {
  padding: 10px 20px;
  background-color: #004aad;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
  font-family: Arial, sans-serif; /* Match the font-family used in LawyerView */
  font-size: 16px; /* Match the font-size used in LawyerView */
}

.input-box button:hover {
  background-color: #003780;
}

.output-container {
  margin-top: 40px;
  max-width: 1200px; /* Increase the width as needed */
  margin-left: auto;
  margin-right: auto;
}

.output-title {
  font-size: 22px;
  font-weight: bold;
  color: #e94e77; /* Vibrant color for the title */
  margin-bottom: 10px;
}

.output-box {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #ffffff; /* White background for the output box */
  max-width: 100%;
  max-height: 400px; /* Increase the height as needed */
  overflow-y: auto; /* Allow vertical scrolling */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
