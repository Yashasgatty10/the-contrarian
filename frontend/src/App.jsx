import { useState } from "react";
import api from "./services/api";

import Header from "./components/Header";
import ArgumentInput from "./components/ArgumentInput";
import SubmitButton from "./components/SubmitButton";
import ResponseCard from "./components/ResponseCard";
import LoadingSpinner from "./components/LoadingSpinner";
import ChatHistory from "./components/ChatHistory";

function App() {
  const [argument, setArgument] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  const handleSubmit = async () => {
    if (!argument.trim()) return;

    setLoading(true);
    setResponse(null);

    try {
      const res = await api.post("/debate", {
        argument,
        history,
      });

      setResponse(res.data);

      setHistory((prev) => [
        ...prev,
        {
          role: "user",
          content: argument,
        },
        {
          role: "assistant",
          content: res.data.rebuttal,
        },
      ]);
    } catch (err) {
      console.error("Axios Error:", err);

      let errorMessage = "Unknown error";

      if (err.response) {
        // Backend responded with an error
        errorMessage =
          err.response.data?.detail ||
          `Server Error (${err.response.status})`;
      } else if (err.request) {
        // Request made but no response
        errorMessage =
          "Backend did not respond. It may be sleeping or unavailable.";
      } else {
        // Axios setup error
        errorMessage = err.message;
      }

      setResponse({
        rebuttal: `❌ ${errorMessage}`,
        sources: [],
      });
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setArgument("");
    setResponse(null);
    setHistory([]);
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white px-6 py-12">
      <div className="max-w-4xl mx-auto">
        <Header />

        <ArgumentInput
          argument={argument}
          setArgument={setArgument}
          handleSubmit={handleSubmit}
        />

        <SubmitButton
          loading={loading}
          handleSubmit={handleSubmit}
          handleClear={handleClear}
        />

        {loading ? (
          <LoadingSpinner />
        ) : (
          <>
            <ResponseCard response={response} />
            <ChatHistory history={history} />
          </>
        )}
      </div>
    </div>
  );
}

export default App;