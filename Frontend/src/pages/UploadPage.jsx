import React from 'react'
import UploadBox from '../components/Documents/UploadBox'
import DocumentList from '../components/Documents/DocumentList'

const UploadPage = () => (
  <div className="page upload-page">
    <div className="split-layout">
      <UploadBox />
      <div className="glass-panel">
        <DocumentList />
      </div>
    </div>
  </div>
)

export default UploadPage
