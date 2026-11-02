# ISAC defensive resilience and fault-injection test catalogue

This repository collects safety-bounded testing use cases for integrated sensing and communication (ISAC), gNodeBs, sensing-capable radios, and cellular-site continuity when an unidentified drone is observed near critical infrastructure. It addresses detection, uncertainty, operator notification, service continuity, and recovery, including simulated wartime-like infrastructure degradation.

**Status:** this is a test-design catalogue, not an implemented test harness, certified protection system, or record of completed tests. No deployment, thresholds, or test results have been supplied.

## What "exhaustive" means here

The goal is **exhaustive coverage of an explicitly declared, finite supported configuration and requirements baseline**. This document does not establish exhaustive coverage of every possible drone, attack, environment, radio, or combination of failures. A catalogue alone cannot establish that claim.

A bounded claim is permitted only after the configuration inventory, applicable requirements, risk assessment, scenario instances, approved thresholds, and evidence are complete and reviewed. Pairwise coverage is a sampling strategy, not proof of exhaustive combination coverage. Untested combinations and residual risks must remain visible.

ISAC sensing can contribute to warning and situational awareness; it cannot guarantee protection of a cellular tower. Detection is not identification, identification is not intent, and an unidentified object must not automatically be classified as hostile.

## Safety and authorization boundaries

Here, "destructive testing" means intentional software/data fault injection and controlled resilience stress, **not destruction of infrastructure**.

- Use synthetic scenes, authorized recorded-data replay, software-in-the-loop (SIL), hardware-in-the-loop (HIL), or conducted/shielded RF facilities with approved limits.
- Authorized live exercises use non-weaponized cooperative aircraft, approved operators, controlled airspace/site permissions, and a documented abort plan. A noncooperative-target model belongs in simulation; do not disable legally required aircraft identification in a live exercise.
- Do not perform live attacks, weapon use, interception, aircraft contact, RF interference, GNSS spoofing, or destructive tower/power/backhaul actions. Represent those effects only through safe models, recorded data, or isolated test interfaces.
- Response authorization, rejection, and interlock cases use mocked interfaces disconnected from real effectors. This catalogue provides no engagement tactics, targeting parameters, or counter-drone defeat procedures.
- Do not inject faults into a production cellular network or disrupt emergency calls. Use isolated networks, test traffic, synthetic identities, and non-sensitive evidence.
- The test director, network owner, aviation/spectrum authorities where applicable, and independent safety reviewer must approve scope. Applicable law and authorization vary by jurisdiction; wartime conditions do not establish permission.

## Why gNodeB ISAC alone is insufficient

Communication coverage does not establish sensing coverage. Object observability depends on geometry, clutter, propagation, synchronization, calibration, available bandwidth, radio architecture, and processing resources. Antenna placement optimized for cellular users may leave sensing gaps. Shared communication/sensing resources can create a service-continuity tradeoff.

Radar-like observations generally cannot establish operator identity, payload, authorization, or hostile intent. Remote ID, when lawfully available, is a separate input, not proof of safety or complete identity. EO/IR, dedicated radar, passive RF, and other authorized sensors have different failure modes; fusion can also introduce correlated errors.

Protection therefore requires layered safety governance, independent confirmation where available, uncertainty-aware operator workflows, infrastructure resilience, and coordination with authorized responders. This catalogue tests those interfaces without prescribing military deployment or engagement.

## Supported-mode and radio inventory

These are coverage axes, not a claim that every combination is standardized, implemented, or physically possible. Record exact product/firmware capability, architecture, approved operating envelope, and supporting evidence before selecting a value. Unsupported combinations require a reason and review, not a passing result.

