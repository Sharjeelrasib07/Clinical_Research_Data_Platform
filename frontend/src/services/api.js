const API_BASE_URL = "http://localhost:8000";

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
};