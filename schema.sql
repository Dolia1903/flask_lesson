DROP TABLE IF EXISTS exchange;


CREATE TABLE exchange (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_to TEXT NOT NULL,
    exchange_rate FLOAT NOT NULL,
    amount INTEGER NOT NULL,
    result FLOAT NOT NULL
);