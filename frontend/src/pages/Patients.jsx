import { useEffect, useState } from "react";
import { api } from "../services/api";
import DataTable from "../components/DataTable";

export default function Patients() {
  const [patients, setPatients] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    api.getPatients().then(setPatients).catch(console.error);
  }, []);

  const filteredPatients = patients.filter((p) =>
    p.patient_id.toLowerCase().includes(search.toLowerCase())
  );

  const columns = [
    { key: "patient_id", label: "Patient ID" },
    { key: "sex_at_birth", label: "Sex at Birth" },
    { key: "gender_identity", label: "Gender Identity" },
    { key: "age", label: "Age" },
    { key: "bmi", label: "BMI" },
    { key: "diagnosis_code", label: "Diagnosis" },
  ];

  return (
    <div className="page">
      <h1>Patients</h1>
      <p className="page-subtitle">
        Browse and search pseudonymized patient records used in the research platform.
      </p>

      <input
        type="text"
        placeholder="Search by Patient ID..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="search-input"
      />

      <DataTable columns={columns} data={filteredPatients} />
    </div>
  );
}