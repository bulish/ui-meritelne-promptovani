Goal
To implement selected client-side functionalities for Mendel University in Brno’s Accreditation application, replacing fragmented manual accreditation work based on Word, Excel, copied University Information System (UIS) data, and email-based coordination.

Methods
The thesis used iterative front-end development within the Smart MENDELU environment. It implemented a Vue.js/JavaScript application using Pinia stores, Vuetify components, composables, backend API integration, role-based access control, and layered user and automated testing.

Main results
The implementation delivered modular interfaces for the A-I and B-I accreditation forms, a publications area in user profiles, and an administration sub-application. Form A-I combines read-only institutional data with editable accreditation information, validates inputs, formats dates, checks secure web links, supports draft saving, and locks data after workflow submission. Form B-I records programme descriptions, graduate profiles, study duration, education-field percentages, regulated-profession information, and approval actions. The workflow uses FormApprovalStatusIds: 1 for approved, 2 for rejected, and 3 for submitted. A finite state machine enforces valid transitions; status changes create an audit trail with previous and new states, timestamps, and responsible users. File-level “Locked” and “Closed” states override form-level permissions. Cypress scenarios verified A-I data persistence, B-I dynamic fields and data clearing, and creation of a new accreditation record.

Conclusions
The thesis concludes that the modules centralize accreditation work, improve transparency and data integrity, automate UIS data retrieval, and provide an extensible foundation; future modules are planned in TypeScript.

Supporting source sections
Sections 1.1–1.3, pp. 11–13: Manual workflow issues, UIS integration, and thesis objectives.

Sections 4.2–4.5, pp. 25–28: Functional and non-functional requirements and iterative development plan.

Sections 7.1–7.3, pp. 42–52: Publications module and Form A-I/Form B-I implementation.

Sections 7.4.1 and 7.5.2–7.5.5, pp. 54–63: Status IDs, audit trail, finite state machine, approval, locking, and closure.

Sections 8.1–8.3.1, pp. 72–75: User testing and Cypress test scenarios.

Section 9, pp. 76–77: Conclusions on data integrity, transparency, extensibility, and future TypeScript migration.

