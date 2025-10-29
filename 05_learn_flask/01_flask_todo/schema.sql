-- Delete the tasks table if it already exists
DROP TABLE IF EXISTS tasks;

-- Create the tasks table
CREATE TABLE tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
title TEXT NOT NULL,
description TEXT,
completed BOOLEAN NOT NULL DEFAULT 0
);

