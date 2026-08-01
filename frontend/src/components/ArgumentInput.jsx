function ArgumentInput({ argument, setArgument, handleSubmit }) {
  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="bg-slate-800/60 backdrop-blur-md border border-slate-700 rounded-2xl p-5">

      <label className="block text-slate-300 font-semibold mb-3">
        Enter your opinion
      </label>

      <textarea
        value={argument}
        onChange={(e) => setArgument(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Example: AI will replace all programmers..."
        className="w-full h-44 bg-transparent resize-none outline-none text-lg placeholder:text-slate-500"
      />

      <p className="text-xs text-slate-500 mt-3">
        Press <strong>Enter</strong> to submit • <strong>Shift + Enter</strong> for a new line
      </p>

    </div>
  );
}

export default ArgumentInput;