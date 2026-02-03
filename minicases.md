### [-> back to Overview](README.md)


#### Case: First Standardized Service Interface in the BMW E/E Architecture

**Context**  
Highly coupled vehicle function architecture with safety-critical dependencies and legacy communication buses.

**Challenge**  
Enable high-level vehicle functions (e.g. speech interaction, automation) to control window movement without exposing functional logic or safety dependencies.

**My Responsibility**  
Architectural ownership of data abstraction and service interface definition for automated window control, from concept to series release.

**Key Architectural Actions**  
- Defined a strict service abstraction decoupling window control from functional and safety logic  
- Designed a standardized service interface exposing movement requests, availability and unified position semantics  
- Established information-hiding rules to enable reuse across brands and vehicle derivatives

**Outcome**  
Released the first standardized service interface for a low-level vehicle function, enabling uniform window control across all BMW Group brands and establishing a reusable blueprint for decoupled, data-centric architectures.


---

### Case: Middleware to Standardize Vehicle Data in a Software-Defined Vehicle

**Context**  
Highly heterogeneous and continuously evolving vehicle board networks with strong variant dependency and limited semantic consistency across derivatives and markets.

**Challenge**  
Abstract low-level vehicle data into a stable, standardized semantic model (VSS by COVESA) despite constant changes in board networks, organizational resistance and evolving external standards.

**My Responsibility**  
Architectural ownership of a data abstraction middleware, including the decision to introduce model-based data mapping as the single source of truth for standardization and scalability.

**Key Architectural Actions**  
- Established an MBSE-based approach to model and maintain semantic mappings between board network data and standardized vehicle signals.  
- Introduced machine-readable model outputs and automated code generation to enable consistent integration across all derivatives . 
- Enforced strict adherence to the external standard while extending it only where required by domain-specific needs.
- Designed end-to-end validation through automated generation, simulation and fleet-wide board network analytics.

**Outcome**  
Enabled scalable vehicle data standardization across all derivatives, significantly reducing re-implementation effort and allowing software teams to focus on feature growth instead of data integration, while establishing a reusable blueprint for data-centric architectures.


# Case: Developing Intelligent Functions to goLive.

## Context: 
- BMW wanted to introduce intelligent funtions in car, that benefit customers with a wow-effect.
- Over 50 customers functions stared development.

## Challenges:
- Project started way behind development schedule.
- Multiple departments competed for budget in a political fashion.
- Various Stakeholders at a time (Savety of Use, Data Protection, User Expereience, Implementers, Testers, Plants, Quality Managers, ...)
- Learning fom customer behavior was a totally new field.
- E/E Architecture was not prepared.
- Tight budget

## My Role:
- I was a **Function Owner** with End to End technical responsability for two functions.
- Focus shifted from E/E architecture -> functional design including UX -> implementation -> testing -> series support.

## Key Decisions:
- Developing the committed functions without political involvement.
- Keepling close contact to all relevant technical stakeholders.
- Using Model Based Systems Engineering (MBSE) to describe and communicate functionality.

## Outcome:
- My two functions (Automated window Opening, Learning Seat Climateization) were released in 2019 starting with G20. 42 Other projects died along the way.
- Two patent specifications were released.
- Now the automated window opening has the best conversion rate and the highest use out of all intelligent functions in 2025 protfolio.

---

# Case: Conzepualisef Data Middleware to provide standardized data.

## Context: 
- In order to facilitate development and data analytics standarized vehilce data was needed accross automotive indutriy.
- To prepare integration of AI, the same data format should exist in car and in backend systems. 

## Challenges:
- Project Stakholders from different departments had an intense conflict. The predecessor left the project.
- Highly complex sourrounding systems, affected by constant changes, sometimes released without documentation.
- Target was not accepted, there was no implementer named. 

## My Role:
- Centeral **Vehicle Data Architect**: Responsible to design a solution for which some department takes over responsiblity for implementation.

## Key Decisions:
- Close collaboration and trust building among various stakeholders.
- Participation in COVESA All members Meeting, to present architectural concept and testing strategy to ged high qulity feedback from specialists across automotive industiries.
- Offer Data Mddle Ware inside data collection framework, so all data collectors profit at one.
- Integrate Data Middleware in MBSE and interconnect ist with board net data base and [Vehicle Signal Specification](https://github.com/COVESA/vehicle_signal_specification).
- Offer a code generator which produces data middle ware tailored to any derivative with its unique board net version.
- Highly automate testing producing a landingpage with transparent test results.

## Outcome:
- Data Middelware is integrated in Neue Klasse E/E Architecture, starting with iX.
- Patent Specification (currently in review).

---

# Case: Integrating Data By Design into Automtive Development Process.


---

# Case: Leading a tree based standardization language into an onthology, to accelerate AI development.

## Context:
- At BMW [COVESA Vehicle Signal Specification](https://github.com/COVESA/vehicle_signal_specification) is used to standardize data and make it easy to understand and easy to find data points even to non-expterts. 
- The tree structured yaml format raises a fundamental Issues.
- There is a solution needed to enable simple governance close to domain knowledge as well as the possibility to imprint domain knowledge into the data model. 

## Challenge:
- In 2026 Automotive Indutry faces uncertainty and a weak chinese market, budget is low.
- There is not a known solution to address these problems.
- high time pressure.

## My Role:
- Lead architect responsible for data modeling and governance principles. Product Owner of the VSS-model used by BMW. 

## Key Decisions:
- Close Collaboration with COVESA in order to find a solution.
  

## Outcome:
- open :D 

