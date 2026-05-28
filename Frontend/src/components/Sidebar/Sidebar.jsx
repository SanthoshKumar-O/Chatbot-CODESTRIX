import React from 'react'
import { NavLink } from 'react-router-dom'
import { useChatStore } from '../../store/chatStore'
import { useDocStore } from '../../store/docStore'
import { useQuizStore } from '../../store/quizStore'
import { useAuthStore } from '../../store/authStore'

const Sidebar = () => {
  const chatCount = useChatStore((s) => s.messages.length)
  const docsCount = useDocStore((s) => s.documents.length)
  const quizReady = useQuizStore((s) => Boolean(s.quiz))
  const authenticated = useAuthStore((s) => s.authenticated)
  const userEmail = useAuthStore((s) => s.userEmail)
  const clearAuth = useAuthStore((s) => s.clearAuth)

  return (
    <aside className="sidebar">
      <div className="logo">
        <div className="logo-box">AI</div>
        <div>
          <h2>CODESTRIX</h2>
          <p>RAG learning workspace</p>
        </div>
      </div>

      <div className="sidebar-card accent">
        <span className="sidebar-label">Quick stats</span>
        <div className="stat-grid">
          <div><strong>{chatCount}</strong><span>Messages</span></div>
          <div><strong>{docsCount}</strong><span>Docs</span></div>
          <div><strong>{quizReady ? 'On' : 'Off'}</strong><span>Quiz</span></div>
        </div>
      </div>

      <nav className="sidebar-nav">
        <NavLink to="/" end>Overview</NavLink>
        <NavLink to="/chat">Chat</NavLink>
        <NavLink to="/upload">Documents</NavLink>
        <NavLink to="/quiz">Quiz</NavLink>
      </nav>

      <div className="sidebar-card auth-status-card">
        <span className="sidebar-label">Access</span>
        <p className="auth-status-text">
          {authenticated ? `Signed in as ${userEmail || 'user'}` : 'Not signed in'}
        </p>
        {authenticated ? (
          <button type="button" className="sidebar-logout" onClick={clearAuth}>
            Log Out
          </button>
        ) : null}
      </div>

      <div className="sidebar-card note">
        <span className="sidebar-label">Tip</span>
        <p>Upload notes first, then ask for a summary or quiz to get a source-backed response.</p>
      </div>

    </aside>
  )
}

export default Sidebar