| Axis | Values to inventory | Required qualification |
|---|---|---|
| Objective `M` | `M1` communication-centric; `M2` sensing-centric; `M3` joint communication/sensing; `M4` sensing unavailable/inhibited with communication fallback | Local operating policies, not universal standardized mode names; protect communication service budgets in every supported mode. |
| Geometry `G` | Monostatic; bistatic; multistatic; passive/opportunistic observation | Record transmitter/receiver roles and clock dependencies. Passive observation is an architecture attribute and need not be mutually exclusive with geometry. |
| Participation `P` | Cooperative target; noncooperative target model; cooperating/noncooperating sensing nodes | Distinguish target cooperation from infrastructure cooperation; live aircraft remain authorized and cooperative. |
| Radio integration `R` | Integrated gNodeB sensing radio; separate network-controlled radio; dedicated radar interface; passive receiver; shielded/conducted SDR prototype | A conventional gNodeB or SDR is not automatically an ISAC sensor. External sensors do not become 3GPP ISAC merely by sharing an interface. |
| Sensor combination `X` | Radio only; radio plus lawful EO/IR; radio plus dedicated radar; radio plus Remote ID; other approved fusion | Declare data rights, trust boundaries, independent/common failure sources, and the behavior when one input is missing. |
| RF configuration `D` | Supported TDD/FDD; half/full duplex if implemented; same/separate carrier; supported bands, bandwidths, polarization and antenna arrangements | Use exact approved device configurations, not assumed equivalence across FR1/FR2, duplex schemes, or waveform implementations. Full-duplex sensing is implementation dependent. |
| Resource/illumination policy `W` | Alternating/concurrent sensing and communication; shared/dedicated time/frequency/spatial resources; downlink/uplink/external illumination; supported beam policies | Qualify only implemented arrangements and legal emissions. A proposed waveform, beam policy or uplink-based prototype is not automatically a standardized gNodeB sensing mode. |
| Topology `N` | Single/multiple sites; standalone or non-standalone where supported; edge/central processing; connected/disconnected backhaul | Specify core, transport, timing, aggregation, and external-service dependencies. |
| Coverage/state `U` | In/out/edge of communication coverage; sensing-covered/unobservable; UE absent/present; supported RRC states | Communication, sensing, and UE state are separate axes. A UE is not necessarily required for network sensing. |
| Lifecycle `L` | Startup; calibration; normal; transition; degraded; maintenance; shutdown; recovery | Include transitions and the interval in which results are not trustworthy. |
| Environment `V` | Clear; modeled precipitation/fog; lighting variation; static/dynamic clutter; occlusion; multipath; ambient RF occupancy | Use qualified recordings/models or an approved benign live envelope; do not create hazardous weather or interference. |
| Load `Q` | Approved minimum/nominal/maximum communication, object, sensor, and compute loads | Include burst and sustained workloads within equipment safety limits. |
| Fault set `F` | Single failures; independent and common-cause combinations; recovery failures | Fault effects are injected through isolated software, emulators, and approved lab interfaces. |

For each radio, record model, firmware, sensing capability evidence, calibration procedure, supported axis values, clock source, observation format, uncertainty representation, health reporting, safe operating limits, and rollback procedure. Record simulated/prototype-only capabilities separately from deployed capabilities.

## Traceability and execution contract

Each matrix row below is a **scenario template**. Expand it into uniquely identified instances for every applicable configuration and requirement. Do not mark the template itself passed because one configuration passed.

Minimum instance record:

```text
instance_id: TC-001/<configuration-id>/<condition-id>/<repetition-id>
requirement_ids: approved local requirement identifiers
source_ids: bibliography identifiers + exact applicable clauses, if any
configuration: M/G/P/R/X/D/W/N/U/L/V/Q/F values + software/model versions
applicability: applicable | excluded-with-reviewed-rationale
facility_and_authorization: isolated test boundary, permits, safety approval
stimulus: synthetic/replay/HIL/shielded RF/authorized benign live
ground_truth: provenance, uncertainty, time reference, scoring windows
threshold_profile: approved version + actual limits + approver + approval date
stop_plan: triggers + independent monitor + owner + safe termination action
evidence: artifact locations, hashes, timestamps, logs, counters, decisions
result: not-run | pass | fail | blocked | aborted | excluded
coverage: exercised values, transitions, combinations, repetitions, omissions
residual_risk_and_disposition: owner, rationale, review and retest requirement
```

Missing approval, ground truth, a required threshold, or a functioning stop monitor means **blocked**, not pass. An abort is not a pass and requires disposition before retest. Preserve the observed failure even when recovery succeeds.

### Local requirement families

These IDs organize local requirements; they are not claims of conformance to a standard.

| ID | Required outcome |
|---|---|
| `REQ-SEN` | Characterized sensing coverage, detection performance, localization, and tracking uncertainty |
| `REQ-UNC` | Explicit unknown/ambiguous state, calibrated confidence, and no inferred hostility |
| `REQ-COM` | Cellular availability, latency, throughput, and emergency-service continuity within approved budgets |
| `REQ-RAD` | Radio calibration, timing, RF-chain integrity, and legal/safe operating envelope |
| `REQ-DAT` | Fresh, attributable, correctly ordered, privacy-controlled sensor and decision data |
| `REQ-RES` | Bounded degradation, fault isolation, rollback, and verified restoration |
| `REQ-HUM` | Usable operator notification, acknowledgement, escalation, and authorization controls |
| `REQ-SAF` | Independent stop authority, controlled live exercises, and inhibited hazardous actions |

### Acceptance profiles

All limits must be set **before execution** by accountable system/safety owners for each configuration. There are deliberately no invented universal detection ranges, deadlines, probabilities, or radio limits.

