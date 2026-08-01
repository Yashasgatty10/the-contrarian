function Header() {
  return (
    <div className="text-center mb-12 animate-fade-in">

      <div className="inline-flex items-center gap-3 bg-slate-800/60 backdrop-blur-md border border-slate-700 rounded-full px-5 py-2 mb-6">

        <span className="text-2xl">🧠</span>

        <span className="text-blue-400 font-semibold tracking-wide">
          AI Critical Thinking Assistant
        </span>

      </div>

      <h1 className="text-6xl md:text-7xl font-extrabold">
        The Contrarian
      </h1>

      <p className="text-slate-300 text-xl mt-5 max-w-2xl mx-auto">
        Challenge assumptions. Detect biases. Explore stronger perspectives with AI-powered reasoning.
      </p>

    </div>
  );
}

export default Header;