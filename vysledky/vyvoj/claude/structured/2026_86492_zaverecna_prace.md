Summary

Goal: This master’s thesis aims to implement selected client-side functionalities of a new Accreditation application at Mendel University in Brno, replacing manual workflows based on Word and Excel templates with a unified web interface that retrieves data from the University Information System (UIS).

Methods: After analyzing the current process, legal framework and requirements, the author designed the interface following the Smart MENDELU design system and Figma wireframes by Veverka (2025). The application uses Vue.js, JavaScript, Vuetify, Pinia stores and composables. Implemented modules include the Publications tab in the user profile, forms A-I and B-I, form statuses, an approval engine using FormApprovalStatusIds, and an administration sub-application with five component types. Development followed Scrumban.

Main results: Role-based status matrices control editing rights across five roles. Approval uses ID 3 (submitted), 1 (approved) and 2 (rejected). File-level “Locked” and “Closed” states override form states. Testing combined user testing with three Cypress end-to-end suites covering A-I, B-I and new record creation.

Conclusions: The application reduces manual labor, improves data integrity and provides real-time transparency. Future modules are planned in TypeScript, with eventual migration of the codebase.

(Word count: ~190)

Supporting sections

Goal: 1.3 Objectives and thesis goals; 1.2 Problem statement; 3.5 Current state of the accreditation process at MENDELU
Methods: 5 Frameworks and tools (Vue.js, Scrumban, Table 5.1); 6.2 Component-based design approach; 7.1 Publications in User profile; 7.2 Form A-I; 7.3 Form B-I; 7.6.2 Standardized component architecture (Types 1–5)
Main results: 7.4 Form status (Tables 7.2–7.5); 7.5.2 Lifecycle of an approval workflow (status IDs 3, 1, 2); 7.5.5 File-level overrides and finalization; 8.3.1 Implementation of automated test scenarios; 8.1 User testing
Conclusions: Chapter 9 Conclusion (paragraphs on primary contribution and extensibility/TypeScript migration)

Note: the thesis was supplied as the text itself, so I used its full body and not the abstract, which was not included.