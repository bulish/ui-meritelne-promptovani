Summary (179 words)

This master’s thesis describes the client-side implementation of selected functionality in Mendel University’s new Accreditation application. The university previously compiled accreditation files manually in text documents and spreadsheets, which caused repeated data entry, errors, and no real-time view of approval progress. The author, working within the Smart MENDELU team, built the interface with Vue.js and JavaScript. Delivered modules include A-I and B-I forms that pull data from the University Information System, a publications section in user profiles, a form-status system that derives permissions from a user’s role and a file’s state, and an approval engine whose available actions (send, approve, return) depend on role and status. A separate administration sub-application manages shared reference data such as study program metadata, so staff can update it without developer involvement. Testing combined internal simulation, a customer pilot of a minimum viable product, a final multi-day check, and Cypress end-to-end suites covering the forms and record creation. The author concludes the system reduces manual work, improves data integrity and transparency, and is extensible, with future modules planned in TypeScript and an eventual migration.

Source sections supporting the main claims

Claim	Section
Manual, fragmented process and its problems	1.1 Motivation and context; 1.2 Problem statement
Goals: A-I/B-I forms, UIS data retrieval, status tracking, administration, publications	1.3 Objectives and thesis goals
Smart MENDELU team and the Vue.js stack	2.6 Digitalization at MENDEL University
Requirements (UIS integration, real-time status, centralized feedback)	4.2 Overview of requirements; 4.3 Functional requirements
Publications module	7.1 Publications in User profile
Role- and status-based permissions	7.4 Form status (incl. Table 7.2)
Approval engine and its actions	7.5 Form approval process (7.5.1, 7.5.2)
Administration sub-application	7.6 Administration sub-application (7.6.1)
Testing approach	8.1 User testing; 8.3 End-to-end testing with Cypress (8.3.1)
Conclusions, TypeScript migration	9 Conclusion
The file is a master’s thesis, not a journal article, and I found no abstract in it. The summary rests on the body chapters only.
The conclusions about reduced labor and improved data integrity are the author’s claims. Chapter 8 describes testing but reports no measured before/after results.