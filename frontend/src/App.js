import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [feedback, setFeedback] = useState(null);
  const [emailSent, setEmailSent] = useState(false);

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("jd", jd);

    try {
      const response = await axios.post("http://localhost:8000/upload/", formData);
      setFeedback(response.data);
      setEmailSent(true);
    } catch (error) {
      console.error("Upload failed", error);
      setEmailSent(false);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: 'Arial' }}>
      <h2>CV Feedback System</h2>
      <div style={{ marginBottom: 10 }}>
        <label>Upload Resume (.pdf or .docx): </label>
        <input type="file" accept=".pdf,.docx" onChange={(e) => setResume(e.target.files[0])} />
      </div>
      <div style={{ marginBottom: 10 }}>
        <label>Upload Job Description (.pdf or .docx): </label>
        <input type="file" accept=".pdf,.docx" onChange={(e) => setJd(e.target.files[0])} />
      </div>
      <button onClick={handleSubmit}>Submit</button>

      {emailSent && (
        <p style={{ color: 'green', marginTop: 10 }}>✅ Feedback email has been sent to the candidate.</p>
      )}

      {feedback && (
        <div style={{ marginTop: 20 }}>
          <h3>Feedback:</h3>
          <pre>{JSON.stringify(feedback, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default App;
