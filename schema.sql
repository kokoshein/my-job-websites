DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    location TEXT NOT NULL,
    salary TEXT NOT NULL,
    phone TEXT NOT NULL, -- ဖုန်းနံပါတ်အတွက် အသစ်ထည့်ထားတာပါ
    description TEXT NOT NULL
);