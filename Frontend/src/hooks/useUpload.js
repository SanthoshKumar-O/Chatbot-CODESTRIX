import { useCallback } from 'react'
import { uploadDocument, listDocuments } from '../services/docService'
import { useDocStore } from '../store/docStore'

export const useUpload = () => {
  const setUploading = useDocStore((s) => s.setUploading)
  const setDocuments = useDocStore((s) => s.setDocuments)
  const addDocument = useDocStore((s) => s.addDocument)

  const upload = useCallback(async (file) => {
    setUploading(true)
    try {
      const res = await uploadDocument(file)
      const docs = await listDocuments()
      setDocuments(docs)
      if (res?.id) {
        addDocument(res)
      }
      return res
    } finally {
      setUploading(false)
    }
  }, [setUploading, setDocuments, addDocument])

  return { upload }
}
