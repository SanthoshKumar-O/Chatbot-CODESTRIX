import React, { useEffect } from 'react'
import { useDocStore } from '../../store/docStore'
import { listDocuments } from '../../services/docService'
import { formatTime } from '../../utils/formatTime'

const DocumentList = () => {
  const documents = useDocStore((s) => s.documents)
  const setDocuments = useDocStore((s) => s.setDocuments)

  useEffect(() => {
    const load = async () => {
      const docs = await listDocuments()
      setDocuments(docs)
    }
    load()
  }, [setDocuments])

  return (
    <div className="document-list">
      <div className="section-title-block">
        <span className="eyebrow">Library</span>
        <h3>Available documents</h3>
      </div>
      {documents.length === 0 && <div className="empty-state">No documents yet. Upload a file to start retrieving from it.</div>}
      {documents.map((d) => (
        <div key={d.id} className="doc-item">
          <div className="doc-name">{d.name}</div>
          <div className="doc-meta">
            <span>{formatTime(d.uploadedAt)}</span>
            <span>{d.status || 'Indexed'}</span>
          </div>
        </div>
      ))}
    </div>
  )
}

export default DocumentList