| Profile | Measured quantities and required acceptance rule |
|---|---|
| `A-SEN` | Detection/miss rate, false alarms per declared time/area, localization/velocity errors and uncertainty coverage; satisfy approved bounds in each required scene stratum, not only pooled averages. |
| `A-TRK` | Track continuity, association/identity-swap rate, stale-track age, reacquisition time, end-to-end observation age; satisfy approved bounds and suppress invalid estimates. |
| `A-UNC` | Unknown/ambiguous decision behavior, confidence calibration and unsupported class assertions; match approved decision rules, including no hostility assertion from unknown identity alone. |
| `A-COM` | Test-session availability, loss, latency percentiles, throughput and resource occupancy; remain within the approved service budget under the specified sensing load. |
| `A-RAD` | Calibration residuals, clock offset/drift, radio health and equipment limits; remain within approved validity limits or explicitly invalidate dependent observations. |
| `A-DAT` | Age, ordering, schema/unit validation, provenance, access decisions and audit completeness; satisfy approved bounds and reject or quarantine invalid/untrusted inputs visibly. |
| `A-RES` | Fault detection/isolation delay, degraded-state declaration, restoration time, state consistency and rollback correctness; meet approved limits with no false healthy state. |
| `A-HUM` | Alarm delivery/acknowledgement/escalation latency, decision correctness and operator workload; satisfy approved workflow rules and usability criteria. |
| `A-SAF` | Stop/interlock/authorization outcomes and reaction deadlines; no unauthorized action or real effector command, and every prescribed stop reaches the approved safe state. |

Specify units, scoring denominators, matching rules, warm-up periods, measurement uncertainty, repetitions, confidence intervals, missing-data policy, and acceptance confidence in the approved profile. Separate detection, classification, and operator notification latency; an average must not hide a required tail-latency or worst-stratum failure.

### Evidence and safe-stop codes

Evidence must use synchronized timestamps with measured clock uncertainty, independent ground truth where applicable, configuration identifiers, and an immutable run identifier.

| Code | Evidence to retain |
|---|---|
| `E1` | Authorized scene truth/model seed, annotated observations, detections, tracks, confidence/uncertainty, and scoring output |
| `E2` | Communication test traffic, session outcomes, service KPIs, resource allocation, and scheduler counters |
| `E3` | Radio/timing/calibration health, approved lab instrument readings, and facility-limit records |
| `E4` | Fault schedule, component health, queues, state transitions, alarms, rollback and recovery logs |
| `E5` | Input provenance, schema/age/access decisions, audit records, and artifact-integrity checks |
| `E6` | Mock-response calls, interlock states, operator actions, approvals, notifications, and stop/exercise logs |

Every instance needs a monitored trigger and named stop owner. The safety plan must specify what happens if the test system itself becomes unresponsive.

| Code | Stop trigger and required safe outcome |
|---|---|
| `S1` | Equipment, RF containment, thermal or electrical limit approached, or facility monitor lost: terminate stimulus using the independent lab control and place equipment in its approved safe state. |
| `S2` | Communication service budget crossed or unintended production coupling detected: end injection, preserve evidence and restore the isolated baseline; do not continue on a live network. |
| `S3` | Required truth, clock validity, data integrity, or uncertainty indication lost: pause scoring, mark results invalid/degraded, and stop dependent automated decisions. |
| `S4` | Recovery deadline exceeded, rollback fails, or fault escapes isolation: stop injection, inhibit unsafe outputs, and invoke the approved isolated restoration plan. |
| `S5` | Missing authorization/interlock, uncontrolled mocked action, operator overload, or unavailable stop authority: inhibit response outputs and end the exercise through independent control. |
| `S6` | Live-exercise boundary, permission, aircraft-control, uninvolved-aircraft/person separation, or weather limit breached: terminate via the approved aviation safety plan and coordinate with the authorized operator. |

Stop codes are mandatory minimums, not an exhaustive safety plan. A failed acceptance metric is recorded as a failure even if it does not require immediate physical termination.

## Traceable scenario coverage matrix

**Coverage notation:** `ALL` means expand across every applicable inventoried value of the named axes, not execute impossible combinations. A named profile requires every relevant metric in that profile plus the case-specific outcome below. Multiple profiles are conjunctive. The source/requirement mapping is local design traceability, not a standards certification.

