-- Schema for Participants
CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    team_id INTEGER,
    role TEXT CHECK(role IN ('user', 'admin', 'judge')),
    password_hash TEXT NOT NULL
);

-- Schema for Events
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT CHECK(type IN ('individual', 'team')),
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    location TEXT NOT NULL
);

-- Schema for Scores
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    participant_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(id),
    FOREIGN KEY (participant_id) REFERENCES participants(id)
);
