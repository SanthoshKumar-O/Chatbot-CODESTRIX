import { useCallback } from 'react'
import { sendMessage } from '../services/chatService'
import { useChatStore } from '../store/chatStore'

export const useChat = () => {
  const addMessage = useChatStore((s) => s.addMessage)
  const setLoading = useChatStore((s) => s.setLoading)
  const sessionId = useChatStore((s) => s.sessionId)

  const send = useCallback(async (text) => {
    setLoading(true)
    addMessage({ role: 'user', text })
    try {
      const data = await sendMessage(text, sessionId)
      addMessage({
        role: 'assistant',
        text: data.response || data.text || '',
        sources: data.sources || [],
        thinking: data.thinking || [],
        mode: data.mode || 'demo',
      })
    } finally {
      setLoading(false)
    }
  }, [addMessage, setLoading, sessionId])

  return { send }
}
