import { useCallback } from 'react'
import {
  uploadDocument,
  listDocuments,
} from '../services/docService'

import { useDocStore } from '../store/docStore'

export const useUpload = () => {
  const setUploading = useDocStore(
    (s) => s.setUploading
  )

  const setDocuments = useDocStore(
    (s) => s.setDocuments
  )

  const upload = useCallback(
    async (file) => {
      setUploading(true)

      try {
        const res = await uploadDocument(file)

        const docs =
          await listDocuments()

        setDocuments(docs)

        return res
      } catch (error) {
        console.error(
          'Upload failed:',
          error
        )

        throw error
      } finally {
        setUploading(false)
      }
    },
    [setUploading, setDocuments]
  )

  return { upload }
}