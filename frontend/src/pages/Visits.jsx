import { useEffect, useState } from "react";
import { api } from "../services/api";
import DataTable from "../components/DataTable";

export default function Visits() {
  const [visits, setVisits] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    api.getVisits().then(setVisits).catch(console.error);
  }, []);

  const filteredVisits = visits.filter(
    (visit) =>
      visit.visit_id.toLowerCase().includes(search.toLowerCase()) ||
      visit.patient_id.toLowerCase().includes(search.toLowerCase()) ||
      visit.department.toLowerCase().includes(search.toLowerCase())
  );

  const columns = [
    { key: "visit_id", label: "Visit ID" },
    { key: "patient_id", label: "Patient ID" },
    { key: "visit_date", label: "Visit Date" },
    { key: "department", label: "Department" },
    { key: "blood_pressure_systolic", label: "BP Systolic" },
    { key: "blood_pressure_diastolic", label: "BP Diastolic" },
    { key: "glucose_level", label: "Glucose" },
  ];

  return (
    <div className="page">
      <h1>Visits</h1>
      <p className="page-subtitle">
        Explore visit-level observations and department activity across the dataset.
      </p>

      <input
        type="text"
        placeholder="Search by Visit ID, Patient ID, or Department..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="search-input"
      />

      <DataTable columns={columns} data={filteredVisits} />
    </div>
  );
}