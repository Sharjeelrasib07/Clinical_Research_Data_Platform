import { useEffect, useState } from "react";
import { api } from "../services/api";
import DataTable from "../components/DataTable";

export default function Labs() {
  const [labs, setLabs] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    api.getLabs().then(setLabs).catch(console.error);
  }, []);

  const filteredLabs = labs.filter(
    (lab) =>
      lab.result_id.toLowerCase().includes(search.toLowerCase()) ||
      lab.patient_id.toLowerCase().includes(search.toLowerCase()) ||
      lab.test_name.toLowerCase().includes(search.toLowerCase())
  );

  const columns = [
    { key: "result_id", label: "Result ID" },
    { key: "patient_id", label: "Patient ID" },
    { key: "test_name", label: "Test Name" },
    { key: "test_value", label: "Value" },
    { key: "unit", label: "Unit" },
    { key: "test_date", label: "Test Date" },
  ];

  return (
    <div className="page">
      <h1>Lab Results</h1>
      <p className="page-subtitle">
        Review pseudonymized laboratory measurements and test values across patients.
      </p>

      <input
        type="text"
        placeholder="Search by Result ID, Patient ID, or Test Name..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="search-input"
      />

      <DataTable columns={columns} data={filteredLabs} />
    </div>
  );
}