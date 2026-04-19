export default function About() {
  return (
    <div className="page">
      <h1>About the Platform</h1>
      <p className="page-subtitle">
        A full-stack clinical research data platform built to demonstrate modern
        workflows for pseudonymized data processing, storage, API delivery, and
        interactive analytics.
      </p>

      <div className="about-card">
        <h2>Platform Purpose</h2>
        <p>
          The Clinical Research Data Platform was developed as a modular system
          for handling synthetic, pseudonymized patient-style datasets in a
          research-oriented environment. It demonstrates how data can move from
          ingestion and transformation to structured storage, API access, and
          user-facing exploration through a unified architecture.
        </p>
      </div>

      <div className="about-card">
        <h2>Research Use Case</h2>
        <p>
          This platform supports analysis of patient demographics, visit patterns,
          laboratory measurements, and diagnosis distributions in a way that is
          relevant to data-driven healthcare and research analytics. It is
          particularly suited to exploring structured workflows that can support
          gender-sensitive clinical and population-level analysis.
        </p>
      </div>

      <div className="about-card">
        <h2>System Architecture</h2>
        <ul className="about-list">
          <li>Raw synthetic datasets are stored in a source data layer.</li>
          <li>Python ETL scripts validate, clean, and standardize records.</li>
          <li>Processed data is loaded into PostgreSQL.</li>
          <li>FastAPI exposes structured endpoints and summary statistics.</li>
          <li>React provides a dashboard for metrics, charts, and table-based exploration.</li>
          <li>Docker ensures reproducible local deployment across services.</li>
        </ul>
      </div>

      <div className="about-card">
        <h2>Core Capabilities</h2>
        <div className="tech-stack">
          <span>Python ETL</span>
          <span>Data Validation</span>
          <span>PostgreSQL</span>
          <span>FastAPI</span>
          <span>React</span>
          <span>Docker</span>
          <span>Data Quality Reporting</span>
          <span>Frontend Analytics</span>
        </div>
      </div>

      <div className="about-card">
        <h2>Data Flow</h2>
        <p className="data-flow">
          Synthetic Data → ETL Pipeline → Processed Layer → PostgreSQL → FastAPI → React Dashboard
        </p>
      </div>

      <div className="about-card">
        <h2>Privacy and Handling Principles</h2>
        <p>
          All records are synthetic and pseudonymized. No real patient identifiers
          are included. The platform demonstrates safe handling concepts relevant
          to research settings, including structured schemas, separated data
          layers, logging, and documented storage procedures.
        </p>
      </div>
    </div>
  );
}