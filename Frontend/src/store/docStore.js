import { create } from "zustand";

export const useDocStore = create((set) => ({
  documents: [],
  uploading: false,

  setDocuments: (docs) =>
    set({ documents: docs }),

  setUploading: (v) =>
    set({ uploading: v }),

  addDocument: (doc) =>
    set((s) => ({
      documents: [...s.documents, doc],
    })),
}));