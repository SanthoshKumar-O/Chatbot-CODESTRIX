import React, { useRef } from 'react'
import { useUpload } from '../../hooks/useUpload'
import { useDocStore } from '../../store/docStore'

const UploadBox = () => {
  const inputRef = useRef()
  const { upload } = useUpload()

  const uploading = useDocStore((s) => s.uploading)

  const onFile = async (e) => {
    const file = e.target.files[0]

    if (!file || uploading) return

    await upload(file)

    e.target.value = ''
  }

  return (
    <div className="upload-box">
      <div className="upload-hero">
        <span className="eyebrow">Documents</span>

        <h2>
          Drop files in to build your knowledge base
        </h2>

        <p>
          Upload PDFs, notes, and study guides to
          power retrieval, summaries, and quiz
          generation.
        </p>
      </div>

      <input
        type="file"
        ref={inputRef}
        onChange={onFile}
        accept=".pdf,.txt,.doc,.docx"
        style={{ display: 'none' }}
      />

      <button
        onClick={() =>
          inputRef.current &&
          inputRef.current.click()
        }
        disabled={uploading}
      >
        {uploading ? 'Uploading…' : 'Select File'}
      </button>
    </div>
  )
}

export default UploadBox;