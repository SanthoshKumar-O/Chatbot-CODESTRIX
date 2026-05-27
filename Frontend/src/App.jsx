import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Sidebar from './components/Sidebar/Sidebar'
import HomePage from './pages/HomePage'
import ChatPage from './pages/ChatPage'
import UploadPage from './pages/UploadPage'
import QuizPage from './pages/QuizPage'

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
            <Route path="/chat" element={<ChatPage />} />
            <Route path="/upload" element={<UploadPage />} />
            <Route path="/quiz" element={<QuizPage />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}


