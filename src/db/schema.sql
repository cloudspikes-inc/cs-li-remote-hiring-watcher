CREATE TABLE IF NOT EXISTS raw_jobs (
  id TEXT PRIMARY KEY,
  title TEXT,
  company TEXT,
  location TEXT,
  description TEXT,
  posted_date TIMESTAMP NULL,
  link TEXT,
  raw_json JSONB,
  inserted_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS clean_jobs (
  id TEXT PRIMARY KEY,
  title TEXT,
  company TEXT,
  location TEXT,
  link TEXT,
  matched_keywords TEXT[],
  score INT,
  inserted_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS job_stats (
  day DATE PRIMARY KEY,
  fetched INT DEFAULT 0,
  filtered INT DEFAULT 0,
  alerted INT DEFAULT 0
);
