import { useEffect, useState } from "react";
import { api } from "../services/api";
import StatCard from "../components/StatCard";
import GenderChart from "../components/charts/GenderChart";
import DiagnosisChart from "../components/charts/DiagnosisChart";

function QualityBadge({ dropped }) {
  const isGood = dropped === 0;

  return (
    <span className={isGood ? "status-badge good" : "status-badge warning"}>
      {isGood ? "Clean" : `${dropped} Dropped`}
    </span>
  );
}

export default function Dashboard() {
  const [health, setHealth] = useState(null);
  const [patients, setPatients] = useState([]);
  const [visits, setVisits] = useState([]);
  const [labs, setLabs] = useState([]);
  const [genderData, setGenderData] = useState([]);
  const [diagnosisData, setDiagnosisData] = useState([]);
  const [dataQuality, setDataQuality] = useState(null);

  useEffect(() => {
    async function loadData() {
      try {
        const [
          healthRes,
          patientsRes,
          visitsRes,
          labsRes,
          genderRes,
          diagnosisRes,
          dataQualityRes,
        ] = await Promise.all([
          api.getHealth(),
          api.getPatients(),
          api.getVisits(),
          api.getLabs(),
          api.getGenderDistribution(),
          api.getDiagnosisSummary(),
          api.getDataQuality(),
        ]);

        setHealth(healthRes);
        setPatients(patientsRes);
        setVisits(visitsRes);
        setLabs(labsRes);
        setDataQuality(dataQualityRes);

        const genderChartData = Object.entries(genderRes.gender_identity || {}).map(
          ([label, count]) => ({
            label,
            count,
          })
        );

        const diagnosisChartData = Object.entries(diagnosisRes).map(
          ([label, count]) => ({
            label,
            count,
          })
        );

        setGenderData(genderChartData);
        setDiagnosisData(diagnosisChartData);
      } catch (error) {
        console.error("Dashboard load error:", error);
      }
    }

    loadData();
  }, []);

  return (
    <div className="page">
      <div className="page-header">
        <div>
          <h1>Dashboard</h1>
          <p className="page-subtitle">
            Overview of pseudonymized clinical research data, ETL outputs, API
            connectivity, and data quality metrics.
          </p>
        </div>

        <div className="page-badges">
          <span className="platform-badge">Research Demo</span>
          <span className="platform-badge">Pseudonymized Data</span>
          <span className="platform-badge">Full-Stack Platform</span>
        </div>
      </div>

      <div className="stats-grid">
        <StatCard title="Patients" value={patients.length} />
        <StatCard title="Visits" value={visits.length} />
        <StatCard title="Lab Results" value={labs.length} />
        <StatCard
          title="API Health"
          value={health?.status === "ok" ? "Connected" : "Unavailable"}
        />
      </div>

      <div className="charts-grid">
        <GenderChart data={genderData} />
        <DiagnosisChart data={diagnosisData} />
      </div>

      <div className="about-card">
        <div className="section-header">
          <h2>Data Quality Overview</h2>
          <span className="etl-run">
            Last ETL Run: {dataQuality?.metadata?.last_etl_run || "Unavailable"}
          </span>
        </div>

        {dataQuality ? (
          <div className="quality-grid">
            <div className="quality-item">
              <div className="quality-top">
                <strong>Patients</strong>
                <QualityBadge dropped={dataQuality.patients.dropped_records} />
              </div>
              <p>
                {dataQuality.patients.cleaned_records} / {dataQuality.patients.raw_records} cleaned
              </p>
              <p>Dropped: {dataQuality.patients.dropped_records}</p>
            </div>

            <div className="quality-item">
              <div className="quality-top">
                <strong>Visits</strong>
                <QualityBadge dropped={dataQuality.visits.dropped_records} />
              </div>
              <p>
                {dataQuality.visits.cleaned_records} / {dataQuality.visits.raw_records} cleaned
              </p>
              <p>Dropped: {dataQuality.visits.dropped_records}</p>
            </div>

            <div className="quality-item">
              <div className="quality-top">
                <strong>Lab Results</strong>
                <QualityBadge dropped={dataQuality.lab_results.dropped_records} />
              </div>
              <p>
                {dataQuality.lab_results.cleaned_records} / {dataQuality.lab_results.raw_records} cleaned
              </p>
              <p>Dropped: {dataQuality.lab_results.dropped_records}</p>
            </div>
          </div>
        ) : (
          <p>Loading data quality report...</p>
        )}
      </div>
    </div>
  );
}