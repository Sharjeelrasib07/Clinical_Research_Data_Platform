export default function Navbar({ currentPage, setCurrentPage }) {
  const links = ["Dashboard", "Patients", "Visits", "Labs", "Admin", "About"];

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <div className="navbar-title">Clinical Research Data Platform</div>
        <div className="navbar-subtitle">
          Pseudonymized data workflows for research analytics and quality tracking
        </div>
      </div>

      <div className="navbar-links">
        {links.map((link) => (
          <button
            key={link}
            className={currentPage === link ? "nav-button active" : "nav-button"}
            onClick={() => setCurrentPage(link)}
          >
            {link}
          </button>
        ))}
      </div>
    </nav>
  );
}