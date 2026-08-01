function SubmitButton({ loading, handleSubmit, handleClear }) {
  return (
    <div className="flex justify-center gap-4 mt-8">

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="
          px-10 py-4
          rounded-2xl
          bg-blue-600
          hover:bg-blue-700
          disabled:bg-slate-700
          transition-all
          duration-300
          shadow-lg
          hover:shadow-blue-500/30
          font-semibold
          text-lg
        "
      >
        {loading ? "🧠 Thinking..." : "🚀 Challenge My Opinion"}
      </button>

      <button
        onClick={handleClear}
        className="
          px-8 py-4
          rounded-2xl
          bg-slate-700
          hover:bg-slate-600
          transition-all
          duration-300
          font-semibold
          text-lg
        "
      >
        🗑 Clear
      </button>

    </div>
  );
}

export default SubmitButton;