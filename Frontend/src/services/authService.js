import { api } from './api'

export const registerUser = async ({ email, password }) => {
  const res = await api.post('/auth/register', { email, password })
  return res.data
}

export const loginUser = async ({ email, password }) => {
  const payload = new URLSearchParams()
  payload.set('username', email)
  payload.set('password', password)

  const res = await api.post('/auth/login', payload, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  })
  return res.data
}
