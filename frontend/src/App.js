import React, { useState } from 'react';
import './App.css';
import VideoUpload from './components/VideoUpload';
import VideoList from './components/VideoList';

function App() {
  const [videos, setVideos] = useState([]);

  const handleVideoUpload = (video) => {
    setVideos([...videos, video]);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Polar Bear Adoption Tracker</h1>
      </header>
      <main>
        <VideoUpload onUpload={handleVideoUpload} />
        <VideoList videos={videos} />
      </main>
    </div>
  );
}

export default App;