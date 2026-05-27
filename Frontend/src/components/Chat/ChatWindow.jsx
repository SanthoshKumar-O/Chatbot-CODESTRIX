import React, { useEffect, useRef } from 'react'
import { useChatStore } from '../../store/chatStore'
import MessageBubble from './MessageBubble'

const ChatWindow = () => {
  const messages = useChatStore((s) => s.messages)
  const loading = useChatStore((s) => s.loading)
  const ref = useRef()

  useEffect(() => {
    if (ref.current) ref.current.scrollTop = ref.current.scrollHeight
  }, [messages])

  return (
    <div className="chat-window" ref={ref}>
      <div className="chat-window-header">
        <div>
          <span className="eyebrow">RAG Learning Assistant</span>
          <h2>Ask, retrieve, and quiz from one workspace</h2>
        </div>
        <div className={`status-pill ${loading ? 'active' : ''}`}>
          {loading ? 'Thinking...' : 'Ready'}
        </div>
      </div>

      <div className="chat-feed">
        {messages.map((m, i) => (
          <MessageBubble key={`${m.role}-${i}`} message={m} />
        ))}
      </div>
    </div>
  )
}

export default ChatWindow
