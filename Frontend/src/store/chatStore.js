import { create } from 'zustand'
import { persist } from 'zustand/middleware'

const starterMessages = [
  {
    role: 'assistant',
    text: 'Ask me about your documents, generate a quiz, or build a study roadmap.',
    sources: [],
    thinking: ['Ready to help'],
  },
]

export const useChatStore = create(
  persist(
    (set) => ({
      messages: starterMessages,
      loading: false,
      sessionId: crypto.randomUUID(),
      addMessage: (msg) => set((s) => ({ messages: [...s.messages, msg] })),
      setLoading: (v) => set({ loading: v }),
      setSessionId: (id) => set({ sessionId: id }),
      reset: () => set({ messages: starterMessages, loading: false, sessionId: crypto.randomUUID() }),
    }),
    { name: 'codestrix-chat' },
  ),
)
