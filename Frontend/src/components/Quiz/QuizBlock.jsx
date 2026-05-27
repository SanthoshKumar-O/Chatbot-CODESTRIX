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

  const currentQuestion = useMemo(() => quiz?.questions?.[currentIndex], [quiz, currentIndex])
  const completed = quiz && currentIndex >= quiz.questions.length

  const startQuiz = async () => {
    setLoading(true)
    try {
      const nextQuiz = await generateQuiz(topic, [])
      setQuiz(nextQuiz)
      addHistory({
        id: nextQuiz.quizId,
        topic: nextQuiz.topic,
        score: 0,
        total: nextQuiz.questions.length,
        createdAt: new Date().toISOString(),
      })
    } finally {
      setLoading(false)
    }
  }

  const submitAnswer = () => {
    if (!currentQuestion || selected === null) return
    const correct = selected === currentQuestion.correctAnswer
    answerQuestion(correct)
  }

  if (!quiz) {
    return (
      <div className="quiz-block empty">
        <span className="eyebrow">Quiz</span>
        <h2>Generate a quiz from your current topic</h2>
        <p>Use active recall to test understanding of uploaded documents or a learning goal.</p>
        <div className="quiz-controls">
          <input value={topic} onChange={(e) => setTopic(e.target.value)} placeholder="Enter a topic" />
          <button onClick={startQuiz} disabled={loading}>{loading ? 'Generating…' : 'Generate Quiz'}</button>
        </div>
      </div>
    )
  }

  if (completed) {
    return (
      <div className="quiz-block result">
        <span className="eyebrow">Quiz Result</span>
        <h2>{quiz.topic}</h2>
        <div className="result-stat">
          <strong>{score}</strong>
          <span>correct answers</span>
        </div>
        <button onClick={() => { resetQuiz(); startQuiz(); }}>Retry Quiz</button>
        <button className="ghost" onClick={resetQuiz}>Clear</button>
      </div>
    )
  }

  return (
    <div className="quiz-block">
      <div className="quiz-head">
        <div>
          <span className="eyebrow">Quiz Mode</span>
          <h2>{quiz.topic}</h2>
        </div>
        <div className="status-pill active">{currentIndex + 1}/{quiz.questions.length}</div>
      </div>

      <div className="quiz-question">{currentQuestion.question}</div>

      <div className="quiz-options">
        {currentQuestion.options.map((option, index) => {
          const isSelected = selected === index
          const isCorrect = answered && index === currentQuestion.correctAnswer
          const isWrong = answered && isSelected && index !== currentQuestion.correctAnswer
          return (
            <button
              key={option}
              className={`quiz-option ${isSelected ? 'selected' : ''} ${isCorrect ? 'correct' : ''} ${isWrong ? 'wrong' : ''}`}
              onClick={() => selectAnswer(index)}
              disabled={answered}
            >
              {option}
            </button>
          )
        })}
      </div>

      <div className="quiz-actions">
        {!answered ? (
          <button onClick={submitAnswer} disabled={selected === null}>Submit</button>
        ) : (
          <button onClick={nextQuestion}>Next Question</button>
        )}
        <button className="ghost" onClick={() => { selectAnswer(null); setAnswered(false); }}>Reset Choice</button>
      </div>
    </div>
  )
}

export default QuizBlock
