import React from 'react'
import QuizBlock from '../components/Quiz/QuizBlock'

const QuizPage = () => (
  <div className="page quiz-page split-layout">
    <div className="glass-panel quiz-edu-card">
      <span className="eyebrow">Learning mode</span>
      <h2>Quiz mode turns your notes into active recall.</h2>
      <p>Use this block to test understanding after chatting with the model or uploading study material.</p>
      <ul>
        <li>Multiple-choice questions</li>
        <li>Quiz history</li>
        <li>Demo fallback when the backend is offline</li>
      </ul>
    </div>
    <QuizBlock />
  </div>
)

export default QuizPage