### Sensing, identity, and environmental conditions

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-001 | Reference scene; `M/G/R/D=ALL` supported sensing configurations | Qualified synthetic/reference replay, then authorized benign confirmation where permitted | E1,E2,E3 | A-SEN,A-COM,A-RAD; meet baseline bounds and declare valid sensing envelope | S1,S2,S3 | REQ-SEN,REQ-COM,REQ-RAD |
| TC-002 | No-object scene and false alarms; `V/Q=ALL` | Empty-scene recordings with labeled clutter | E1 | A-SEN,A-UNC; false-alarm denominator defined; no invented object/hostility labels | S3 | REQ-SEN,REQ-UNC |
| TC-003 | Unidentified versus authorized object; `P/X=ALL` | Synthetic metadata present, absent, ambiguous and conflicting | E1,E5,E6 | A-UNC,A-DAT; unknown remains unknown and authorization remains a separate decision | S3,S5 | REQ-UNC,REQ-DAT,REQ-SAF |
| TC-004 | Benign confusers; `V/X=ALL` | Labeled birds, aircraft and moving clutter in authorized datasets | E1 | A-SEN,A-UNC; measure per-class confusion and retain ambiguous classifications | S3 | REQ-SEN,REQ-UNC |
| TC-005 | Visibility/propagation changes; `V/R/X=ALL` | Qualified weather/lighting model or replay | E1,E3 | A-SEN,A-UNC; report stratum-specific degradation and unsupported conditions | S1,S3 | REQ-SEN,REQ-UNC |
| TC-006 | Occluded or unobservable object; `G/U/V=ALL` | Scene replay with declared observation gaps | E1,E4 | A-TRK,A-UNC; declare unobservable/stale state rather than a confident extrapolation | S3 | REQ-SEN,REQ-UNC |
| TC-007 | Multipath/duplicate observations; `G/V=ALL` | Channel/scene simulator within approved models | E1,E3 | A-SEN,A-TRK; quantify ghost/duplicate tracks and uncertainty | S1,S3 | REQ-SEN,REQ-RAD |
| TC-008 | Multiple objects and association ambiguity; `G/X/Q=ALL` | Labeled multi-object synthetic/replay scenes | E1,E4 | A-TRK,A-UNC; bound association errors and expose unresolved identities | S3 | REQ-SEN,REQ-UNC |
| TC-009 | Observation gap and reacquisition; `L/U=ALL` | Pause/resume a replay stream | E1,E4 | A-TRK; stale tracks expire and reacquisition does not silently inherit identity | S3,S4 | REQ-SEN,REQ-RES |
| TC-010 | Sensing/communication boundary mismatch; `U/N=ALL` | Independent modeled communication and sensing availability | E1,E2,E4 | A-SEN,A-COM,A-UNC; no sensing-coverage claim based only on communication coverage | S2,S3 | REQ-SEN,REQ-COM,REQ-UNC |
| TC-011 | Cooperative versus noncooperative target model; `P/G=ALL` | Metadata removal only in simulation/replay | E1,E5 | A-SEN,A-UNC; characterize dependency on cooperation without assuming live target cooperation | S3 | REQ-SEN,REQ-UNC |
| TC-012 | Sensor modality disagreement; `X=ALL` fusion combinations | Replay intentionally inconsistent but labeled sensor outputs | E1,E5,E6 | A-UNC,A-DAT; conflict visible, provenance retained, no unsupported certainty | S3,S5 | REQ-UNC,REQ-DAT |

