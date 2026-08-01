function LoadingSpinner() {
  return (
    <div className="mt-10 text-center">
      <div className="inline-flex items-center gap-3 bg-slate-800 px-6 py-4 rounded-xl">
        <div className="w-4 h-4 rounded-full bg-blue-500 animate-pulse"></div>

        <p className="text-slate-300">
          The Contrarian is thinking...
        </p>
      </div>
    </div>
  );
}

export default LoadingSpinner;