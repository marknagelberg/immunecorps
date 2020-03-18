# ImmuneCorps

People infected with COVID-19 [likely become immune](https://twitter.com/florian_krammer/status/1239036927535448069), although this is not known with certainty. If true, this immune cohort will become a critical resource for people who have not had the virus. These people, for example, could be called upon to [give blood](https://marginalrevolution.com/marginalrevolution/2020/03/convalescent-blood-therapy.html) for convalescent blood therapy, volunteer at hospitals, or get groceries for the uninfected and vulnerable. 

Immune people need a way to join an [ImmuneCorps](https://twitter.com/naval/status/1238610618770313216): an army of immune good samaritans that want to help those in need. Health authorities will need a way to track these people and enlist their help. Citizens need a way of verifying whether someone that says they are immune is in fact immune. Citizens also should have a way of sending requests to immune volunteers.

ImmuneCorps will be a web application that Health Authorities can deploy to solve these problems. 

## Proposed Features / Functionality

ImmuneCorps is in planning and early development stages. The ideas and proposed functionality may be subject to substantial changes in light of new ideas or requirements. 

ImmuneCorps will have three main groups of users: 

1) **The Health Authority** installs and runs the application, serves it on a public-facing website, adds individuals they know to be immune, approves volunteers. 
2) **ImmuneCorps Volunteers** (people that are immune to Coronavirus) and 
3) **Citizens** needing help from ImmuneCorps Volunteers or needing to verify someone that says they are immune is immune. 

The application should be able to perform the following core tasks:

-  Health Authorities have their IT staff install ImmuneCorps using their own servers / databases and serve it to a public facing website, with their personalized Government logo / name. This should be relatively easy / painless and there should be good documentation about how to do it. 

-  ImmuneCorps Volunteers can visit the ImmuneCorps website to enter in information that they want to volunteer as a member of ImmuneCorps. This would include an email, but the application form should be configurable by the Health Authority to include information in the sign-up form they need to connect the person to their health records (e.g. health number, scanned document). 

-  The Health Authority can configure the geographic location from which they will accept / consider volunteers and citizen requests for ImmuneCorps. 

-  The Health Authority can mark ImmuneCorps volunteer applicants as immune-verified. 

-  The Health Authority can search and filter ImmuneCorps volunteers according to the information they have asked from them. They should also be able to export information to popular usable formats like Excel or CSV.

-  A public facing API can confirm whether someone is a verified ImmuneCorps volunteer. 

-  Citizens can submit requests to ImmuneCorps to have an ImmuneCorps volunteer help them. 

## Technologies

ImmuneCorps is developed in Python, using the Django web framework. 

