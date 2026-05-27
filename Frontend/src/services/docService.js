import { api } from "./api";

const STORAGE_KEY = "codestrix_documents";

const readLocalDocs = () => {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
};

const writeLocalDocs = (docs) => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(docs));
};

export const uploadDocument = async (file) => {
  if (import.meta.env.VITE_USE_BACKEND !== "true") {
    const docs = readLocalDocs();
    const next = [
      ...docs,
      {
        id: crypto.randomUUID(),
        name: file.name,
        uploadedAt: new Date().toISOString(),
        size: file.size,
        status: "Ready",
      },
    ];
    writeLocalDocs(next);
    return next[next.length - 1];
  }

  const formData = new FormData();
  formData.append("file", file);

  const res = await api.post("/documents/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return res.data;
};

export const listDocuments = async () => {
  if (import.meta.env.VITE_USE_BACKEND !== "true") {
    return readLocalDocs();
  }

  const res = await api.get("/documents");
  return res.data.documents || res.data;
};
