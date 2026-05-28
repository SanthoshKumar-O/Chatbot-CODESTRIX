import './App.css'
import { BrowserRouter, Navigate, Routes, Route } from 'react-router-dom'
import Sidebar from './components/Sidebar/Sidebar'
import HomePage from './pages/HomePage'
import ChatPage from './pages/ChatPage'
import UploadPage from './pages/UploadPage'
import QuizPage from './pages/QuizPage'
import { useAuthStore } from './store/authStore'

const ProtectedRoute = ({ children }) => {
  const authenticated = useAuthStore((s) => s.authenticated)

  if (!authenticated) {
    return <Navigate to="/" replace state={{ authRequired: true }} />
  }

  return children
}

export default function App() {
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


