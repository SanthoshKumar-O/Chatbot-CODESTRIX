import { api } from './api'

export const createSession = async () => {
  const res = await api.post('/sessions/')
  return res.data
}

export const getSessions = async () => {
  const res = await api.get('/sessions/')
  return res.data
}

export const deleteSession = async (sessionId) => {
  await api.delete(`/sessions/${sessionId}/`)
}