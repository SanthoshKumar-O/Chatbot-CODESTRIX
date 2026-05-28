import './App.css'
import { BrowserRouter, Navigate, Routes, Route } from 'react-router-dom'
import Sidebar from './components/Sidebar/Sidebar'
import HomePage from './pages/HomePage'
import ChatPage from './pages/ChatPage'
import UploadPage from './pages/UploadPage'
import QuizPage from './pages/QuizPage'
import { useEffect } from 'react'
import { createSession } from './services/sessionService'
import { useChatStore } from './store/chatStore'
export default function App() {
  const sessionId = useChatStore((s) => s.sessionId)
  const setSessionId = useChatStore((s) => s.setSessionId)
  useEffect(() => {
  const initSession = async () => {
    if (sessionId) return

    try {
      const session = await createSession()

      if (session?.id) {
        setSessionId(session.id)
      }
    } catch (error) {
      console.error(
        'Failed to create session:',
        error
      )
    }
  }

  initSession()
}, [sessionId, setSessionId])
  return (
    <BrowserRouter future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
      <div className="container">
        <div className="topbar">
          <div className="brand-title">Codestrix · Learning Chat</div>
        </div>
        <Sidebar />
        <main className="main">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route
              path="/chat"
              element={(
                <ProtectedRoute>
                  <ChatPage />
                </ProtectedRoute>
              )}
            />
            <Route
              path="/upload"
              element={(
                <ProtectedRoute>
                  <UploadPage />
                </ProtectedRoute>
              )}
            />
            <Route
              path="/quiz"
              element={(
                <ProtectedRoute>
                  <QuizPage />
                </ProtectedRoute>
              )}
            />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}


