import ChatInterface from '../components/ChatInterface';

export default function Chat() {
  return (
    <div className="flex h-screen bg-white text-gray-900">
      <div className="flex-1 overflow-hidden">
        <ChatInterface />
      </div>
    </div>
  );
}
