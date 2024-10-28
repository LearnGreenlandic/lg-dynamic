PRAGMA case_sensitive_like = ON;
PRAGMA foreign_keys = OFF;
PRAGMA journal_mode = MEMORY;
PRAGMA synchronous = OFF;
PRAGMA threads = 4;
PRAGMA trusted_schema = OFF;
PRAGMA locking_mode = NORMAL;

CREATE TABLE qas (
	qa_q TEXT NOT NULL,
	qa_a TEXT NOT NULL,
	qa_q_txt TEXT NOT NULL DEFAULT '',
	qa_a_txt TEXT NOT NULL DEFAULT '',

	PRIMARY KEY (qa_q)
);

CREATE TABLE qs (
	q TEXT NOT NULL,
	q_txt TEXT NOT NULL DEFAULT '',

	PRIMARY KEY (q)
);
