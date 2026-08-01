function ChatHistory({ history }) {
  if (history.length === 0) return null;

  return (
    <div className="mt-10 space-y-4">

      <h2 className="text-2xl font-bold">
        Conversation History
      </h2>

      {history.map((message, index) => (
        <div
          key={index}
          className={`p-4 rounded-2xl ${
            message.role === "user"
              ? "bg-blue-900/40 border border-blue-700"
              : "bg-slate-800 border border-slate-700"
          }`}
        >
          <p className="text-sm text-slate-400 mb-2">
            {message.role === "user" ? "👤 You" : "🧠 The Contrarian"}
          </p>

          <p className="whitespace-pre-wrap">
            {message.content}
          </p>

        </div>
      ))}

    </div>
  );
}

export default ChatHistory;