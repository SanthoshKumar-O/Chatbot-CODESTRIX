import React, { useMemo, useState } from 'react'
import { generateQuiz } from '../../services/quizService'
import { useQuizStore } from '../../store/quizStore'

const QuizBlock = () => {
  const quiz = useQuizStore((s) => s.quiz)
  const currentIndex = useQuizStore((s) => s.currentIndex)
  const score = useQuizStore((s) => s.score)
  const selected = useQuizStore((s) => s.selected)
  const answered = useQuizStore((s) => s.answered)

  const setQuiz = useQuizStore((s) => s.setQuiz)
  const selectAnswer = useQuizStore((s) => s.selectAnswer)
  const answerQuestion = useQuizStore((s) => s.answerQuestion)
  const nextQuestion = useQuizStore((s) => s.nextQuestion)
  const setAnswered = useQuizStore((s) => s.setAnswered)
  const resetQuiz = useQuizStore((s) => s.resetQuiz)
  const addHistory = useQuizStore((s) => s.addHistory)

  const [topic, setTopic] = useState('Artificial Intelligence')
  const [loading, setLoading] = useState(false)

  const currentQuestion = useMemo(
    () => quiz?.questions?.[currentIndex],
    [quiz, currentIndex]
  )

  const completed =
    quiz &&
    quiz.questions &&
    currentIndex >= quiz.questions.length

  const startQuiz = async () => {
    if (!topic.trim() || loading) return

    setLoading(true)

    try {
      const nextQuiz = await generateQuiz(topic, [])

      if (
        !nextQuiz ||
        !nextQuiz.questions ||
        !Array.isArray(nextQuiz.questions)
      ) {
        throw new Error('Invalid quiz response')
      }

      setQuiz(nextQuiz)
    } catch (error) {
      console.error('Quiz generation failed:', error)
    } finally {
      setLoading(false)
    }
  }

  const submitAnswer = () => {
    if (!currentQuestion || selected === null) return

    const correct =
      selected === currentQuestion.correctAnswer

    answerQuestion(correct)
  }

  const finishQuiz = () => {
    if (!quiz) return

    addHistory({
      id: quiz.quizId,
      topic: quiz.topic,
      score,
      total: quiz.questions.length,
      createdAt: new Date().toISOString(),
    })

    resetQuiz()
  }

  if (!quiz) {
    return (
      <div className="quiz-block empty">
        <span className="eyebrow">Quiz</span>

        <h2>
          Generate a quiz from your current topic
        </h2>

        <p>
          Test understanding using active recall
          powered by your uploaded documents.
        </p>

        <div className="quiz-controls">
          <input
            value={topic}
            onChange={(e) =>
              setTopic(e.target.value)
            }
            placeholder="Enter a topic"
          />

          <button
            onClick={startQuiz}
            disabled={loading}
          >
            {loading
              ? 'Generating…'
              : 'Generate Quiz'}
          </button>
        </div>
      </div>
    )
  }

  if (completed) {
    return (
      <div className="quiz-block result">
        <span className="eyebrow">
          Quiz Result
        </span>

        <h2>{quiz.topic}</h2>

        <div className="result-stat">
          <strong>{score}</strong>
          <span>
            out of {quiz.questions.length}
          </span>
        </div>

        <div className="quiz-actions">
          <button
            onClick={() => {
              finishQuiz()
              startQuiz()
            }}
          >
            Retry Quiz
          </button>

          <button
            className="ghost"
            onClick={finishQuiz}
          >
            Clear
          </button>
        </div>
      </div>
    )
  }

  if (!currentQuestion) {
    return (
      <div className="quiz-block">
        Failed to load question.
      </div>
    )
  }

  return (
    <div className="quiz-block">
      <div className="quiz-head">
        <div>
          <span className="eyebrow">
            Quiz Mode
          </span>

          <h2>{quiz.topic}</h2>
        </div>

        <div className="status-pill active">
          {currentIndex + 1}/
          {quiz.questions.length}
        </div>
      </div>

      <div className="quiz-question">
        {currentQuestion.question}
      </div>

      <div className="quiz-options">
        {currentQuestion.options?.map(
          (option, index) => {
            const isSelected =
              selected === index

            const isCorrect =
              answered &&
              index ===
                currentQuestion.correctAnswer

            const isWrong =
              answered &&
              isSelected &&
              index !==
                currentQuestion.correctAnswer

            return (
              <button
                key={option}
                className={`quiz-option ${
                  isSelected ? 'selected' : ''
                } ${
                  isCorrect ? 'correct' : ''
                } ${isWrong ? 'wrong' : ''}`}
                onClick={() =>
                  selectAnswer(index)
                }
                disabled={answered}
              >
                {option}
              </button>
            )
          }
        )}
      </div>

      <div className="quiz-actions">
        {!answered ? (
          <button
            onClick={submitAnswer}
            disabled={selected === null}
          >
            Submit
          </button>
        ) : (
          <button onClick={nextQuestion}>
            Next Question
          </button>
        )}

        <button
          className="ghost"
          onClick={() => {
            selectAnswer(null)
            setAnswered(false)
          }}
        >
          Reset Choice
        </button>
      </div>
    </div>
  )
}

export default QuizBlock