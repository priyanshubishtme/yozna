import { useState } from 'react';

export default function PDFViewer({ documentId }: { documentId: string }) {
  const [page, setPage] = useState(1);

  // Real implementation would use PDF.js to render PDF and overlay coordinates.
  return (
    <div className="flex flex-col h-full bg-gray-100 items-center justify-center p-4">
      <div className="bg-white shadow-lg w-full max-w-3xl aspect-[1/1.4] relative flex items-center justify-center border">
         <span className="text-gray-400">PDF Viewer Placeholder for Document {documentId} (Page {page})</span>
         {/* Simulated Highlight Box */}
         <div className="absolute top-[20%] left-[20%] w-[60%] h-[10%] bg-yellow-300/40 border-2 border-yellow-400"></div>
      </div>
      <div className="mt-4 flex space-x-4">
        <button className="px-4 py-2 bg-gray-200 rounded" onClick={() => setPage(p => Math.max(1, p-1))}>Prev</button>
        <span className="py-2">Page {page}</span>
        <button className="px-4 py-2 bg-gray-200 rounded" onClick={() => setPage(p => p+1)}>Next</button>
      </div>
    </div>
  );
}
