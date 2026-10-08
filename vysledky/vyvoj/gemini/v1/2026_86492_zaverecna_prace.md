## Goal

The thesis aims to implement specific client-side functionalities for a unified accreditation application at Mendel University in Brno, moving away from fragmented, manual record-keeping to a streamlined digital environment.

## Methods

The project utilized an iterative development approach within the Smart MENDELU team using a Scrumban methodology, supported by tools such as Trello, Git/GitLab, Fork, SonarQube, Swagger, and Docker. The client-side application was built using the Vue.js framework and JavaScript, incorporating Vuetify and a shared style library for UI design. Testing was conducted using user evaluations, frontend testing levels, and automated end-to-end test scenarios implemented via Cypress.

## Main results

The project successfully delivered core accreditation components, including the A-I and B-I forms, a research publications module, an administration sub-application, and a centralized approval engine. Specifically, the publications profile integrates research outputs and citation metrics across platforms like Web of Science and Scopus. The A-I and B-I forms incorporate core metadata, study parameters, and real-time validation rules. Furthermore, an automated role-action permission matrix successfully synchronizes form-level accessibility and status IDs (e.g., status 1 for approved, 2 for rejected, and 3 for submitted) with backend validation workflows.

## Conclusions

The authors conclude that implementing a centralized, web-based digital accreditation platform effectively eliminates administrative bottlenecks, reduces the risk of human error, and ensures real-time data transparency and synchronization with the University Information System. They recommend adopting TypeScript for future extensions and full code migration to further enhance application stability and maintainability.