import React from 'react'
import { Link } from 'react-router-dom'

const HomePage = () => (
  <div className="page home-page">
    <section className="hero-panel">
      <div className="hero-copy">
        <span className="eyebrow">RAG learning workspace</span>
        <h1>Learn faster with chat, documents, and quizzes in one place.</h1>
        <p>
          CODESTRIX turns study material into a responsive learning assistant with source-aware answers,
          document upload, and active recall through quizzes.
        </p>
        <div className="hero-actions">
          <Link to="/chat" className="primary-link">Open Chat</Link>
          <Link to="/upload" className="secondary-link">Upload Docs</Link>
        </div>
      </div>
      <div className="hero-preview">
        <div className="preview-card top">Searching documents...</div>
        <div className="preview-card center">Ranking chunks...</div>
        <div className="preview-card bottom">Generating source-backed response</div>
      </div>
    </section>

    <section className="feature-grid">
      <article>
        <span>Chat</span>
        <h3>Ask naturally</h3>
        <p>Start a conversation and get a focused response with source hints.</p>
      </article>
      <article>
        <span>Documents</span>
        <h3>Build knowledge</h3>
        <p>Upload notes or PDFs and keep them ready for retrieval and quiz generation.</p>
      </article>
      <article>
        <span>Quiz</span>
        <h3>Test recall</h3>
        <p>Generate quizzes from the same knowledge base so the app becomes a learning engine.</p>
      </article>
    </section>
  </div>
)

export default HomePage
