The thesis presents the development of selected client-side functionalities for Mendel University in Brno’s digital accreditation application. It addresses weaknesses in the previous process, which depended on disconnected Word and Excel files, repeated data entry, email-based feedback, and limited visibility of application status. The implemented solution uses Vue.js, JavaScript, Pinia, and Vuetify to create modular interfaces for the A-I and B-I accreditation forms, an academic publications section, and an administration sub-application. Data are retrieved from university systems where possible, while reactive validation, unsaved-change protection, and read-only modes improve data integrity and usability.

A central contribution is the role- and status-based approval workflow. A finite-state model, audit trail, authorization checks, and communication timeline control how forms are submitted, reviewed, returned for revision, approved, locked, and finalized. File-level locking prevents changes during final review. The administration module centralizes configurable institutional data and supports reusable components. Testing combined continuous internal checks, user testing, layered frontend testing, and Cypress end-to-end scenarios covering form editing, dynamic inputs, data clearing, and accreditation-file creation. The thesis concludes that the implemented modules provide a more transparent, integrated, maintainable, and extensible basis for MENDELU’s continuing digitalization.

Source sections supporting the claims
Sections 1.1–1.3, pp. 11–13: Motivation, current problems, objectives, and project scope.

Sections 3.5 and 4.2–4.5, pp. 22–28: Manual workflow limitations, requirements, data integration, and development planning.

Sections 6.1–6.4, pp. 38–41: Interface architecture, component design, data flow, security, and access control.

Sections 7.1–7.3, pp. 42–52: Publications module and implementation of Forms A-I and B-I.

Sections 7.4–7.5, pp. 52–63: Status logic, authorization, approval workflow, auditability, communication, locking, and finalization.

Section 7.6, pp. 63–71: Administration sub-application and reusable component architecture.

Sections 8.1–8.3.1, pp. 72–75: User testing, testing levels, Cypress, and automated scenarios.

Section 9, pp. 76–77: Overall contribution, benefits, and future extensibility.