### ISAC modes and sensing-capable radio configurations

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-013 | Communication-centric scheduling; `M1/D/Q=ALL` | Approved synthetic communication and sensing demand | E1,E2 | A-SEN,A-COM; quantify sensing degradation while preserving service budget | S1,S2 | REQ-SEN,REQ-COM |
| TC-014 | Sensing-centric scheduling; `M2/D/Q=ALL` | Isolated configured resource-policy change | E1,E2 | A-SEN,A-COM; sensing priority never silently overrides mandatory service limits | S1,S2 | REQ-SEN,REQ-COM |
| TC-015 | Joint operation; `M3/D/W/Q=ALL` | Concurrent/alternating bounded synthetic workloads under supported resource policies | E1,E2,E4 | A-SEN,A-COM; simultaneous bounds hold, not just separate unloaded benchmarks | S1,S2 | REQ-SEN,REQ-COM |
| TC-016 | Sensing inhibition/fallback; `M4/L=ALL` | Disable sensing through approved isolated control | E2,E4,E6 | A-COM,A-RES,A-UNC; unavailable state visible; no fresh-looking sensing output | S2,S4 | REQ-COM,REQ-RES,REQ-UNC |
| TC-017 | Every supported mode transition; `M/L=ALL` directed transitions | Exercise approved transition graph in SIL/HIL | E1,E2,E4 | A-TRK,A-COM,A-RES; account for transients, invalid observations and rollback | S2,S3,S4 | REQ-SEN,REQ-COM,REQ-RES |
| TC-018 | Monostatic radio health; applicable `G/R/D` | Conducted/shielded emulator varying approved leakage/residual model | E1,E3 | A-SEN,A-RAD; radio-validity limits enforced and observations invalidated when exceeded | S1,S3 | REQ-SEN,REQ-RAD |
| TC-019 | Bistatic alignment; applicable `G/N` | Isolated timing/geometry metadata perturbation | E1,E3,E5 | A-SEN,A-RAD,A-DAT; detect invalid alignment and suppress misleading estimates | S1,S3 | REQ-SEN,REQ-RAD,REQ-DAT |
| TC-020 | Multistatic node loss/disagreement; applicable `G/N` | Drop or delay synthetic node observations | E1,E3,E4 | A-TRK,A-RES; degraded coverage/uncertainty reflects surviving valid nodes | S3,S4 | REQ-SEN,REQ-RES |
| TC-021 | Passive illumination unavailable; passive `G/R` | Remove modeled illuminator from replay | E1,E3,E4 | A-SEN,A-UNC; absence of illumination is not reported as absence of objects | S3 | REQ-SEN,REQ-UNC |
| TC-022 | External radar/passive/SDR interface compatibility; `R/X=ALL` | Golden and invalid sample/interface fixtures in isolation | E1,E3,E5 | A-RAD,A-DAT; units, frames, calibration and validity preserve their meaning | S1,S3 | REQ-RAD,REQ-DAT |
| TC-023 | Duplex/carrier/band/beam/illumination changes; `D/W=ALL` supported edges | Approved reconfiguration in shielded/conducted HIL | E1,E2,E3 | A-SEN,A-COM,A-RAD; independently qualify each configuration and transition, including observation gaps | S1,S2,S3 | REQ-SEN,REQ-COM,REQ-RAD |
| TC-024 | UE state and network architecture dependencies; `N/U=ALL` | Isolated UE/core state emulator and test sessions | E1,E2,E4 | A-SEN,A-COM,A-RES; expose actual dependency, including unsupported/UE-absent conditions | S2,S4 | REQ-SEN,REQ-COM,REQ-RES |
| TC-025 | Calibration drift or invalid calibration; `R/D/L=ALL` | Perturb calibration metadata in simulator | E1,E3,E4 | A-RAD,A-UNC; detect invalidity, withhold confidence and require approved recalibration | S1,S3 | REQ-RAD,REQ-UNC |
| TC-026 | Timing source drift/loss; `G/N/R=ALL` | Clock fault through an isolated emulator, never over-air spoofing | E1,E3,E4 | A-RAD,A-TRK,A-RES; identify dependent invalid observations and bounded recovery | S3,S4 | REQ-RAD,REQ-SEN,REQ-RES |

