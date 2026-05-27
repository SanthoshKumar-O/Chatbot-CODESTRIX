import { useCallback } from 'react'
import { generateQuiz } from '../services/quizService'
import { useQuizStore } from '../store/quizStore'

export const useQuiz = () => {
  const setQuiz = useQuizStore((s) => s.setQuiz)
  const addHistory = useQuizStore((s) => s.addHistory)

  const generate = useCallback(async (topic, docIds) => {
    const q = await generateQuiz(topic, docIds)
    setQuiz(q)
    addHistory({
      id: q.quizId || crypto.randomUUID(),
      topic: q.topic || topic,
      score: 0,
      total: q.questions?.length || 0,
      createdAt: new Date().toISOString(),
    })
    return q
  }, [setQuiz, addHistory])

  return { generate }
}
