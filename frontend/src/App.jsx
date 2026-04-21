import { useState } from "react";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import Patients from "./pages/Patients";
import Visits from "./pages/Visits";
import Labs from "./pages/Labs";
import Admin from "./pages/Admin";
import About from "./pages/About";

export default function App() {
  const [currentPage, setCurrentPage] = useState("Dashboard");

  function renderPage() {
    switch (currentPage) {
      case "Patients":
        return <Patients />;
      case "Visits":
        return <Visits />;
      case "Labs":
        return <Labs />;
      case "Admin":
        return <Admin />;
      case "About":
        return <About />;
      default:
        return <Dashboard />;
    }
  }

  return (
    <div className="app-container">
      <Navbar currentPage={currentPage} setCurrentPage={setCurrentPage} />
      <main className="main-content">{renderPage()}</main>
      <footer className="footer">
        Built with React, FastAPI, PostgreSQL, Docker, and Python ETL pipelines.
      </footer>
    </div>
  );
}