### Data, service, and infrastructure fault injection

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-027 | Stale/reordered/duplicate observations; `X/N/Q=ALL` | Replay transport faults at isolated interfaces | E1,E4,E5 | A-DAT,A-TRK; age/order rules enforced with visible rejection or quarantine | S3,S4 | REQ-DAT,REQ-SEN |
| TC-028 | Invalid schema, units or reference frame; `R/X=ALL` | Bounded invalid fixtures in test-only input adapter | E1,E5 | A-DAT,A-UNC; reject/quarantine visibly; no silently plausible converted track | S3 | REQ-DAT,REQ-UNC |
| TC-029 | Missing/untrusted input provenance; `X/N=ALL` | Synthetic unauthorized/stale-credential requests | E5,E6 | A-DAT,A-SAF; deny unauthorized inputs/actions with attributable audit evidence | S3,S5 | REQ-DAT,REQ-SAF |
| TC-030 | Sensor disconnection or RF-chain health loss; `R/X=ALL` | HIL health signal or replay-stream disconnect | E1,E3,E4 | A-RAD,A-RES,A-UNC; detect outage and stop presenting stale data as healthy | S1,S3,S4 | REQ-RAD,REQ-RES,REQ-UNC |
| TC-031 | Compute/accelerator pressure; `M/Q/N=ALL` | Bounded synthetic load in isolated compute | E1,E2,E4 | A-TRK,A-COM,A-RES; load shedding preserves declared service and observation-age rules | S1,S2,S4 | REQ-SEN,REQ-COM,REQ-RES |
| TC-032 | Queue/storage pressure and evidence loss; `Q/N=ALL` | Quota-limited test storage and bounded queue load | E4,E5,E6 | A-DAT,A-RES; evidence loss visible; no success claim when required evidence is absent | S3,S4 | REQ-DAT,REQ-RES |
| TC-033 | Backhaul delay, loss or disconnection; `N/Q=ALL` | Isolated network emulator | E1,E2,E4 | A-TRK,A-COM,A-RES; bounded local operation and visible loss of external dependencies | S2,S3,S4 | REQ-SEN,REQ-COM,REQ-RES |
| TC-034 | Core/control-service unavailable; `N/L=ALL` | Stop isolated mock service | E2,E4,E6 | A-COM,A-RES; expose unavailable functions without unsafe retry storms | S2,S4 | REQ-COM,REQ-RES |
| TC-035 | Power-state transition or restart; `R/N/L=ALL` | Approved power-state HIL model or software restart | E2,E3,E4 | A-COM,A-RAD,A-RES; no physical mains manipulation; validate readiness before healthy state | S1,S2,S4 | REQ-COM,REQ-RAD,REQ-RES |
| TC-036 | Thermal warning/derating; `R/Q/L=ALL` | Simulated health input; do not overheat equipment | E2,E3,E4 | A-RAD,A-COM,A-RES; derating and shutdown respect approved equipment/service policies | S1,S2,S4 | REQ-RAD,REQ-COM,REQ-RES |
| TC-037 | Component crash and restart loop; `N/L=ALL` | Controlled failure of isolated process/container | E1,E2,E4 | A-RES,A-TRK,A-COM; no stale-state resurrection or unbounded restart | S2,S3,S4 | REQ-RES,REQ-SEN,REQ-COM |
| TC-038 | Model/configuration update and rollback; `M/R/L=ALL` | Versioned approved test update, including incompatible fixture | E1,E4,E5 | A-SEN,A-DAT,A-RES; reject incompatibility, retain provenance and restore qualified version | S3,S4 | REQ-SEN,REQ-DAT,REQ-RES |
| TC-039 | Redundant-node failover and split view; `N/G=ALL` | Isolated partition/failover emulator | E1,E4,E5 | A-TRK,A-DAT,A-RES; avoid duplicate authoritative decisions and reconcile explicitly | S3,S4,S5 | REQ-SEN,REQ-DAT,REQ-RES |
| TC-040 | Alarm delivery/acknowledgement path failure; `N/L/Q=ALL` | Disable mock notification endpoint | E4,E6 | A-HUM,A-RES; unavailable delivery and escalation visible; no false acknowledgement | S4,S5 | REQ-HUM,REQ-RES |

### Operator safeguards and authorized benign live exercises

No row in this section authorizes an attack, physical engagement, or RF disruption. Validate faults and response logic in isolation before any separately approved live confirmation.

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-041 | Benign live detection/tracking confirmation; approved `M/R/V` subset | Authorized cooperative non-weaponized aircraft within permitted envelope | E1,E2,E3,E6 | A-SEN,A-TRK,A-COM,A-SAF; independent truth and service bounds; no response actuation | S1,S2,S3,S6 | REQ-SEN,REQ-COM,REQ-SAF |
| TC-042 | Uninvolved aircraft/person or boundary incursion | Tabletop rehearsal; live stop observation only if independently safe | E6 | A-SAF; execute approved abort plan without pursuing or interacting with uninvolved aircraft | S5,S6 | REQ-SAF |
| TC-043 | Exercise permission or operator-control loss | Tabletop/mocked loss notification; no deliberate live control loss | E4,E6 | A-SAF,A-HUM; independent stop authority and responsible operator receive correct escalation | S5,S6 | REQ-SAF,REQ-HUM |
| TC-044 | Human ambiguity and uncertainty display; `X/Q=ALL` | Recorded unknown/conflicting scenes in operator simulator | E1,E6 | A-UNC,A-HUM; display age, confidence, disagreement and missing identity without hostility inference | S3,S5 | REQ-UNC,REQ-HUM |
| TC-045 | Alarm burst and operator handover; `Q/L=ALL` | Bounded synthetic alarms in tabletop simulator | E4,E6 | A-HUM,A-SAF; preserve priority, ownership and acknowledgement under approved workload | S5 | REQ-HUM,REQ-SAF |
| TC-046 | Missing/expired authorization for mocked response | Synthetic requests to disconnected response simulator | E5,E6 | A-SAF,A-DAT; deny request; record reason and actor; no real effector interface | S5 | REQ-SAF,REQ-DAT |
| TC-047 | Human approval absent or withdrawn | Mock operator workflow with approval withheld/revoked | E6 | A-SAF,A-HUM; no automated engagement and no action after withdrawal | S5 | REQ-SAF,REQ-HUM |
| TC-048 | Stop/interlock failure or lost controller heartbeat | Isolated mock interface with independent test cutoff | E4,E6 | A-SAF,A-RES; unavailable control inhibits outputs and independent stop remains effective | S4,S5 | REQ-SAF,REQ-RES |
| TC-049 | Authorized responder notification and handoff | Mock notification and tabletop responder coordination | E5,E6 | A-HUM,A-DAT; uncertainty/provenance retained; no claim that notification equals protection | S3,S5 | REQ-HUM,REQ-DAT |
| TC-050 | Evidence retention, access and privacy | Synthetic incident artifacts and approved retention-policy fixtures | E5,E6 | A-DAT; least-authorized access, integrity verification and retention/deletion rules demonstrated | S3,S5 | REQ-DAT |

