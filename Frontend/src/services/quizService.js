import { api } from "./api";

const buildQuiz = (topic) => ({
  quizId: crypto.randomUUID(),
  topic: topic || "Core Concepts",
  questions: [
    {
      id: 1,
      question: `Which statement best describes ${topic || "the topic"}?`,
      options: ["A broad overview", "A narrow detail", "A random fact", "A file upload"],
      correctAnswer: 0,
    },
    {
      id: 2,
      question: "What helps long-term retention most?",
      options: ["Passive rereading", "Active recall", "Skipping review", "Only watching videos"],
      correctAnswer: 1,
    },
    {
      id: 3,
      question: "What should a good RAG answer include?",
      options: ["Sources", "Nothing but text", "Only emojis", "No citations"],
      correctAnswer: 0,
    },
  ],
});

export const generateQuiz = async (topic, docIds = []) => {
  if (import.meta.env.VITE_USE_BACKEND !== "true") {
    return buildQuiz(topic);
  }

  const res = await api.post("/quiz/generate", { topic, docIds });
  return res.data;
};

export const submitQuizResults = async (quizId, answers) => {
  if (import.meta.env.VITE_USE_BACKEND !== "true") {
    return { quizId, answers, submitted: true };
  }

  const res = await api.post(`/quiz/${quizId}/submit`, { answers });
  return res.data;
};
