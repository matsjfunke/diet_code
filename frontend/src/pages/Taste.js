import React, { useState } from "react";
import api from "../utils/api";
import "./Taste.css";

const Taste = () => {
  const [ranking, setRanking] = useState([]);
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchRanking = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await api.get("/gh-deletion-ranking", {
        params: { url },
      });
      setRanking(response.data);
    } catch (err) {
      setError("Failed to fetch ranking. Please check the URL and try again.");
      console.error("Error fetching ranking:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetchRanking();
  };

  return (
    <div className="taste-container">
      <h1 className="main-heading">GitHub Deletion Ranking</h1>
      <h3 className="sub-header">
        Paste a link to a public GitHub Repository to get a ranking of
        contributor deletions.
      </h3>
      <form onSubmit={handleSubmit} className="taste-form">
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter GitHub repository URL"
          required
          className="taste-input"
        />
        <button type="submit" disabled={loading} className="taste-button">
          {loading ? "Loading..." : "Get Ranking"}
        </button>
      </form>

      {error && <p className="taste-error">{error}</p>}

      {ranking.length > 0 && (
        <div className="taste-ranking-list">
          <h2 className="taste-ranking-header">Deletion Ranking</h2>
          <ul className="taste-contributor-list">
            {ranking.map((item) => (
              <li
                key={item.contributor.username}
                className="taste-contributor-item"
              >
                <img
                  src={item.contributor.profile_pic}
                  alt={`${item.contributor.username}'s avatar`}
                  className="taste-avatar"
                />
                <div className="taste-contributor-info">
                  <h3>{item.contributor.username}</h3>
                  <p>Deletions: {item.contributor.deletions}</p>
                  <p>Additions: {item.contributor.additions}</p>
                  <p>Commits: {item.contributor.commits}</p>
                </div>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Taste;
