import { useCallback } from 'react'
import { sendMessage } from '../services/chatService'
import { useChatStore } from '../store/chatStore'

export const useChat = () => {
  const addMessage = useChatStore((s) => s.addMessage)
  const setLoading = useChatStore((s) => s.setLoading)
  const sessionId = useChatStore((s) => s.sessionId)

  const send = useCallback(
    async (text) => {
      if (!text.trim()) return

      setLoading(true)

      addMessage({
        role: 'user',
        text,
      })

      try {
        const data = await sendMessage(
          text,
          sessionId
        )

        addMessage({
          role: 'assistant',
          text: data.response || '',
          sources: data.sources || [],
          thinking: data.thinking || [],
          mode: 'backend',
        })
      } catch (error) {
        console.error(
          'Chat request failed:',
          error
        )

        addMessage({
          role: 'assistant',
          text:
            'Failed to connect to backend.',
          sources: [],
          thinking: [],
          mode: 'error',
        })
      } finally {
        setLoading(false)
      }
    },
    [addMessage, setLoading, sessionId]
  )

  return { send }
}