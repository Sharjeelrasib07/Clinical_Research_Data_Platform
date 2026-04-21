import { useState } from "react";
import { api } from "../services/api";

export default function Admin() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function handleRunETL() {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await api.runETL();
      setResult(response);
    } catch (err) {
      setError("Failed to run ETL pipeline.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="page">
      <h1>Admin Control Panel</h1>
      <p className="page-subtitle">
        Run operational tasks and manage ETL workflow execution for the platform.
      </p>

      <div className="about-card">
        <h2>ETL Pipeline Control</h2>
        <p>
          This action clears existing tables, reloads the synthetic source data,
          and regenerates the data quality report.
        </p>

        <button
          className="etl-button"
          onClick={handleRunETL}
          disabled={loading}
        >
          {loading ? "Running ETL..." : "Run ETL Pipeline"}
        </button>

        {result && (
          <div className="etl-result success-box">
            <strong>Status:</strong> {result.status}
            <br />
            <strong>Message:</strong> {result.message}
          </div>
        )}

        {error && (
          <div className="etl-result error-box">
            <strong>Error:</strong> {error}
          </div>
        )}
      </div>
    </div>
  );
}