import { useCallback } from 'react'
import { generateQuiz } from '../services/quizService'
import { useQuizStore } from '../store/quizStore'

export const useQuiz = () => {
  const setQuiz = useQuizStore((s) => s.setQuiz)

  const generate = useCallback(
    async (topic, docIds) => {
      const q = await generateQuiz(
        topic,
        docIds
      )

      setQuiz(q)

      return q
    },
    [setQuiz]
  )

  return { generate }
}