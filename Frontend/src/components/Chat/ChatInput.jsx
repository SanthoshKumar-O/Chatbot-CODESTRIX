import React, { useState } from 'react'
import { useChat } from '../../hooks/useChat'
import { useChatStore } from '../../store/chatStore'

const ChatInput = () => {
  const [text, setText] = useState('')
  const { send } = useChat()
  const loading = useChatStore((s) => s.loading)

  const submit = async () => {
    if (!text.trim()) return
    await send(text)
    setText('')
  }

  return (
    <div className="chat-input-shell">
      <div className="chat-input">
        <textarea
          value={text}
          placeholder="Ask about your documents, request a quiz, or describe what you want to learn..."
          onChange={(e) => setText(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault()
              submit()
            }
          }}
        />
        <button disabled={loading} onClick={submit}>
          {loading ? 'Thinking…' : 'Send'}
        </button>
      </div>
      <div className="input-hints">
        <span>Enter to send</span>
        <span>Shift+Enter for a new line</span>
      </div>
    </div>
  )
}

export default ChatInput
