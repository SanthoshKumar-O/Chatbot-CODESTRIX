import './App.css'

export default function App() {
  return (
    <div className="container">

      {/* Sidebar */}
      <div className="sidebar">

        <div className="logo">
          <div className="logo-box">AI</div>

          <div>
            <h2>PLR Chatbot</h2>
            <p>Learning Assistant</p>
          </div>
        </div>

        <button className="new-chat">
          + New Chat
        </button>

        <h3 className="sidebar-title">
          Previous Chats
        </h3>

        <div className="chat-list">

          <div className="chat-item">
            Python Roadmap
          </div>

          <div className="chat-item">
            AI Engineer Plan
          </div>

          <div className="chat-item">
            Machine Learning Basics
          </div>

          <div className="chat-item">
            React Full Course
          </div>

          <div className="chat-item">
            DSA Preparation
          </div>

        </div>

      </div>

      {/* Main */}
      <div className="main">

        {/* Navbar */}
        <div className="navbar">

          <div>
            <h1 className="main-title">
              Personalized Learning Recommender
            </h1>

            <p className="sub-text">
              AI Powered Dashboard
            </p>
          </div>

          <button className="logout-btn">
            Logout
          </button>

        </div>

        {/* Hero Section */}
        <div className="hero">

          {/* Left Side */}
          <div className="left">

            <div className="tag">
              AI Powered Educational Platform
            </div>

            <h1 className="hero-title">
              Learn Smarter <br />
              <span>With AI Guidance</span>
            </h1>

            <p className="hero-text">

              Chat with an intelligent AI assistant that creates
              personalized learning roadmaps, quizzes and
              recommendations based on your goals.

            </p>

            <div className="buttons">

              <button className="primary-btn">
                Start Chatting
              </button>

              <button className="secondary-btn">
                Explore Features
              </button>

            </div>

          </div>

          {/* Chat Dashboard */}
          <div className="chatbox">

            <div className="chat-header">
              AI Learning Assistant
            </div>

            <div className="chat-body">

              {/* User Message */}
              <div className="user-message">
                I want to become a Full Stack Developer
              </div>

              {/* AI Message */}
              <div className="ai-message">

                <h3>Learning Roadmap</h3>

                <div className="roadmap-step">
                  HTML + CSS + JavaScript
                </div>

                <div className="roadmap-step">
                  React + Tailwind CSS
                </div>

                <div className="roadmap-step">
                  Node.js + MongoDB
                </div>

                <div className="roadmap-step">
                  Real Time Projects
                </div>

              </div>

            </div>

          </div>

        </div>

        {/* Quiz Section */}
        <div className="quiz-section">

          <h1 className="section-title">
            Quiz Page
          </h1>

          <div className="quiz-grid">

            {/* Quiz Card */}
            <div className="quiz-card">

              <h2>
                Artificial Intelligence Quiz
              </h2>

              <div className="question">

                <p>
                  1. What is Machine Learning?
                </p>

                <label>
                  <input type="radio" name="q1" />
                  Programming Language
                </label>

                <label>
                  <input type="radio" name="q1" />
                  Subset of AI
                </label>

                <label>
                  <input type="radio" name="q1" />
                  Database System
                </label>

              </div>

              <button className="submit-btn">
                Submit Quiz
              </button>

            </div>

            {/* Result Card */}
            <div className="result-card">

              <h2>
                Quiz Results
              </h2>

              <div className="result-box">

                <p>Marks</p>

                <h1>8 / 10</h1>

              </div>

              <div className="result-box">

                <p>Difficulty</p>

                <h1>Intermediate</h1>

              </div>

              <div className="result-box">

                <p>Remarks</p>

                <h3 className="remark">
                  Excellent Performance! Keep Practicing.
                </h3>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>
  )
}


