import React from 'react'
import ChatWindow from '../components/Chat/ChatWindow'
import ChatInput from '../components/Chat/ChatInput'

const ChatPage = () => {
  return (
    <div className="page chat-page">
      <div className="chat-panel glass-panel">
        <div className="panel-grid">
          <div className="panel-stack">
            <div className="mini-card">
              <span className="eyebrow">Live flow</span>
              <h3>Thinking state, sources, and direct replies</h3>
              <p>The UI is now structured for source-backed chat responses and can fall back to demo mode if the backend is offline or not authenticated.</p>
            </div>
          </div>
        </div>
        <ChatWindow />
        <ChatInput />
      </div>
    </div>
  )
}

export default ChatPage
