Goal
Analyze MENDELU’s manual accreditation process and implement selected client-side features of the new Accreditation application: A-I/B-I forms, form statuses, the approval process, an administration sub-application, and profile publications.

Methods
The author analyzed the current process, regulations, and stakeholder requirements. The client side was then developed iteratively (Scrumban) within the Smart MENDELU team using Vue.js, JavaScript, Pinia, and Vuetify, following Figma designs by Veverka. Verification combined internal and MVP user testing with Cypress end-to-end tests.

Main results
Each form uses a view–composable–Pinia store architecture. UI access is computed by crossing the backend status with the user’s highest-priority role out of five roles. FormApprovalStatusIds are 1 (approved), 2 (rejected, which requires a reason), and 3 (submitted). A shared useFormApproval.js composable resolves endpoints dynamically (e.g., /forms-a/i/approvals). File-level “Locked” and “Closed” states override form editability, and closing a file requires Form A-I’s approval date. The administration module offers five reusable component types (Type1–Type5), and closed files keep their original values after administrative changes. Three Cypress suites cover Form A-I, Form B-I, and new file creation.

Conclusions
The author concludes that the application reduces manual labor and improves data integrity and real-time transparency through UIS integration and a centralized workflow. Future modules are planned in TypeScript, which will lead to a full migration of the codebase.

Supporting passages

Thesis assignment (“Guides to writing a thesis”) and §1.3: the goals and scope
§3.5, Ch. 4, §4.5, §5.5, Ch. 6 (Figma designs by Veverka 2025): the analysis and development approach
§7.2.2, §7.3.1: the view/composable/store architecture
§7.4, §7.4.1, §7.4.2, Tables 7.2–7.5: the five roles, role prioritization, and status IDs 1/2/3
§7.5.2–7.5.3: the approval actions, required rework reason, useFormApproval.js, and the dynamic endpoint
§7.5.5: the Locked/Closed states and the Form A-I approval-date condition
§7.6.2, §7.6.4: the five component types and the “Closed File” protection rule
§8.1, §8.3.1: user testing and the three Cypress suites
Ch. 9: the conclusions and the planned TypeScript migration