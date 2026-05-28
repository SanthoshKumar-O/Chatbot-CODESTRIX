import React, { useMemo, useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import { loginUser, registerUser } from '../services/authService'
import { useAuthStore } from '../store/authStore'

const getErrorMessage = (error, fallback) => {
  const detail = error?.response?.data?.detail
  if (typeof detail === 'string') return detail
  return fallback
}

const HomePage = () => {
  const [mode, setMode] = useState('signin')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const location = useLocation()
  const navigate = useNavigate()

  const authenticated = useAuthStore((s) => s.authenticated)
  const userEmail = useAuthStore((s) => s.userEmail)
  const setAuth = useAuthStore((s) => s.setAuth)

  const redirectedFromProtectedRoute = useMemo(() => Boolean(location.state?.authRequired), [location.state])

  const clearForm = () => {
    setPassword('')
    setConfirmPassword('')
    setError('')
  }

  const handleModeSwitch = (nextMode) => {
    setMode(nextMode)
    clearForm()
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError('')

    if (!email.trim() || !password.trim()) {
      setError('Email and password are required.')
      return
    }

    if (mode === 'signup' && password !== confirmPassword) {
      setError('Passwords do not match.')
      return
    }

    setLoading(true)
    try {
      const payload = { email: email.trim(), password }
      const data = mode === 'signup' ? await registerUser(payload) : await loginUser(payload)
      setAuth({ token: data.access_token, userEmail: payload.email })
      clearForm()
      navigate('/chat', { replace: true })
    } catch (err) {
      const fallback = mode === 'signup' ? 'Unable to create account.' : 'Unable to sign in.'
      setError(getErrorMessage(err, fallback))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page home-page">
      <section className="hero-panel">
        <div className="hero-copy">
          <span className="eyebrow">RAG chatbot workspace</span>
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
          <div className="preview-card bottom">Generating answer with citations</div>
        </div>
      </section>

      <section className="dashboard-auth-panel glass-panel">
        <div className="auth-copy">
          <span className="eyebrow">Dashboard access</span>
          <h3>Use Sign In or Sign Up here to unlock the dashboard modules.</h3>
          <p>
            Authentication is integrated directly into the dashboard landing view, so your chat, documents,
            and quiz tools stay in one place.
          </p>
          {redirectedFromProtectedRoute && !authenticated ? (
            <p className="auth-notice">Please sign in or create an account to access protected pages.</p>
          ) : null}
        </div>

        {authenticated ? (
          <div className="auth-success">
            <span className="sidebar-label">Signed in</span>
            <h4>{userEmail || 'Authenticated user'}</h4>
            <p>Your dashboard is ready. Continue to chat, upload files, or generate quizzes.</p>
            <div className="hero-actions">
              <Link to="/chat" className="primary-link">Go to Chat</Link>
              <Link to="/quiz" className="secondary-link">Open Quiz</Link>
            </div>
          </div>
        ) : (
          <form className="auth-form" onSubmit={handleSubmit}>
            <div className="auth-switch">
              <button
                type="button"
                className={mode === 'signin' ? 'auth-tab active' : 'auth-tab'}
                onClick={() => handleModeSwitch('signin')}
              >
                Sign In
              </button>
              <button
                type="button"
                className={mode === 'signup' ? 'auth-tab active' : 'auth-tab'}
                onClick={() => handleModeSwitch('signup')}
              >
                Sign Up
              </button>
            </div>

            <label>
              Email
              <input
                type="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                placeholder="you@example.com"
                autoComplete="email"
              />
            </label>

            <label>
              Password
              <input
                type="password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                placeholder="Enter password"
                autoComplete={mode === 'signin' ? 'current-password' : 'new-password'}
              />
            </label>

            {mode === 'signup' ? (
              <label>
                Confirm password
                <input
                  type="password"
                  value={confirmPassword}
                  onChange={(event) => setConfirmPassword(event.target.value)}
                  placeholder="Confirm password"
                  autoComplete="new-password"
                />
              </label>
            ) : null}

            {error ? <p className="auth-error">{error}</p> : null}

            <button type="submit" className="auth-submit" disabled={loading}>
              {loading ? 'Please wait...' : mode === 'signup' ? 'Create Account' : 'Sign In'}
            </button>
          </form>
        )}
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
}

export default HomePage
