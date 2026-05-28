import { api } from "./api";

export const sendMessage = async (message, sessionId) => {
  try {
    const res = await api.post("/chat", {
      message,
      session_id: sessionId,
    });

    return {
      response: res.data.response,
      sources: res.data.sources || [],
      thinking: res.data.thinking || [],
      mode: "backend",
    };
  } catch (error) {
    console.error("Chat API Error:", error);

    return {
      response: "Backend connection failed.",
      sources: [],
      thinking: [],
      mode: "error",
    };
  }
};

export const streamMessage = async (
  message,
  sessionId,
  onChunk
) => {
  const result = await sendMessage(message, sessionId);

  if (onChunk) {
    onChunk(result.response);
  }

  return result;
};