### Selected compound failures and restoration

These are mandatory risk-review candidates, not an exhaustive list of combinations. A site hazard assessment determines additional common-cause and higher-order cases.

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-051 | Degraded scene plus peak communication demand; `V/Q/M=ALL` applicable | Replay scene plus isolated traffic generator | E1,E2,E4 | A-SEN,A-COM,A-UNC; report sensing degradation without sacrificing approved service budget | S1,S2,S3 | REQ-SEN,REQ-COM,REQ-UNC |
| TC-052 | Timing loss plus multistatic-node loss | Combined isolated clock/node emulator faults | E1,E3,E4 | A-RAD,A-TRK,A-RES; no falsely precise fused result or premature recovery | S3,S4 | REQ-RAD,REQ-SEN,REQ-RES |
| TC-053 | Compute pressure plus stale-data backlog | Bounded load and replay delay | E1,E4,E5 | A-TRK,A-DAT,A-RES; shed stale work and visibly mark lost timeliness | S1,S3,S4 | REQ-SEN,REQ-DAT,REQ-RES |
| TC-054 | Sensor disagreement plus unavailable operator notification | Conflicting replay and mock notification outage | E1,E4,E6 | A-UNC,A-HUM,A-SAF; retain uncertainty and inhibit mocked action without authorization | S3,S5 | REQ-UNC,REQ-HUM,REQ-SAF |
| TC-055 | Shared power/timing/backhaul dependency loss | Common-cause model in SIL/HIL, no live infrastructure disruption | E2,E3,E4 | A-COM,A-RAD,A-RES; expose correlated loss rather than assume independent redundancy | S1,S2,S4 | REQ-COM,REQ-RAD,REQ-RES |
| TC-056 | Restart plus stale model/configuration state | Isolated restart with version-mismatched fixtures | E1,E4,E5 | A-DAT,A-RES; reject incompatible state before declaring readiness | S3,S4 | REQ-DAT,REQ-RES |
| TC-057 | Redundancy failover plus evidence-store outage | Isolated partition and quota-limited evidence service | E4,E5,E6 | A-DAT,A-RES; make missing evidence and authority ownership explicit | S3,S4,S5 | REQ-DAT,REQ-RES |
| TC-058 | Stop request during mode change/recovery | Mock stop while isolated transition is in progress | E2,E4,E6 | A-SAF,A-RES; stop takes precedence and recovery cannot re-enable inhibited outputs | S2,S4,S5 | REQ-SAF,REQ-RES |
| TC-059 | Recovery after compound degraded operation; `L/N=ALL` | Remove emulated faults in controlled order | E1,E2,E3,E4 | A-SEN,A-COM,A-RAD,A-RES; recalibrate/revalidate dependencies before declaring restored service | S1,S2,S3,S4 | REQ-SEN,REQ-COM,REQ-RAD,REQ-RES |
| TC-060 | Repeated fault/recovery cycles and sustained observation | Approved-duration synthetic endurance run | E1,E2,E4,E5 | A-TRK,A-COM,A-DAT,A-RES; bound resource growth, state drift and recurring failures | S1,S2,S3,S4 | REQ-SEN,REQ-COM,REQ-DAT,REQ-RES |

## Coverage accounting and release gate

Maintain a versioned coverage ledger using the instance fields above. A spreadsheet, test-management system, or structured data export is acceptable; this README is not an execution database.

1. Freeze the supported configuration inventory and local requirements. Map source clauses only where actually applicable; explicitly distinguish normative requirements, recommendations, and local design choices.
2. Expand each scenario over applicable axis values and all supported directed lifecycle/mode transitions. Record constraints for impossible or prohibited combinations and obtain independent review.
3. Execute reference/boundary/single-fault cases, then a constrained pairwise interaction suite and risk-selected higher-order/common-cause cases. Do not describe the pairwise suite as exhaustive.
4. For a literal exhaustive bounded-combination claim, enumerate and execute **every feasible combination in the declared finite domain**, including declared fault sequences and bounded timing/value partitions. State unmodeled continuous values and omitted dimensions. If that is infeasible, report partial/risk-based coverage instead.
5. Link every requirement and expected observable outcome to instances, acceptance-profile versions, results, evidence, and residual-risk disposition. Independently validate the ground-truth and scoring method.
6. Require review of failures, aborts, exclusions, missing evidence, uncertainty, and restoration results. A waiver does not convert an unexecuted or failed test into a pass.
7. Rebaseline and rerun affected cases after changes to firmware, models, radio configuration, dependencies, approved limits, or operating environment.

