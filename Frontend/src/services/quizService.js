import { api } from "./api";

export const generateQuiz = async (
  topic,
  docIds = []
) => {
  try {
    const res = await api.post(
      "/quiz/generate",
      {
        topic,
        docIds,
      }
    );

    return res.data;
  } catch (error) {
    console.error("Quiz generation failed:", error);

    return {
      quizId: null,
      topic,
      questions: [],
    };
  }
};

export const submitQuizResults = async (
  quizId,
  answers
) => {
  const res = await api.post(
    `/quiz/${quizId}/submit`,
    {
      answers,
    }
  );

  return res.data;
};