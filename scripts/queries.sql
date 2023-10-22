DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS vacancies;

CREATE TABLE companies
(
    company_id VARCHAR(10) PRIMARY KEY,
    company    VARCHAR(50)
);
CREATE TABLE vacancies
(
    company_id   VARCHAR(10) NOT NULL REFERENCES companies (company_id),
    vacancy_name VARCHAR(100),
    salary_from  int,
    salary_to    int,
    url          text
)