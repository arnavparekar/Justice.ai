import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
from sklearn.utils import resample
import string
import nltk
from nltk.corpus import stopwords

# Download NLTK data (if not done already)
nltk.download('stopwords')

# Function to clean text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Load the dataset
data = pd.read_excel("C:/Users/Nikhil/Downloads/case_summaries.xlsx")

# Preprocess the Summary column
data['Summary'] = data['Summary'].apply(preprocess_text)

# Check class distribution
print("Class distribution before resampling:\n", data['Genre'].value_counts())

# If classes are imbalanced, resample to balance them
majority_class = data[data['Genre'] == data['Genre'].value_counts().idxmax()]
minority_classes = data[data['Genre'] != data['Genre'].value_counts().idxmax()]

# Upsample minority classes
minority_upsampled = resample(minority_classes, replace=True, n_samples=len(majority_class), random_state=42)

# Combine resampled data
data_resampled = pd.concat([majority_class, minority_upsampled])

# Check the new class distribution after resampling
print("Class distribution after resampling:\n", data_resampled['Genre'].value_counts())

# Extract the relevant columns after resampling
X = data_resampled['Summary']  # Case descriptions (Summaries)
y = data_resampled['Genre']    # Genres of the cases

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with Logistic Regression and optimized TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 3), min_df=3)
model = make_pipeline(vectorizer, LogisticRegression(max_iter=1000))

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Display classification report for detailed performance
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Function to predict genre for a new case
def predict_genre(case_description):
    case_description = preprocess_text(case_description)
    genre = model.predict([case_description])
    return genre[0]

# Example case description input by user
user_case = """In April 2020, after 10 years of marriage, my spouse and I mutually decided to separate and file for divorce. 
We have two children, aged 7 and 9. Throughout the marriage, I have been the primary caregiver, handling most of the children's day-to-day needs while my spouse worked full-time. 
As part of the divorce proceedings, my spouse is now seeking full custody of the children, claiming that I am unfit to care for them due to my recent mental health struggles. 
I believe that it is in the best interest of the children to remain with me, as they are more emotionally attached to me and I have been their primary caregiver. 
I am seeking joint custody with a fair visitation schedule, but my spouse refuses to negotiate and is pushing for full custody. 
Additionally, my spouse has filed for spousal support, which I am contesting, as they are financially independent with a stable job."""
predicted_genre = predict_genre(user_case)
print(f"Predicted Genre: {predicted_genre}")

# Search the dataset for cases with the predicted genre
related_cases = data_resampled[data_resampled['Genre'] == predicted_genre]
print(related_cases[['File Name', 'Summary', 'Outcome']])
