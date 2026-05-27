import React, { useRef } from 'react'
import { useUpload } from '../../hooks/useUpload'
import { useDocStore } from '../../store/docStore'

const UploadBox = () => {
  const inputRef = useRef()
  const { upload } = useUpload()
  const uploading = useDocStore((s) => s.uploading)

  const onFile = async (e) => {
    const file = e.target.files[0]
    if (!file) return
    await upload(file)
  }

  return (
    <div className="upload-box">
      <div className="upload-hero">
        <span className="eyebrow">Documents</span>
        <h2>Drop files in to build your knowledge base</h2>
        <p>PDFs, notes, and study guides are stored locally in demo mode and can be connected to your backend when ready.</p>
      </div>
      <input type="file" ref={inputRef} onChange={onFile} />
      <button onClick={() => inputRef.current && inputRef.current.click()} disabled={uploading}>
        {uploading ? 'Uploading…' : 'Select File'}
      </button>
    </div>
  )
}

export default UploadBox
