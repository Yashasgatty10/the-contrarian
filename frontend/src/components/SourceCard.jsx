function SourceCard({ source }) {
  return (
    <div className="rounded-2xl border border-slate-600 bg-slate-900/50 backdrop-blur-sm p-5 hover:border-blue-500 transition-all duration-300">

      <div className="flex justify-between items-start">

        <h4 className="font-bold text-lg">
          {source.title}
        </h4>

        <span className="text-xs bg-blue-600 px-2 py-1 rounded-full">
          {source.type}
        </span>

      </div>

      <div className="mt-4">

        <p className="text-sm text-slate-400">
          Similarity Score
        </p>

        <p className="text-blue-400 font-semibold">
          {source.score}
        </p>

      </div>

    </div>
  );
}

export default SourceCard;