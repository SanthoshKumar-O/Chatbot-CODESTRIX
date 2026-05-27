import { api } from "./api";

const USE_BACKEND = import.meta.env.VITE_USE_BACKEND === "true";

const buildLocalResponse = (message) => {
  const lower = message.toLowerCase();
  const sources = [
    { name: "project-notes.pdf", chunk: 3 },
    { name: "course-outline.txt", chunk: 7 },
  ];

  let response = "I can help with that. Upload documents, ask a follow-up, or generate a quiz from the current topic.";

  if (lower.includes("roadmap") || lower.includes("learn")) {
    response = "A good path is: fundamentals, guided practice, then one project per topic. I can turn this into a weekly roadmap if you want.";
  } else if (lower.includes("quiz")) {
    response = "I can generate a quick quiz from the current topic or your uploaded notes. Pick a topic and I will draft questions.";
  } else if (lower.includes("upload") || lower.includes("document")) {
    response = "Upload PDFs or notes in the Documents tab so I can include them in answers and quizzes.";
  }

  return {
    response,
    sources,
    thinking: ["Searching documents...", "Ranking chunks...", "Generating answer..."],
    mode: "demo",
  };
};

export const sendMessage = async (message, sessionId) => {
  if (USE_BACKEND && sessionId) {
    try {
      const res = await api.post("/chat/stream", {
        session_id: sessionId,
        message,
      });
      return {
        response: res.data.response || res.data.answer || "",
        sources: res.data.sources || [],
        thinking: res.data.thinking || [],
        mode: "backend",
      };
    } catch (error) {
      console.warn("Backend chat unavailable, falling back to demo mode.", error);
    }
  }

  return buildLocalResponse(message);
};

export const streamMessage = (message, sessionId, onChunk) => {
  return sendMessage(message, sessionId, onChunk);
};
