import { Link } from 'react-router';

export default function Landing() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4">
      <h1 className="text-4xl font-bold mb-4 text-blue-900">Yojana Sahayak</h1>
      <p className="text-lg text-gray-700 mb-8">AI Government Scheme Intelligence Platform</p>
      <div className="space-x-4">
        <Link to="/app" className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">Discover My Schemes</Link>
        <Link to="/app/chat" className="bg-white text-blue-600 border border-blue-600 px-6 py-3 rounded-lg hover:bg-blue-50 transition">Ask AI Assistant</Link>
      </div>
    </div>
  );
}
