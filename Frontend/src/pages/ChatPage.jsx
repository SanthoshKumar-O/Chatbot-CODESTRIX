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
              <p>
  Ask questions, retrieve relevant document chunks,
  and receive source-backed answers from your
  knowledge base.
</p>
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
