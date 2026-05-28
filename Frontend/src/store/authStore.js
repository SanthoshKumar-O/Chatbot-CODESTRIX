import { create } from 'zustand'
import { persist } from 'zustand/middleware'

const STORAGE_KEY = 'codestrix_token'

export const useAuthStore = create(
  persist(
    (set) => ({
      token: localStorage.getItem(STORAGE_KEY) || '',
      userEmail: '',
      authenticated: Boolean(localStorage.getItem(STORAGE_KEY)),
      setAuth: ({ token, userEmail }) => {
        localStorage.setItem(STORAGE_KEY, token)
        set({ token, userEmail, authenticated: true })
      },
      clearAuth: () => {
        localStorage.removeItem(STORAGE_KEY)
        set({ token: '', userEmail: '', authenticated: false })
      },
    }),
    {
      name: 'codestrix-auth',
      partialize: (state) => ({
        token: state.token,
        userEmail: state.userEmail,
        authenticated: state.authenticated,
      }),
    },
  ),
)
