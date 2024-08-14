PRAGMA case_sensitive_like = ON;
PRAGMA foreign_keys = OFF;
PRAGMA journal_mode = MEMORY;
PRAGMA locking_mode = EXCLUSIVE;
PRAGMA synchronous = OFF;
PRAGMA threads = 4;
PRAGMA trusted_schema = OFF;
PRAGMA page_size = 65536;
VACUUM;
PRAGMA locking_mode = NORMAL;

CREATE TABLE qas (
	qa_q TEXT NOT NULL,
	qa_a TEXT NOT NULL,

	PRIMARY KEY (qa_q)
);
