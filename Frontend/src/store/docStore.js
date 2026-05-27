import { create } from 'zustand'
import { persist } from 'zustand/middleware'

export const useDocStore = create(
  persist(
    (set) => ({
      documents: [],
      uploading: false,
      setDocuments: (docs) => set({ documents: docs }),
      setUploading: (v) => set({ uploading: v }),
      addDocument: (doc) => set((s) => ({ documents: [...s.documents, doc] })),
    }),
    { name: 'codestrix-docs' },
  ),
)
