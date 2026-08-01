import ReactMarkdown from "react-markdown";
import SourceCard from "./SourceCard";

function ResponseCard({ response }) {

  const copyResponse = () => {
    navigator.clipboard.writeText(response.rebuttal);
    alert("Response copied!");
  };

  if (!response) return null;

  return (
    <div className="mt-12 rounded-3xl border border-slate-700 bg-slate-800/60 backdrop-blur-md p-8 shadow-2xl">

      <div className="flex justify-between items-center mb-6">

        <h2 className="text-3xl font-bold">
          AI Response
        </h2>

        <button
          onClick={copyResponse}
          className="px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 transition"
        >
          📋 Copy
        </button>

      </div>

      <div className="prose prose-invert max-w-none">
        <ReactMarkdown>
          {response.rebuttal}
        </ReactMarkdown>
      </div>

      <hr className="my-8 border-slate-700" />

      <h3 className="text-2xl font-bold mb-4">
        Sources Used
      </h3>

      <div className="grid md:grid-cols-2 gap-4">
        {response.sources?.map((source, index) => (
          <SourceCard
            key={index}
            source={source}
          />
        ))}
      </div>

    </div>
  );
}

export default ResponseCard;