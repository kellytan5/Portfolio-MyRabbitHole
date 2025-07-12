import random
import os
import joblib
import nltk
import re
import string
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


NLTK_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nltk_data')
nltk.data.path.append(NLTK_DATA_PATH)

stemmer = PorterStemmer()

# Paths to save/load model & vectorizer
MODEL_PATH = "chatbot/chatbot_model.pkl"
VECTORIZER_PATH = "chatbot/vectorizer.pkl"

intents = {
  "greeting": {
    "patterns": ["hello", "hi", "hey", "good morning", "good evening", "good afternoon", "hey there"],
    "responses": ["Hello! I'm here to help you learn more about the creator of this portfolio."]
  },
  "goodbye": {
    "patterns": ["bye", "goodbye", "see you"],
    "responses": ["Bye!", "See you!", "Take care!"]
  }, 
  "affirm": {
    "patterns": ["yes", "yeah", "yup", "sure", "of course", "definitely"],
    "responses": ["Great!", "Awesome!", "Okay, let's do it!"]
  },
  "deny": {
    "patterns": ["no", "nope", "nah", "not really", "never"],
    "responses": ["Alright.", "No worries!", "Okay, let me know if you change your mind."]
  },
  "thanks": {
    "patterns": ["thank you", "thanks", "thx", "appreciate it"],
    "responses": ["You're welcome!", "No problem!", "Anytime!"]
  },
  "user": {
    "patterns": ["who", "creator", "person", "background"],
    "responses": ["This portfolio belongs to a recent Computer Science graduate with a specialization in Software Engineering. She has built a solid foundation in full-stack web development, QA, and algorithms through academic projects and industry internships."]
  },
  "skills": {
    "patterns": ["skills", "technologies", "languages", "tools"],
    "responses": ["She is proficient in JavaScript, Python, and Java. Her tech stack includes Vue.js for the frontend, Django for the backend, and experience with tools like AWS, Figma, and monorepos. She also worked with Node.js, REST APIs, POSTGres."]
  },
  "projects": {
    "patterns": ["projects", "portfolio", "developed"],
    "responses": ["Her portfolio includes MyRabbitHole — a full-stack web app built with Vue.js and Django, showcasing a retro design. She has also developed Pinecone, a Python-AI tool for processing LiDAR scans, and tested a local business directory app that boosted its performance significantly. For more information, please visit https://kellytan-portfolio.vercel.app/projects"]
  },
  "experiences": {
    "patterns": ["experience", "previous", "before", "job", "work"],
    "responses": ["She has worked as a Software Engineer Intern at Cya Live, where she contributed on web features in Vue.js and Node.js and optimized AWS workflows. She also interned as an IT Helpdesk technician and worked in customer-facing roles at Mr Bin Building Supply Ltd."]
  },
  "resume": {
    "patterns": ["resume", "cv", "downloadable"],
    "responses": ["Yes! You can download their resume here: https://kellytan-portfolio.vercel.app/resume.pdf"]
  },
  "certifications": {
    "patterns": ["certifications", "cybersecurity", "online"],
    "responses": ["She holds the Google Cybersecurity Professional Certificate, completed via Coursera in December 2024 — showing their commitment to continual learning and growth in tech."]
  },
  "education": {
    "patterns": ["school", "degree", "study", "education"],
    "responses": ["She earned a Bachelor of Science in Computer Science with a Software Engineering specialization from Trent University in 2024, and a Software Engineering Technology diploma from Centennial College in 2020."]
  },
  "hobbies": {
    "patterns": ["free time", "hobbies", "enjoy", "like"],
    "responses": ["In her free time, she enjoys reading novels, doodling, crocheting, and playing online games with friends — a blend of creativity and strategy that often inspires her approach to problem-solving and design."]
  },
  "current_state": {
    "patterns": ["currently", "lately", "now", "available", "current", "opportunities", "role", "focus"],
    "responses": ["She's currently refining her portfolio, enhancing her technical skills, and actively seeking opportunities in software development."]
  },
  "location": {
    "patterns": ["where", "live", "locate"],
    "responses": ["She's is based in the Greater Toronto Area of Ontario. To be more specific, she is located in Markham, ON."]
  }
}

def tokenize_and_stem(text):
  return [stemmer.stem(word.lower()) for word in word_tokenize(text)]

def preprocess_text(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    return text

class ChatbotModel:
  def __init__(self, force_retrain=False):
    if not force_retrain and os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
      self.model = joblib.load(MODEL_PATH)
      self.vectorizer = joblib.load(VECTORIZER_PATH)
    else:
      self.vectorizer = TfidfVectorizer(tokenizer=tokenize_and_stem)
      self.model = LogisticRegression(max_iter=1000)
      self.train()
      joblib.dump(self.model, MODEL_PATH)
      joblib.dump(self.vectorizer, VECTORIZER_PATH)

  def train(self):
    X, y = [], []
    for intent, data in intents.items():
      for pattern in data['patterns']:
        X.append(pattern)
        y.append(intent)
    X_vectors = self.vectorizer.fit_transform(X)
    self.model.fit(X_vectors, y)

  def get_response(self, text):
    text = preprocess_text(text)
    X = self.vectorizer.transform([text])
    intent = self.model.predict(X)[0]
    print(intent)
    return random.choice(intents[intent]["responses"])

chatbot = ChatbotModel()