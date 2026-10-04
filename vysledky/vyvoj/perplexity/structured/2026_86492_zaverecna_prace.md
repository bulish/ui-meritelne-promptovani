Goal: This master’s thesis aimed to implement selected client-side functionalities for Mendel University in Brno’s Accreditation application, replacing fragmented Word, Excel, email, and manually copied University Information System (UIS) data workflows with an integrated digital environment. It focused on Forms A-I and B-I, a publications area in user profiles, a role-aware approval process, and an administration sub-application.

Methods: The application was implemented using Vue.js, JavaScript, Pinia, Vuetify, Vite, and modular composables and stores. The design employed component-based architecture, reactive state management, role-based access control, form validation, audit trails, API synchronization, and a finite-state approval workflow. Testing combined continuous internal testing, customer testing of a Minimum Viable Product, unit and integration testing principles, and Cypress end-to-end tests.

Main results: Form A-I supports metadata, validation, automatic date formatting, secure-link checks, draft saving, and submission. Form B-I captures qualitative programme information and quantitative regulatory data. Workflow states use FormApprovalStatusIds: 1 approved, 2 rejected, and 3 submitted. The system logs status changes, restricts editing by role and state, enables feedback-linked rework, and globally locks or closes completed files. Cypress tests covered A-I persistence, B-I dynamic fields and resets, and creation of new accreditation records.

Conclusions: The implemented modules improve transparency, data integrity, and maintainability by centralizing workflows and automating UIS data retrieval, while providing an extensible foundation for future TypeScript-based development.

Supporting source sections
1.1–1.3, “Motivation and context,” “Problem statement,” and “Objectives and thesis goals” (pp. 11–13): Manual-process limitations, UIS integration, scope, and intended functionality.

4.2–4.4, “Overview of requirements,” “Functional requirements,” and “Non-functional requirements” (pp. 25–27): Required forms, publications module, workflow tracking, administration, security, responsiveness, and maintainability.

6.2–6.4, “Component-based design approach,” “State and data flow design,” and “Security and access control design” (pp. 39–41): Modular design, reactive state, validation, authentication, and access controls.

7.2–7.3, “Form A-I” and “Form B-I” (pp. 45–52): Form architecture, data fields, validation, workflow actions, and technical implementation.

7.4–7.5.5, “Form status” through “File-level overrides and finalization” (pp. 52–63): Status IDs, permissions, audit trail, approval lifecycle, communication, locking, and closure.

8.1–8.3.1, “User testing” through “Implementation of automated test scenarios” (pp. 72–75): Testing strategy and Cypress test coverage.

9, “Conclusion” (pp. 76–77): Claimed contribution to digitalization, reduced manual work, data integrity, extensibility, and planned TypeScript migration.