Report at least these separate measures; never collapse them into one unexplained percentage:

| Measure | Numerator / denominator |
|---|---|
| Requirement evidence completeness | Applicable requirements with reviewed acceptance evidence / all applicable requirements |
| Instance execution | Completed pass-or-fail instances / all applicable enumerated instances; show blocked, aborted and not-run counts separately |
| Instance pass rate | Passed instances / all applicable enumerated instances; do not remove failures or unexecuted cases |
| Axis and transition coverage | Exercised approved values/edges / all applicable approved values/edges |
| Interaction coverage | Exercised feasible combinations at each declared interaction strength / all feasible combinations at that strength |
| Fault/recovery coverage | Exercised declared fault effects, sequences and restoration outcomes / all applicable declared items |
| Exclusion review | Reviewed exclusions / all proposed exclusions, with reasons and risk owners |

**Current coverage:** not assessed. All TC-001 through TC-060 are templates awaiting configuration-specific instantiation, approval and execution. There are no measured pass rates or validated protection claims in this repository.

Suggested claim format:

> Catalogue revision [commit] covers the declared [system/configuration/requirements baseline]. Of [N] applicable enumerated instances, [P] passed, [F] failed, [B] were blocked, [A] aborted and [U] were not run. Interaction coverage is [strength and feasible combinations]. Reviewed exclusions and residual risks are [references]. Exhaustiveness applies only to [explicit finite domain]; no universal attack coverage or guaranteed infrastructure protection is claimed.

## References and standards applicability

Source-to-case mappings and exact edition/clauses must be recorded in instance records. A research framework or study is not evidence that a commercial gNodeB implements interoperable ISAC. Verify the applicable 3GPP release, product capability, regulatory permissions and certification separately.

- **SRC-RES:** NIST SP 800-160 Vol. 2 Rev. 1, *Developing Cyber-Resilient Systems: A Systems Security Engineering Approach*: https://doi.org/10.6028/NIST.SP.800-160v2r1. Resilience engineering guidance for REQ-RES, REQ-DAT and recovery/compound-fault cases; not an ISAC performance specification.
- **SRC-RISK:** NIST SP 800-30 Rev. 1, *Guide for Conducting Risk Assessments*: https://doi.org/10.6028/NIST.SP.800-30r1. Risk-assessment guidance supporting applicability, compound-failure selection, exclusions and residual-risk review across all cases.
- **SRC-IMT:** ITU-R Recommendation M.2160, *Framework and overall objectives of the future development of IMT for 2030 and beyond*: https://www.itu.int/rec/R-REC-M.2160. Framework context for integrated sensing and communication; not proof of implemented gNodeB features, radio conformance, or counter-drone performance.
- **SRC-3GPP:** 3GPP TR 22.837, *Study on Integrated Sensing and Communication*: https://www.3gpp.org/ftp/Specs/archive/22_series/22.837/. Study context for use cases and requirements investigation. A Technical Report is not a normative Technical Specification and does not establish commercial implementation or interoperability.
- **SRC-ETSI:** ETSI ISG ISAC deliverables portal: https://www.etsi.org/committee/isac. Consult the current published use-case, deployment, architecture and channel-modeling reports when qualifying the inventory. Record the exact document, edition and applicable clauses before using it as instance-level evidence; a Group Report is not a product certification.

**Source-verification status:** the research pass supplied candidate standards references, but independent retrieval of the ITU/3GPP/ETSI sources was unavailable in this session. Their current editions, release applicability and clause-level mappings remain verification prerequisites, not completed checks. No unverified release/date, normative compliance, or regulatory-authority claim is used as an acceptance criterion here.

Local traceability: TC-001 through TC-026 require REQ-SEN/REQ-RAD capability and performance requirements supplied by the actual system owner; this catalogue does not invent normative radio thresholds. TC-027 through TC-040 and TC-051 through TC-060 use SRC-RES/SRC-RISK as engineering guidance. TC-041 through TC-050 additionally require jurisdiction-specific aviation, spectrum, privacy and site permissions; no general reference substitutes for those approvals.

SRC-IMT/SRC-3GPP/SRC-ETSI provide background for the mode/radio inventory and TC-001 through TC-026; they do not supply automatic pass/fail thresholds. Any normative claim must instead identify a verified applicable specification and product requirement. Aviation authorization, spectrum authorization, privacy compliance, and authority to take any response action are separate determinations.
