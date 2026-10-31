import { BrowserRouter, Routes, Route } from 'react-router';
import Landing from './pages/Landing';
import Chat from './pages/Chat';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/app/chat" element={<Chat />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
