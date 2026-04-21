const API_BASE_URL = "https://clinical-research-data-platform.onrender.com";

async function fetchJson(endpoint) {
  const response = await fetch(`${API_BASE_URL}${endpoint}`);
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json();
}

export const api = {
  getHealth: () => fetchJson("/health"),
  getPatients: () => fetchJson("/patients"),
  getVisits: () => fetchJson("/visits"),
  getLabs: () => fetchJson("/labs"),
  getGenderDistribution: () => fetchJson("/stats/gender-distribution"),
  getDiagnosisSummary: () => fetchJson("/stats/diagnosis-summary"),
  getDataQuality: () => fetchJson("/stats/data-quality"),

  // ✅ NEW: Run ETL pipeline
  runETL: async () => {
    const response = await fetch(`${API_BASE_URL}/admin/run-etl`, {
      method: "POST",
    });

    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }

    return response.json();
  },
};