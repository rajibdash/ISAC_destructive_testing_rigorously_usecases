# ISAC defensive resilience and fault-injection test catalogue

This repository collects safety-bounded testing use cases for integrated sensing and communication (ISAC), gNodeBs, sensing-capable radios, devices, core-network services, and cellular-site continuity when an unidentified drone is observed near critical infrastructure. It addresses detection, uncertainty, operator notification, service continuity, and recovery, including simulated wartime-like infrastructure degradation and an explicitly declared architecture with core-hosted AI.

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

## Core-network and AI-domain responsibilities

The original radio-focused catalogue treated core failure mainly as a dependency outage (TC-024, TC-033, TC-034). That was insufficient: a healthy radio and accurate local detector can still produce an unusable end-to-end service if core admission, identity, transport, policy, sensing coordination, analytics, AI serving, or operator delivery fails. TC-061 through TC-128 extend the baseline without replacing the radio tests.

**Architecture qualification:** "6G Core" and "AI domain in the core" describe the system under test, not a standardized architecture asserted by this README. Inventory the actual functions, contracts, implementation status and applicable specification editions. The 5G Core functions below are established architectural reference points; do not relabel them as finalized 6G functions or assume that a sensing orchestrator or object-identification AI is a standardized network function.

NWDAF (Network Data Analytics Function) provides specified network analytics in supported 5GS implementations. It is not, merely by being present, an object-identification engine, a safety authority, or a counter-drone controller. Model training/serving capabilities, sensing management, object fusion, and AI-to-network-control interfaces must each be declared and qualified separately. A normative Stage-1 service requirement does not by itself establish an interoperable core/RAN implementation.

### Responsibility and ownership map

Assign named implementation owners and independent acceptance reviewers for each row. A function may be external to the core, distributed, optional, or absent; document that explicitly rather than silently assigning all work to the gNodeB or to "AI."

| Domain / reference functions | Responsibility to declare and stress | Principal new cases |
|---|---|---|
| Devices, sensing radios and RAN | Observation validity, resource enforcement, health reporting, local uncertainty, supported mobility and disconnected behavior; retain TC-001 through TC-060 | TC-064, TC-078, TC-113, TC-120 |
| Access and subscription: AMF, AUSF, UDM/UDR where applicable | UE registration/mobility, subscriber authentication, authorized device participation and revocation; these do not authenticate a sensed physical object's identity | TC-062, TC-064, TC-068, TC-109 |
| Sessions and user plane: SMF/UPF where applicable | Communication-session lifecycle, sensing-data transport where designed, routing, QoS enforcement, isolation and continuity | TC-063, TC-065, TC-067, TC-083 |
| Policy and exposure: PCF, NSSF, NEF/AF where applicable | Policy/slice selection, admission, authorized exposure, quotas and revocation; RAN and transport must enforce their respective resource decisions | TC-066, TC-067, TC-071, TC-079, TC-082 |
| Service-based core infrastructure: NRF, SCP if deployed, service endpoints | Discovery, routing, overload handling, credential lifecycle and bounded retries with observable errors | TC-069, TC-070, TC-081 |
| Sensing service coordination / fusion application, if implemented | Job/task admission, capabilities, lifecycle/cancellation, observation correlation, uncertainty propagation and consumer notification; hosting and interfaces are deployment specific | TC-061, TC-073, TC-074, TC-078, TC-109 |
| Analytics: NWDAF and declared analytics consumers | Subscription lifecycle, freshness, analytics limitations and scoped recommendations; prohibit accidental substitution of network analytics for object truth | TC-072, TC-106, TC-111 |
| Core-hosted AI platform, if implemented | Data/model governance, preprocessing, training/validation, registry, serving, calibrated abstention, resource isolation, release/rollback and decision provenance | TC-085 through TC-112 |
| Platform / operations / data owners | Shared-failure domains, state consistency, autoscaling, deployment, backup/restore, retention and jurisdiction boundaries across core and AI | TC-075 through TC-082, TC-114 through TC-128 |
| Safety and human operations | Independent stop authority, approval of permitted network-control actions, uncertainty-aware review and responder notification; no AI authority to infer hostility or engage | TC-107, TC-108, TC-112, TC-118, TC-123 |

### Core-hosted AI service contract

Record the actual path, for example: authorized observations -> authenticated ingestion -> schema/time/frame validation -> feature processing -> AI inference/fusion -> uncertainty-aware track service -> authorized consumer/operator. Communication/session establishment, core policy, orchestration, network analytics and model lifecycle are dependencies or control paths, not necessarily serial steps in every observation.

Distinguish physical-object detection, class estimation, track association, cooperative claimed identity, subscriber/device identity, authorization, and intent. Store confidence and provenance for each supported assertion; a subscriber identity, track ID, Remote ID claim or model score cannot substitute for the others.

Define per-hop and end-to-end age/deadline budgets, data rights, allowed consumers, overload behavior, expiry, cancellation and ownership. Carry observation time and clock uncertainty, source/frame/units, job and tenant identifiers, schema/preprocessing/model/calibration versions, and track lineage. Specify what happens without UE attachment, a PDU session, core connectivity, a model, or a required sensor. Do not invent a dependency on a UE/PDU session for a deployment that uses network-side sensing transport.

Core-hosted AI may make the core a shared failure and resource-contention domain. Declare whether inference is advisory only or may request bounded, reversible network-resource changes. Any permitted write path needs independent policy validation, scope/expiry, audit, rate limits and stop authority; it must never control real engagement. Replacing failed AI with a fallback is valid only when that fallback is separately qualified and visibly reports its limitations; "unavailable/unknown" is preferable to fabricated healthy output.

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
| Core/service placement `C` | Central/regional/edge core; core-hosted AI; split core/edge/device AI; local or federated sensing service; supported inter-operator arrangements | Inventory actual service/function versions, APIs, dependency graph, shared-failure domains, state ownership and trust/jurisdiction boundaries. |
| Core load `B` | UE registrations; session churn; mobility; API requests; sensing jobs; subscriptions/consumers; data throughput; tenants/slices | Declare bounded baseline, burst, ramp, sustained, admission-limit and recovery load values separately; distinguish offered, admitted, rejected and completed work. |
| AI configuration `J` | Enabled/unavailable; advisory/bounded network-control permission; model/preprocessing versions; inference runtime/precision; batch policy; single/multi-modal; optional distributed training or generative assistant | Inventory only implemented features; training, analytics, inference, fusion and control are separate capabilities. An excluded optional feature is not a passed case. |
| Governance `H` | Authorized/revoked/expired identity; tenant/slice; data purpose, consent or other legal basis; retention; residency; model approval state | Use synthetic identities and approved fixtures; device authorization is separate from physical-object identity and response authority. |
| Frequency profile `K` | `K-FR2-1`; `K-FR2-2`; `K-SUBTHZ`; mixed-band configuration with explicitly identified component profiles | Instantiate exact legal/supported carriers and configurations, not a single generic "mmWave" value. Apply the frequency-profile overlay below to every scenario. |

For each radio, record model, firmware, sensing capability evidence, calibration procedure, supported axis values, clock source, observation format, uncertainty representation, health reporting, safe operating limits, and rollback procedure. Record simulated/prototype-only capabilities separately from deployed capabilities.

For core and AI services, additionally record service owner, API/schema versions, caller permissions, dependencies, processing/storage locations, model/data lineage, resource reservations, failover/fencing rules, recovery objectives and approved degraded behavior. Apply relevant `M/R/X/N/U/L/V/Q/F` axes to the new core/AI cases as well as `C/B/J/H`; their interaction with radio and device conditions must not disappear from coverage accounting.

## FR2/mmWave and sub-THz configuration overlay

This overlay applies to **every existing case, TC-001 through TC-128**, including core/AI/governance cases, and to TC-129 through TC-152 added below. Frequency-specific tests supplement, not replace, the original requirements and safety controls. The 128-case core/AI baseline is part of this update's branch; the linked main revision `1296dc12edd08d1e1ccab68d20d35e65a14fe63e` contained the earlier 60-case catalogue.

### Frequency classification and implementation status

| Profile | Classification | Qualification boundary |
|---|---|---|
| `K-FR2-1` | NR FR2-1 range: 24.25-52.6 GHz in applicable NR specifications | The range is not a continuous allocation or a guarantee of product support. Select the actual NR operating band, carrier, bandwidth, numerology and device/BS capability from the applicable specification edition and regional authorization. |
| `K-FR2-2` | NR FR2-2 range: 52.6-71 GHz in applicable NR specifications | Qualify separately from FR2-1; do not inherit waveform, channel access, beam, RF or sensing capability merely from the FR2 label. Record any applicable shared-spectrum/channel-access obligations. |
| `K-SUBTHZ` | Experimental sub-THz radio with explicitly declared frequency interval and waveform | "Sub-THz" has no single project-independent boundary here. An implementation may, for example, declare a subset of 100-300 GHz; this is a naming example, not a selected carrier, permission or NR band. Describe any other experimental interval explicitly rather than calling it FR2. |
| Mixed-band | Enumerated FR1/FR2/sub-THz components, if actually implemented | Declare communication and sensing carriers separately, their timing/frame relation, approved inter-band transitions and fallback capabilities. No automatic transfer of calibration, object signatures, AI qualification or coverage between bands. |

"mmWave" is a broad descriptive term, not synonymous with NR FR2; conversely, the conventional 30 GHz millimeter-wave boundary does not change the NR FR2-1 definition. A sub-THz prototype is not automatically a 3GPP NR radio, standardized 6G feature, or interoperable ISAC implementation. Exact standards editions and band tables remain qualification prerequisites.

### Mandatory configuration manifest

For each `K` profile, declare a finite supported set and justified boundary partitions for the following fields. Record `not implemented`, `simulation only`, `lab prototype`, or `qualified hardware` where appropriate. No actual carrier, hardware support or operating permission is claimed by this catalogue.

| Manifest group | Values and dependencies to record |
|---|---|
| Spectrum and waveform | Actual communication and sensing frequencies/bands; occupied/usable bandwidth; waveform and sample rate; supported numerology/duplex; carrier aggregation if implemented; channel-access constraints and authorization. |
| Front end and aperture | Tx/Rx chains; antenna/panel arrangement; analog/hybrid/digital beamforming; codebook/version; supported steering envelope; polarization; aperture-dependent near/far-field model validity; enclosure/radome and mounting configuration. |
| Hardware impairments | Qualified phase-noise/frequency-offset model; LO/multiplier and clock dependencies; PA compression/linearity; receiver noise/dynamic range; ADC/DAC precision/clipping; IQ imbalance; frequency-dependent gain/delay; permitted thermal derating. |
| Calibration and measurement | Frequency/beam/polarization-dependent calibration; phase coherence and timing uncertainty; instrumentation and converter/extender versions; cable/fixture losses; chamber quiet-zone/near-field transformation validity and measurement uncertainty. |
| Propagation and object data | Qualified channel/target-scattering model or authorized measurements per band; blockage, weather/material attenuation and multipath partitions; bistatic/monostatic geometry; model frequency/distance/environment validity. |
| Device and service behavior | Supported UE/panel orientations and power states; beam acquisition/tracking/recovery; configured reference/calibration gaps; sensing observability during beam sweeps; per-band data rates, queue budgets and core transport dependencies. |
| AI and fusion | Per-band training/evaluation provenance and held-out splits; preprocessing/model validity; uncertainty calibration; cross-band association/registration; missing-band behavior and qualified fallback. |
| Limits and safety | Locally authorized emission/exposure, facility, thermal and electrical limits; independent monitors; instrument range; safe shutdown and qualified rollback. No RF output without approved facilities and authorization. |

Conducted tests alone do not characterize an antenna array, beam management, enclosure, or radiated exposure. Use an appropriately qualified shielded OTA chamber where necessary. At sub-THz, unqualified converters, chamber geometry or calibration can dominate the result; mark such measurements blocked rather than claiming hardware validation from a channel simulation. Weather/material and target-scattering models must be validated in their intended frequency/geometry domain, not extrapolated automatically from FR1 or FR2.

### Per-case applicability and inheritance rules

For **every TC-001 through TC-128**, create an applicability entry for every declared exact frequency configuration, including unsupported configurations under review. Its disposition must be `execute`, `reuse-reviewed-evidence`, or `excluded-with-reviewed-rationale`; the resulting instance still uses the result states in the execution contract. Unsupported hardware is excluded or simulation-only as declared, never a hardware pass.

An executable instance inherits its original stimulus constraints, requirement families, acceptance profiles, evidence and stops. Add `A-HF`, `REQ-HF` and `E10` wherever RF/beam/channel effects or their downstream consequences are exercised. Frequency-independent logic tests may reuse evidence only with approved equivalence of code/configuration, interfaces, load envelope and dependencies. Link that evidence separately to each affected configuration; count one execution, not many invented executions. Re-execute when band-dependent event rates, precision, model versions, authorization or failure paths invalidate equivalence.

| Original cases: complete partition of TC-001 through TC-128 | Required FR2/sub-THz overlay |
|---|---|
| TC-001 through TC-012 | Per-band observability, scattering/occlusion/multipath and environmental validity; beam-dependent observation gaps; score misses, confusion and uncertainty independently per band. |
| TC-013 through TC-026 | Supported bandwidth/numerology/resource/beam policies, array/duplex health, calibration and multistatic coherence; no presumed FR2-to-sub-THz mode portability. |
| TC-027 through TC-040 | Per-band sample/feature throughput, timestamps/units, quantization, thermal/compute/transport pressure and restart validity; repeat faults using declared band-specific data envelopes. |
| TC-041 through TC-050 | Band-specific permissions, exposure/facility approval, operator visibility of band/beam uncertainty and interlocks. Apply live cases only with separately authorized qualified hardware; otherwise record the live instance excluded/blocked and retain isolated logic tests. |
| TC-051 through TC-060 | Combine band-valid propagation/beam effects with declared faults and load; restore calibration, beam state and service validity before reporting recovery. |
| TC-061 through TC-084 | Frequency/capability-aware admission, per-band resource/data envelopes, beam-recovery event bursts, transport/policy/fallback lifecycle and explicit rejection of unsupported sub-THz service requests. |
| TC-085 through TC-112 | Per-band datasets/features, hardware-impairment strata, unknown rejection/calibration and model/runtime versions; reject unqualified cross-band AI transfer and control authority. |
| TC-113 through TC-128 | End-to-end age/quality under beam reacquisition, band changes and shared-failure conditions; cross-band identity lineage, core/AI governance and independent stop remain mandatory. |

This table establishes a coverage obligation for every original ID, not completed executions. Finite frequency, beam, hardware-impairment and environment partitions must be declared in the ledger before making a bounded exhaustive claim; continuous physical variation cannot be exhausted by naming three profiles.

## Traceability and execution contract

Each matrix row below is a **scenario template**. Expand it into uniquely identified instances for every applicable configuration and requirement. Do not mark the template itself passed because one configuration passed.

Minimum instance record:

```text
instance_id: TC-001/<configuration-id>/<condition-id>/<repetition-id>
requirement_ids: approved local requirement identifiers
source_ids: bibliography identifiers + exact applicable clauses, if any
configuration: M/G/P/R/X/D/W/N/U/L/V/Q/F/C/B/J/H/K values + software/model versions
frequency_manifest: exact K configuration + waveform/array/calibration/channel versions
frequency_applicability: execute | reuse-reviewed-evidence | excluded-with-reviewed-rationale
evidence_reuse: original run + equivalence review + reviewer + limits, if applicable
ownership_and_path: responsible domain + dependency graph + end-to-end trace path
load_profile: offered/admitted/completed/rejected work + ramp/burst/hold/recovery limits
ai_contract: applicable model/data/feature versions + authority + expiry + fallback
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
| `REQ-CORE` | Authorized and consistent core/service lifecycle, admission, overload handling and end-to-end service contracts |
| `REQ-ID` | Separation and scoped binding of subscriber/device, object, track, tenant and authorization identities |
| `REQ-AI` | Qualified AI performance, abstention, serving timeliness, model compatibility and lifecycle integrity |
| `REQ-CTL` | Independently validated, bounded and reversible permitted network-control recommendations/actions |
| `REQ-GOV` | Purpose-limited data/model use, residency, retention, revocation and accountable approvals |
| `REQ-HF` | Frequency-qualified radio/beam/channel operation, calibrated OTA evidence, bounded degradation and valid downstream core/AI behavior |

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
| `A-CORE` | Admitted/completed/rejected job and API rates, registration/session success and tail latency, queue age, retry amplification, resource use and state convergence; meet approved load/latency/consistency budgets and return explicit bounded overload outcomes. |
| `A-ID` | Tenant/identity binding, track lineage and authorization decisions against synthetic ground truth; no unauthorized cross-binding/disclosure or inferred physical identity from subscriber authentication. |
| `A-AI` | Per-stratum/class precision/recall, unknown rejection, calibration, uncertainty coverage, inference tail latency and output age, numerical validity and approved model/preprocessing compatibility; meet approved quality/timeliness bounds or visibly abstain. |
| `A-CTL` | Policy-check outcomes, action scope/expiry, change rate, stability, rollback and stop precedence; only independently authorized bounded network changes pass, with no autonomous engagement path. |
| `A-GOV` | Data/model provenance and approval, purpose/consumer restrictions, storage/transfer locations, revocation propagation and retention/deletion completion; comply with approved policy and report unavailable enforcement explicitly. |
| `A-HF` | Per-frequency/beam configuration calibration residuals, measurement uncertainty, beam acquisition/recovery time and duty cycle, RF quality/dynamic range, sensing validity and approved emissions/exposure/thermal limits; meet approved bounds or declare unavailable/degraded and inhibit invalid outputs. Applicable RF conformance alone is insufficient to pass ISAC quality requirements. |

Specify units, scoring denominators, matching rules, warm-up periods, measurement uncertainty, repetitions, confidence intervals, missing-data policy, and acceptance confidence in the approved profile. Separate detection, classification, and operator notification latency; an average must not hide a required tail-latency or worst-stratum failure.

For core/AI stress tests, approve maximum load, ramp/burst/hold durations, queue capacities, admission limits, percentile definitions, recovery observation interval and stop limits before execution. Report offered load and all rejected, dropped, expired, timed-out, abstained and missing outputs; do not compute AI quality only on easy completed requests. Measure observation-to-consumer age as well as service processing time. Specify recovery point/time objectives and how accepted jobs and data are reconciled after a failure.

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
| `E7` | Synthetic subscriber/session/job/tenant identifiers, core API traces, policy/admission decisions, discovery/routing state, load counters and distributed trace spans |
| `E8` | Approved evaluation dataset/split hashes, preprocessing/model/runtime versions, inference timestamps and outputs, quality/calibration/abstention scores, drift and resource telemetry |
| `E9` | Model/data approvals and lineage, deployment/rollback history, control-policy decisions, access/revocation/retention/residency evidence and recovery reconciliations |
| `E10` | Exact frequency/waveform/array manifest; beam state and observation-gap logs; chamber/instrument calibration and uncertainty; per-band channel/model/scene provenance; permitted RF/exposure/thermal readings and hardware/simulation status |

Every instance needs a monitored trigger and named stop owner. The safety plan must specify what happens if the test system itself becomes unresponsive.

| Code | Stop trigger and required safe outcome |
|---|---|
| `S1` | Equipment, RF containment, thermal or electrical limit approached, or facility monitor lost: terminate stimulus using the independent lab control and place equipment in its approved safe state. |
| `S2` | Communication service budget crossed or unintended production coupling detected: end injection, preserve evidence and restore the isolated baseline; do not continue on a live network. |
| `S3` | Required truth, clock validity, data integrity, or uncertainty indication lost: pause scoring, mark results invalid/degraded, and stop dependent automated decisions. |
| `S4` | Recovery deadline exceeded, rollback fails, or fault escapes isolation: stop injection, inhibit unsafe outputs, and invoke the approved isolated restoration plan. |
| `S5` | Missing authorization/interlock, uncontrolled mocked action, operator overload, or unavailable stop authority: inhibit response outputs and end the exercise through independent control. |
| `S6` | Live-exercise boundary, permission, aircraft-control, uninvolved-aircraft/person separation, or weather limit breached: terminate via the approved aviation safety plan and coordinate with the authorized operator. |
| `S7` | Tenant/purpose/residency boundary crossed, revoked access persists, or an unapproved model/control path becomes active: isolate the affected test services, inhibit outputs, preserve restricted audit evidence, and require governance/safety review before resuming. |

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

### Core-network and sensing-service stress

TC-061 through TC-084 use isolated core services, emulators and synthetic subscribers/traffic only. Where a named 5GC function is absent, instantiate the declared equivalent contract or record a reviewed exclusion; do not assume that an application-level sensing job is a PDU session. Each case inherits the execution, evidence, approval and stop requirements above.

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-061 | Sensing capability discovery/admission; `C/B/M/R=ALL` | Bounded synthetic jobs requesting supported, unavailable and unsupported sensing capabilities | E3,E4,E7 | A-CORE,A-RAD; admit only authorized supported jobs within resource budgets; return explicit unsupported/overload outcomes | S2,S4,S7 | REQ-CORE,REQ-RAD |
| TC-062 | UE registration and re-registration burst; `C/B/U=ALL` | Isolated UE emulator with synthetic subscribers, including absent/invalid subscriptions | E2,E4,E7 | A-CORE,A-COM,A-ID; bound authentication/registration load; do not authenticate a sensed object from UE attachment | S2,S4,S7 | REQ-CORE,REQ-COM,REQ-ID |
| TC-063 | Session setup/modify/release churn; `C/B/N=ALL` | Synthetic sessions, duplicated requests and delayed completions in isolated core | E2,E4,E7 | A-CORE,A-COM; bound latency/state/resource leakage; reconcile retries without duplicate logical session effects | S2,S4 | REQ-CORE,REQ-COM,REQ-RES |
| TC-064 | Device mobility, idle/paging and serving-node changes; `C/B/U/L=ALL` | UE/RAN emulator transitions with labeled sensing tracks | E1,E2,E7 | A-CORE,A-TRK,A-ID; preserve only valid service continuity; UE mobility must not silently reassign object identity | S2,S3,S4 | REQ-CORE,REQ-SEN,REQ-ID |
| TC-065 | Sensing-data transport/UPF contention where applicable; `C/B/Q=ALL` | Bounded isolated microbursts and sustained test traffic | E1,E2,E4,E7 | A-CORE,A-COM,A-TRK; enforce declared QoS and freshness; measure loss/age across the actual sensing transport | S1,S2,S3 | REQ-CORE,REQ-COM,REQ-SEN |
| TC-066 | Policy conflicts and admission priority; `C/B/M/H=ALL` | Mock competing communication/sensing policy updates | E2,E6,E7,E9 | A-CORE,A-COM,A-CTL; explicit policy precedence and rejection; RAN/core enforcement agree without unapproved priority escalation | S2,S5,S7 | REQ-CORE,REQ-COM,REQ-CTL |
| TC-067 | Tenant/slice isolation and noisy neighbors; `C/B/H=ALL` | Synthetic tenants with independently bounded load and overlapping job identifiers | E2,E4,E7,E9 | A-CORE,A-COM,A-ID; enforce per-tenant resource/data isolation; no cross-tenant result delivery | S2,S4,S7 | REQ-CORE,REQ-COM,REQ-ID |
| TC-068 | Authentication/subscription dependency loss and revocation; `C/B/H=ALL` | Mock AUSF/UDM/UDR unavailability, expiry and test credential revocation | E4,E5,E7 | A-CORE,A-ID,A-GOV; bounded failure and approved existing-session policy; no unauthorized access via stale caches | S4,S7 | REQ-CORE,REQ-ID,REQ-GOV |
| TC-069 | Discovery/routing staleness during scaling; `C/B/L=ALL` | Isolated NRF/service-registry updates and stale endpoint fixtures | E4,E7 | A-CORE,A-RES; avoid retired/unready endpoints, bound rediscovery and preserve explicit failures | S2,S4 | REQ-CORE,REQ-RES |
| TC-070 | Service API/SCP overload and retry amplification; `C/B=ALL` | Bounded API load, timeouts and explicit overload responses in isolated services | E4,E7 | A-CORE,A-COM; honor retry/deadline budgets and backpressure; dependency load stays within approved limits | S1,S2,S4 | REQ-CORE,REQ-COM,REQ-RES |
| TC-071 | Exposure/subscription fan-out and slow consumers; `C/B/H=ALL` | Mock NEF/AF or declared service clients, stalled callbacks and cancellations | E4,E5,E7 | A-CORE,A-DAT,A-ID; quota/authorization enforced; slow consumer does not block others or receive expired data | S3,S4,S7 | REQ-CORE,REQ-DAT,REQ-ID |
| TC-072 | NWDAF analytics load, expiry and unavailable input; `C/B/J=ALL` | Synthetic analytics subscriptions and stale/missing network counters | E4,E7,E8 | A-CORE,A-DAT,A-CTL; expose stale/unavailable analytics; no substitution for physical-object ground truth or unchecked control | S3,S4,S7 | REQ-CORE,REQ-DAT,REQ-CTL |
| TC-073 | Event/observation broker backlog and schema evolution; `C/B/X=ALL` | Versioned fixtures with duplicates, reordering and bounded broker pressure | E4,E5,E7 | A-CORE,A-DAT,A-TRK; validate compatibility, bound age and make loss/replay visible | S3,S4 | REQ-CORE,REQ-DAT,REQ-SEN |
| TC-074 | Sensing-job cancel/retry/expiry race; `C/B/L=ALL` | Test job requests with delayed acknowledgements and cancellation during execution | E4,E6,E7 | A-CORE,A-CTL; one authoritative lifecycle, no orphan resources or output accepted after cancellation/expiry | S4,S5 | REQ-CORE,REQ-RES,REQ-CTL |
| TC-075 | Core/application state-store partition and leader conflict; `C/N=ALL` | Isolated replica partition and stale lease fixture | E4,E7,E9 | A-CORE,A-RES,A-CTL; fence stale writers and reconcile state; unavailable authority is not silently duplicated | S4,S5,S7 | REQ-CORE,REQ-RES,REQ-CTL |
| TC-076 | Regional/core-service failover and restoration; `C/L=ALL` | Isolated service outage with synthetic accepted jobs/sessions | E2,E4,E7,E9 | A-CORE,A-COM,A-RES; meet approved recovery point/time objectives and reconcile accepted/lost work explicitly | S2,S4 | REQ-CORE,REQ-COM,REQ-RES |
| TC-077 | Inter-operator/federated/roaming boundary where supported; `C/H=ALL` | Mock partner core and purpose-limited synthetic observations | E5,E7,E9 | A-CORE,A-ID,A-GOV; enforce authorization, residency and uncertainty provenance across boundary; no implied sensing-data sharing right | S3,S4,S7 | REQ-CORE,REQ-ID,REQ-GOV |
| TC-078 | Core location/time/frame metadata stale or conflicting; `C/G/R=ALL` | Labeled coordinate/time fixtures through declared location/fusion services | E1,E3,E7 | A-RAD,A-DAT,A-TRK; reject invalid transformations and propagate clock/frame uncertainty to consumers | S3 | REQ-RAD,REQ-DAT,REQ-SEN |
| TC-079 | Quota/accounting/charging dependency outage; `C/B/H=ALL` | Isolated counters, quota changes and mock accounting unavailability | E2,E4,E7,E9 | A-CORE,A-COM,A-GOV; explicit approved entitlement/degraded policy; no silent service denial or unbounded sensing admission | S2,S4,S7 | REQ-CORE,REQ-COM,REQ-GOV |
| TC-080 | Core rolling upgrade/autoscale with active jobs; `C/B/L=ALL` | Approved isolated rollout, scale-in and incompatible API fixture | E2,E4,E7,E9 | A-CORE,A-COM,A-RES; drain/reassign work, reject incompatible versions and restore qualified baseline | S2,S4 | REQ-CORE,REQ-COM,REQ-RES |
| TC-081 | Shared DNS/PKI/secret service failure or rotation; `C/H/L=ALL` | Mock resolution failure and test certificate/token expiry/rotation | E4,E5,E7 | A-CORE,A-ID,A-RES; bounded retries and recovery without disabling authentication or accepting revoked identities | S4,S7 | REQ-CORE,REQ-ID,REQ-RES |
| TC-082 | Purpose/permission withdrawal and retention propagation; `C/H=ALL` | Synthetic revocation/deletion fixtures across caches, replicas and derived outputs | E5,E7,E9 | A-DAT,A-GOV; enforce approved legal retention/deletion basis and approved propagation deadline; expose residual copies | S3,S7 | REQ-DAT,REQ-GOV |
| TC-083 | Communication/emergency-service priority under sensing load; `C/B/M/Q=ALL` | Isolated test sessions representing approved priority classes, never real emergency numbers | E2,E4,E7 | A-COM,A-CORE; preserve approved service budgets and visibly reject excess sensing demand | S2,S4 | REQ-COM,REQ-CORE,REQ-SAF |
| TC-084 | Partial core transaction completion and lost acknowledgement; `C/B/L=ALL` | Fail isolated service between resource reservation, state update and reply | E4,E7,E9 | A-CORE,A-RES; idempotent retry or explicit reconciliation; no false success, orphan reservation or duplicate logical action | S4,S5 | REQ-CORE,REQ-RES,REQ-CTL |

### AI domain hosted in the core

TC-085 through TC-112 apply to declared AI capabilities, not automatically to NWDAF. Use authorized datasets, synthetic mutations and isolated model/runtime fixtures; no operational evasion or attack-generation procedure is required. Quality evaluation must include misses, unknowns, rejected/expired work and uncertainty, not just classifier accuracy on completed detections.

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-085 | Feature/preprocessing contract mismatch; `C/J/R/X=ALL` | Golden samples plus wrong unit/order/schema/version fixtures | E1,E5,E8 | A-DAT,A-AI; reject incompatible pipeline versions; no plausible prediction from misinterpreted features | S3,S7 | REQ-DAT,REQ-AI |
| TC-086 | Missing, truncated or non-finite AI input/output; `J/X=ALL` | Bounded invalid tensor/metadata/output fixtures in test adapter | E4,E5,E8 | A-DAT,A-AI; explicit validation failure/abstention, no fabricated class or confidence | S3,S4 | REQ-DAT,REQ-AI,REQ-UNC |
| TC-087 | Inference burst, concurrency and batching; `C/B/J/Q=ALL` | Approved ramp/burst/hold workloads from labeled replay | E1,E4,E7,E8 | A-AI,A-CORE,A-COM; bound tail latency, oldest-item age and resource use; explicit overload/expiry | S1,S2,S3,S4 | REQ-AI,REQ-CORE,REQ-COM |
| TC-088 | Accelerator memory pressure, device reset or worker crash; `C/J=ALL` | Bounded allocation load and emulated runtime faults, no equipment damage | E4,E8 | A-AI,A-RES; visible failure and qualified restart/fallback within approved limits, not invented results | S1,S3,S4 | REQ-AI,REQ-RES |
| TC-089 | Cold start/model cache eviction/registry unavailable; `C/B/J/L=ALL` | Isolated cache reset and mock model-store outage | E4,E8,E9 | A-AI,A-RES; readiness follows verified model loading; report unavailable during warm-up | S3,S4,S7 | REQ-AI,REQ-RES |
| TC-090 | Late inference, cancellation and result expiry; `C/B/J=ALL` | Delayed replay jobs and cancelled requests | E1,E7,E8 | A-AI,A-TRK,A-CORE; discard or explicitly label late outputs; never revive cancelled/stale tracks | S3,S4 | REQ-AI,REQ-SEN,REQ-CORE |
| TC-091 | Out-of-distribution scene/device conditions; `J/R/V=ALL` | Independently held-out approved datasets and qualified simulation | E1,E8 | A-AI,A-UNC; characterize quality/coverage by stratum and flag unsupported inputs; no universal OOD-detection guarantee | S3 | REQ-AI,REQ-UNC |
| TC-092 | Confidence calibration and abstention boundaries; `J/V/Q=ALL` | Versioned evaluation sets across ambiguity and load strata | E1,E8 | A-AI,A-UNC; meet approved calibration/uncertainty bounds and abstention policy including timely-output coverage | S3 | REQ-AI,REQ-UNC |
| TC-093 | Unknown object classes and unsupported identity claims; `J/P/X=ALL` | Labeled unseen/ambiguous objects and missing cooperative identity | E1,E6,E8 | A-AI,A-ID,A-UNC; retain unknown class/identity and never infer hostile intent from score or identity absence | S3,S5 | REQ-AI,REQ-ID,REQ-UNC |
| TC-094 | Data/concept drift and delayed ground-truth labels; `J/R/V/L=ALL` | Controlled changes in dataset composition and label arrival | E1,E8,E9 | A-AI,A-RES; detect approved measurable drift signals, qualify monitoring limits and gate continued use/revalidation | S3,S4 | REQ-AI,REQ-RES |
| TC-095 | Training/serving skew and evaluation leakage; `J/R/L=ALL` | Independent preprocessing comparison and held-out site/time/object split audit | E1,E5,E8,E9 | A-AI,A-GOV; no disallowed split overlap; comparable features and independently reproduced quality before approval | S3,S7 | REQ-AI,REQ-GOV |
| TC-096 | Training-data provenance, purpose and residency; `C/J/H=ALL` | Synthetic authorized/disallowed dataset lineage, withdrawal and transfer fixtures | E5,E8,E9 | A-GOV,A-AI; reject unapproved use/transfer; trace affected derived models and apply approved requalification/retirement policy, not assumed instant unlearning | S7 | REQ-GOV,REQ-AI |
| TC-097 | Label/data integrity degradation; `J/X=ALL` | Declared bounded synthetic label inconsistencies and corrupted records in isolated evaluation | E1,E5,E8,E9 | A-DAT,A-AI; surface integrity/quality failure and block unqualified model promotion | S3,S7 | REQ-DAT,REQ-AI,REQ-GOV |
| TC-098 | Missing/misaligned modalities at AI fusion; `J/X=ALL` | Labeled sensor dropout, different sample rates and alignment errors | E1,E3,E8 | A-AI,A-TRK,A-UNC; qualified modality-specific degradation or abstention, with no silent imputation as truth | S3,S4 | REQ-AI,REQ-SEN,REQ-UNC |
| TC-099 | Correlated/duplicated evidence and ensemble disagreement; `J/G/X=ALL` | Replay shared-source duplicates and conflicting approved model outputs | E1,E5,E8 | A-AI,A-UNC; retain lineage and avoid treating correlated observations as independent certainty | S3 | REQ-AI,REQ-DAT,REQ-UNC |
| TC-100 | Precision/runtime/hardware portability; `C/J/R=ALL` | Golden corpus on each approved CPU/accelerator/quantized runtime | E1,E8,E9 | A-AI; meet numerical validity and per-stratum quality bounds for each qualified artifact/runtime combination | S1,S3 | REQ-AI |
| TC-101 | Model artifact approval/integrity and dependency mismatch; `J/H=ALL` | Test artifacts with invalid digest, missing approval or incompatible dependency manifest | E5,E8,E9 | A-AI,A-GOV; refuse activation; retain qualified version only if permitted and visibly identified | S3,S7 | REQ-AI,REQ-GOV |
| TC-102 | AI canary/mixed-version rollout and rollback; `C/J/L=ALL` | Isolated approved rollout and deliberately failing evaluation fixture | E1,E4,E8,E9 | A-AI,A-RES,A-ID; bound quality regression, preserve versioned track lineage and restore qualified model consistently | S3,S4,S7 | REQ-AI,REQ-RES,REQ-ID |
| TC-103 | Training versus inference/core resource contention; `C/B/J/Q=ALL` | Quota-limited training/evaluation jobs concurrent with synthetic service load | E2,E4,E7,E8 | A-AI,A-CORE,A-COM; enforce reservations and approved admission; training cannot starve priority communication/inference | S1,S2,S4 | REQ-AI,REQ-CORE,REQ-COM |
| TC-104 | Retraining approval, reproducibility and regression gate; `J/L/H=ALL` | Versioned offline training pipeline with failed/missing approval fixtures | E1,E8,E9 | A-AI,A-GOV; reproduce approved evaluation within specified tolerance; no automatic production promotion after drift | S3,S7 | REQ-AI,REQ-GOV |
| TC-105 | Distributed/federated training where implemented; `C/J/H=ALL` | Mock participant dropout, version mismatch and invalid update provenance | E5,E8,E9 | A-AI,A-GOV,A-RES; validate participant/update eligibility, bounded convergence criterion and privacy/residency policy | S3,S4,S7 | REQ-AI,REQ-GOV,REQ-RES |
| TC-106 | AI/network-analytics feedback instability; bounded-control `J/M=ALL` | SIL policy loop with delayed/conflicting recommendations | E2,E4,E7,E8,E9 | A-CTL,A-COM,A-AI; meet approved stability/change-rate bounds; independent policy rejects unsafe oscillation | S2,S4,S5 | REQ-CTL,REQ-COM,REQ-AI |
| TC-107 | Advisory-only AI and revoked write authority; `J/H=ALL` | Mock out-of-scope/expired network-control requests | E5,E6,E8,E9 | A-CTL,A-ID,A-SAF; deny unauthorized writes independently of AI; no real response/engagement interface | S5,S7 | REQ-CTL,REQ-ID,REQ-SAF |
| TC-108 | Decision provenance and operator interpretation; `J/Q=ALL` | Recorded predictions with missing/conflicting explanation metadata | E1,E6,E8,E9 | A-AI,A-HUM,A-DAT; show model/version, age, uncertainty and evidence limits; no fabricated rationale | S3,S5 | REQ-AI,REQ-HUM,REQ-DAT |
| TC-109 | Track/object/device identity correlation; `J/P/X/H=ALL` | Synthetic ID rotation, overlapping tracks, duplicate claims and UE changes | E1,E5,E7,E8 | A-ID,A-TRK,A-UNC; preserve uncertain associations and separate subscriber, claimed identity and physical track | S3,S7 | REQ-ID,REQ-SEN,REQ-UNC |
| TC-110 | Optional generative assistant handling untrusted reports; applicable `J/H` | Benign test reports containing conflicting instructions and unsupported assertions | E5,E6,E8,E9 | A-DAT,A-HUM,A-CTL; treat reports as data, enforce independent permissions and never invent identification or response authority | S3,S5,S7 | REQ-DAT,REQ-HUM,REQ-CTL |
| TC-111 | AI telemetry/drift monitor/evaluation service unavailable; `C/J/L=ALL` | Disable isolated monitoring endpoint or hold evaluation results | E4,E8,E9 | A-AI,A-RES; monitoring gap visible and approved continued-use/stop policy enforced; no assumed healthy quality | S3,S4 | REQ-AI,REQ-RES |
| TC-112 | AI-domain shutdown, independent stop and qualified fallback; `C/J/L=ALL` | Isolated AI outage/stop with only approved fallback paths enabled | E1,E2,E4,E6,E8 | A-SAF,A-RES,A-COM,A-UNC; stop works without AI, preserve communication and report unavailable/degraded identification | S2,S4,S5 | REQ-SAF,REQ-RES,REQ-COM,REQ-UNC |

### Device-RAN-core-AI compound failures and end-to-end assurance

TC-113 through TC-128 test responsibility boundaries that component benchmarks miss. Apply these to supported modes/radios/devices and declared core/AI placements. Combined faults remain isolated, bounded and independently stoppable.

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-113 | Observation-to-operator latency/freshness under concurrent load; `C/B/J/M/R=ALL` | Timestamped scene replay with device, RAN, transport, core, AI and mock consumer spans | E1,E2,E6,E7,E8 | A-TRK,A-AI,A-HUM,A-COM; meet end-to-end and per-hop budgets including queues/retries; a timely stale result fails | S2,S3,S5 | REQ-SEN,REQ-AI,REQ-HUM,REQ-COM |
| TC-114 | AI-serving burst plus UE registration/session surge; `C/B/J/Q=ALL` | Concurrent bounded synthetic workloads on declared shared platform | E2,E4,E7,E8 | A-CORE,A-AI,A-COM; preserve approved isolation/priority and report rejected/expired work by class | S1,S2,S4 | REQ-CORE,REQ-AI,REQ-COM |
| TC-115 | Core disconnection plus continued local observations; `C/J/U=ALL` | Network emulator partition with timestamped replay at RAN/device | E1,E4,E7,E8 | A-TRK,A-RES,A-UNC; only qualified local fallback runs; unavailable core AI is not reported as active | S3,S4 | REQ-SEN,REQ-RES,REQ-UNC |
| TC-116 | Reconnection backlog plus changed model/policy; `C/B/J/L=ALL` | Release buffered replay after isolated update and outage | E1,E4,E7,E8,E9 | A-DAT,A-AI,A-CTL; validate age/version/authorization before replay; no retrospective live-looking decision or old command | S3,S4,S7 | REQ-DAT,REQ-AI,REQ-CTL |
| TC-117 | Shared core/AI cluster, storage or region loss; `C/N/J=ALL` | Common-cause service-failure emulator with synthetic accepted work | E2,E4,E7,E8,E9 | A-CORE,A-RES,A-COM; demonstrate actual failure-domain independence or explicitly report correlated loss | S2,S4 | REQ-CORE,REQ-RES,REQ-COM |
| TC-118 | Uncertain AI result plus failed operator delivery; `C/J/X=ALL` | Ambiguous replay and unavailable mock notification path | E1,E4,E6,E8 | A-UNC,A-HUM,A-SAF; retain uncertainty and visible delivery failure; no automation that bypasses human authority | S3,S5 | REQ-UNC,REQ-HUM,REQ-SAF |
| TC-119 | Revocation during active inference/federation; `C/J/H=ALL` | Synthetic consent/authorization withdrawal with in-flight jobs and caches | E5,E7,E8,E9 | A-ID,A-GOV,A-CORE; enforce approved propagation deadline at result delivery and onward sharing, not only ingestion | S7 | REQ-ID,REQ-GOV,REQ-CORE |
| TC-120 | Device/RAN timing/calibration loss plus AI confidence; `C/J/R/G=ALL` | Isolated health/clock faults with held-out replay | E1,E3,E7,E8 | A-RAD,A-AI,A-UNC; propagate invalidity end-to-end even when classifier score remains high | S3 | REQ-RAD,REQ-AI,REQ-UNC |
| TC-121 | Tenant pressure plus core/AI scale-in/failover; `C/B/J/H=ALL` | Synthetic multi-tenant load with controlled isolated rescheduling | E2,E4,E7,E8,E9 | A-CORE,A-ID,A-AI; no cache/result/authority cross-binding and no hidden resource-budget breach | S1,S2,S4,S7 | REQ-CORE,REQ-ID,REQ-AI |
| TC-122 | Model update plus radio/mode/core API transition; `C/J/M/R/L=ALL` | Supported directed transitions and incompatible version fixtures in SIL/HIL | E1,E3,E7,E8,E9 | A-AI,A-RAD,A-CORE,A-RES; block incompatible combinations and bound qualified rollback | S1,S3,S4 | REQ-AI,REQ-RAD,REQ-CORE,REQ-RES |
| TC-123 | Stop/revocation during AI-driven network change; `C/J/L=ALL` | Mock change pending while independent stop or permission withdrawal arrives | E2,E6,E7,E9 | A-CTL,A-SAF,A-RES; stop/revocation precedence persists across retries, failover and restart | S2,S5,S7 | REQ-CTL,REQ-SAF,REQ-RES |
| TC-124 | Recovery from mismatched core/model/data backups; `C/J/L=ALL` | Isolated restore from versioned synthetic snapshots with declared recovery objectives | E4,E5,E7,E8,E9 | A-CORE,A-AI,A-GOV,A-RES; validate consistency, revoked rights and accepted-work disposition before readiness | S3,S4,S7 | REQ-CORE,REQ-AI,REQ-GOV,REQ-RES |
| TC-125 | Multi-site object handoff versus UE/session mobility; `C/G/J/U=ALL` | Labeled cross-site replay plus independent synthetic UE mobility | E1,E7,E8 | A-ID,A-TRK,A-AI; correlate only supported evidence; no duplicate authoritative object or subscriber-to-object identity shortcut | S3,S7 | REQ-ID,REQ-SEN,REQ-AI |
| TC-126 | Core/AI privacy controls under evidence-store failure; `C/J/H=ALL` | Synthetic incident traces with unavailable audit/retention endpoint | E4,E5,E8,E9 | A-DAT,A-GOV,A-RES; apply approved deny/degrade rules, restrict emergency evidence and expose enforcement gaps | S3,S4,S7 | REQ-DAT,REQ-GOV,REQ-RES |
| TC-127 | Long-duration core/AI churn and repeated degraded recovery; `C/B/J/L=ALL` | Approved-duration isolated jobs, sessions, updates and fault/recovery cycles | E2,E4,E7,E8,E9 | A-CORE,A-AI,A-RES,A-COM; bound leaks, queue growth, identity drift and quality/latency regressions over time | S1,S2,S3,S4 | REQ-CORE,REQ-AI,REQ-RES,REQ-COM |
| TC-128 | Pre-approved multi-domain acceptance and operator handoff rehearsal; all applicable axes | Replay a versioned scenario pack with independent domain owners and mock responders | E1,E2,E3,E4,E5,E6,E7,E8,E9 | A-SEN,A-CORE,A-AI,A-COM,A-CTL,A-HUM,A-SAF,A-GOV plus every profile required by constituent instances; all cross-domain contracts pass; unresolved gaps explicit | S1,S2,S3,S4,S5,S7 | REQ-SEN,REQ-CORE,REQ-AI,REQ-COM,REQ-CTL,REQ-HUM,REQ-SAF,REQ-GOV |

### FR2/mmWave and experimental sub-THz qualification and stress

TC-129 through TC-152 apply to each declared supported `K` configuration and its applicable `D/W/G/R/V/Q/C/J` combinations. All RF stimuli remain simulated, conducted, or inside qualified shielded facilities. The cases provide no field interference, targeting, engagement or attack procedures. `A-HF` adds frequency-specific limits; original sensing, communication, AI and safety acceptance is still required.

| ID | Scenario and axis coverage | Safe stimulus | Observable evidence | Acceptance profile and case-specific outcome | Stop | Requirement |
|---|---|---|---|---|---|---|
| TC-129 | Blockage and intermittent observability; `K/G/V=ALL` | Qualified channel replay/emulator with labeled blocked intervals | E1,E3,E10 | A-HF,A-SEN,A-TRK,A-UNC; measure per-band misses/gaps and declare unobservable rather than absent-object state | S1,S3 | REQ-HF,REQ-SEN,REQ-UNC |
| TC-130 | Beam acquisition, tracking, misalignment and recovery; `K/W/R/Q=ALL` | SIL or shielded OTA reference scene with approved beam-state/orientation changes | E1,E2,E4,E10 | A-HF,A-TRK,A-COM; bound acquisition/recovery and observation gaps without hiding communication resource cost | S1,S2,S3 | REQ-HF,REQ-SEN,REQ-COM |
| TC-131 | Wideband beam squint and frequency-dependent array response; `K/D/W=ALL` | Qualified wideband array model or shielded calibrated measurement | E1,E3,E10 | A-HF,A-SEN; score across approved bandwidth/steering partitions; report unsupported angular/frequency regions | S1,S3 | REQ-HF,REQ-RAD,REQ-SEN |
| TC-132 | Near/far-field model validity and focusing assumptions; `K/G/R=ALL` | Qualified spherical/planar-wave reference fixtures in simulator or suitable chamber | E1,E3,E10 | A-HF,A-SEN,A-UNC; use aperture/frequency-valid models and uncertainty; no far-field claim outside qualified domain | S1,S3 | REQ-HF,REQ-RAD,REQ-UNC |
| TC-133 | Frequency-dependent atmospheric/weather attenuation; `K/V=ALL` | Validated gas, precipitation and cloud/fog models or authorized reference recordings | E1,E3,E10 | A-HF,A-SEN,A-COM; score approved strata separately, enforce model validity and expose degraded coverage | S1,S2,S3 | REQ-HF,REQ-SEN,REQ-COM |
| TC-134 | Material/roughness/polarization and target-scattering variability; `K/G/V=ALL` | Authorized measured or qualified synthetic scattering/multipath scenes | E1,E3,E10 | A-HF,A-SEN,A-UNC; no fixed cross-band reflectivity/identity assumption; quantify model uncertainty | S1,S3 | REQ-HF,REQ-SEN,REQ-UNC |
| TC-135 | Radome/enclosure loss and mounting variation; `K/R/L=ALL` | Qualified enclosure-loss fixtures or model; no damage or unsafe contamination | E1,E3,E10 | A-HF,A-RAD,A-RES; detect configuration/calibration invalidity and require requalification where necessary | S1,S3,S4 | REQ-HF,REQ-RAD,REQ-RES |
| TC-136 | Phase noise, frequency offset and LO/multiplier impairments; `K/D/G=ALL` | Approved impairment emulator or shielded test equipment | E1,E3,E10 | A-HF,A-RAD,A-SEN; quantify coherence/sensing degradation; invalidate estimates beyond qualified limits | S1,S3 | REQ-HF,REQ-RAD,REQ-SEN |
| TC-137 | PA/receiver nonlinearity, dynamic range and self-leakage; `K/R/D=ALL` | Bounded conducted/shielded impairment fixtures, never damaging drive levels | E1,E2,E3,E10 | A-HF,A-SEN,A-COM; expose compression/saturation and comply with approved RF limits | S1,S2,S3 | REQ-HF,REQ-RAD,REQ-SEN,REQ-COM |
| TC-138 | Converter precision, clipping and usable bandwidth; `K/D/J=ALL` | Golden samples plus approved ADC/DAC/IQ/filter impairment models | E1,E3,E8,E10 | A-HF,A-SEN,A-AI; qualify each precision/bandwidth pipeline and preserve uncertainty through feature extraction | S1,S3 | REQ-HF,REQ-SEN,REQ-AI |
| TC-139 | Array element/panel fault and calibration drift; `K/R/W=ALL` | Software/HIL element-health or calibration metadata fault | E1,E3,E4,E10 | A-HF,A-RAD,A-RES; declare reduced aperture/coverage and revalidate calibration before healthy state | S1,S3,S4 | REQ-HF,REQ-RAD,REQ-RES |
| TC-140 | Thermal/power derating with beam/sensing workload; `K/R/Q=ALL` | Simulated health inputs and bounded isolated workload; no deliberate overheating | E2,E3,E4,E10 | A-HF,A-COM,A-RES; approved derating must propagate changed resource/coverage capability to RAN/core consumers | S1,S2,S4 | REQ-HF,REQ-COM,REQ-RES |
| TC-141 | Cross-radio timing/phase coherence and sample-clock mismatch; `K/G/N=ALL` | Isolated clock emulator with per-node uncertainty records | E1,E3,E7,E10 | A-HF,A-RAD,A-TRK; only claim coherent fusion when qualified; otherwise use qualified noncoherent mode or invalidate | S3,S4 | REQ-HF,REQ-RAD,REQ-SEN |
| TC-142 | Waveform ambiguity and observation-sampling gaps; `K/D/W=ALL` | Labeled synthetic scenes spanning approved resolution/ambiguity partitions | E1,E2,E3,E10 | A-HF,A-SEN,A-TRK; measure ambiguity and uncertainty separately from communication quality; no bandwidth-only accuracy guarantee | S1,S2,S3 | REQ-HF,REQ-SEN,REQ-UNC |
| TC-143 | OTA instrumentation/chamber/converter validity; `K/R=ALL` | Calibrated reference fixtures and test instrument fault/status flags | E3,E4,E10 | A-HF,A-RAD; valid calibration/quiet-zone/transform and uncertainty required; unqualified setup blocks hardware acceptance | S1,S3 | REQ-HF,REQ-RAD |
| TC-144 | UE panel/orientation, power-state and mobility dependencies; `K/R/U/L=ALL` | UE/panel emulator or shielded OTA fixture with synthetic sessions | E1,E2,E3,E10 | A-HF,A-COM,A-TRK; characterize device versus network-only sensing and beam recovery independently | S1,S2,S3 | REQ-HF,REQ-COM,REQ-SEN |
| TC-145 | Cross-band fallback, carrier/panel transition and hysteresis; mixed `K/M/L` | Approved isolated transition graph and unavailable-band fixtures | E1,E2,E4,E7,E10 | A-HF,A-COM,A-TRK,A-RES; no assumed sensing continuity on communication fallback; bound oscillation and stale-track carryover | S1,S2,S3,S4 | REQ-HF,REQ-COM,REQ-SEN,REQ-RES |
| TC-146 | AI cross-band domain shift and hardware signatures; `K/J/R/V=ALL` | Independent per-band held-out corpora and wrong-band model fixtures | E1,E8,E9,E10 | A-HF,A-AI,A-UNC; reject unqualified model/preprocessing transfer and meet per-band quality/abstention criteria | S3,S7 | REQ-HF,REQ-AI,REQ-UNC |
| TC-147 | Band-dependent data/beam-event load on core/AI; `K/B/C/J/Q=ALL` | Bounded synthetic sample/feature streams and beam-recovery event bursts | E2,E4,E7,E8,E10 | A-HF,A-CORE,A-AI,A-COM; separate actual event/data rates from RF bandwidth and preserve approved end-to-end budgets | S1,S2,S3,S4 | REQ-HF,REQ-CORE,REQ-AI,REQ-COM |
| TC-148 | Mixed-band fusion, registration and identity lineage; mixed `K/G/X/J` | Time/frame-labeled multi-band replay with dropout/duplicate tracks | E1,E3,E5,E8,E10 | A-HF,A-ID,A-TRK,A-UNC; prevent cross-band double-counting or identity shortcuts and retain correlated uncertainty | S3,S7 | REQ-HF,REQ-ID,REQ-SEN,REQ-UNC |
| TC-149 | Spectrum permission, exposure and containment interlocks; `K/R/H=ALL` | Mock permission/limit withdrawal and instrument status in approved isolated facility | E3,E6,E9,E10 | A-HF,A-SAF,A-GOV; independent RF inhibit on invalid permission/monitor state; never exceed limits to test protection | S1,S5,S7 | REQ-HF,REQ-SAF,REQ-GOV |
| TC-150 | Band-specific propagation loss plus beam fault plus core/AI contention; applicable `K/V/F/C/J/Q` | Qualified combined emulator faults and bounded isolated workload | E1,E2,E3,E4,E7,E8,E10 | A-HF,A-SEN,A-COM,A-AI,A-RES; uncertainty and degraded state propagate despite shared load; no falsely healthy fused result | S1,S2,S3,S4 | REQ-HF,REQ-SEN,REQ-COM,REQ-AI,REQ-RES |
| TC-151 | Restart/restore after band or front-end change; `K/R/J/L=ALL` | Isolated restore with mismatched calibration/beam/model artifacts | E1,E3,E4,E8,E9,E10 | A-HF,A-RAD,A-AI,A-RES; validate matching radio/calibration/model manifest before readiness; rollback if incompatible | S1,S3,S4,S7 | REQ-HF,REQ-RAD,REQ-AI,REQ-RES |
| TC-152 | Per-profile end-to-end qualification and evidence closure; `K=ALL` | Replay each approved band-specific acceptance pack with independent reviewers | E1,E2,E3,E4,E5,E6,E7,E8,E9,E10 | A-HF plus all constituent profiles; every original-case/profile entry has reviewed disposition and traceable evidence; no simulated result labeled hardware pass | S1,S2,S3,S4,S5,S7 | REQ-HF,REQ-SEN,REQ-COM,REQ-CORE,REQ-AI,REQ-SAF |

## Coverage accounting and release gate

Maintain a versioned coverage ledger using the instance fields above. A spreadsheet, test-management system, or structured data export is acceptable; this README is not an execution database.

1. Freeze the supported configuration inventory, domain ownership/dependency map and local requirements, including core/AI placement and authority. Map source clauses only where actually applicable; explicitly distinguish normative requirements, recommendations, and local design choices.
2. Expand each scenario over applicable axis values and all supported directed lifecycle/mode/band transitions. Apply the `K` overlay to every case, including original cases without `K` in their row text. Record constraints for impossible or prohibited combinations and obtain independent review.
3. Execute reference/boundary/single-fault cases, then a constrained pairwise interaction suite and risk-selected higher-order/common-cause cases. Do not describe the pairwise suite as exhaustive.
4. For a literal exhaustive bounded-combination claim, enumerate and execute **every feasible combination in the declared finite domain**, including declared fault sequences and bounded timing/value partitions. State unmodeled continuous values and omitted dimensions. If that is infeasible, report partial/risk-based coverage instead.
5. Link every requirement and expected observable outcome to instances, acceptance-profile versions, results, evidence, and residual-risk disposition. Independently validate the ground-truth and scoring method.
6. Require review of failures, aborts, exclusions, missing evidence, uncertainty, and restoration results. A waiver does not convert an unexecuted or failed test into a pass.
7. Rebaseline and rerun affected cases after changes to firmware, models, training/evaluation data, preprocessing, radio configuration, core policy/API, deployment placement, dependencies, approved limits, or operating environment.

For the core/AI extension, cover `C/B/J/H` interactions with the radio/device axes and with each other. Include shared-dependency and authority-boundary failures, not only independent node outages. Establish a no-fault baseline, then approve bounded ramps/bursts/holds, single failures, selected compound failures and post-load recovery for each applicable instance. Never infer measured capacity from a catalogue or from a single unloaded inference benchmark.

| Responsibility coverage obligation | Scenario linkage |
|---|---|
| Access/session/mobility and communication priority | TC-062 through TC-068, TC-083, TC-114, TC-125; retain TC-013 through TC-017 and TC-024 |
| Sensing service lifecycle/exposure/state and recovery | TC-061, TC-069 through TC-084, TC-115 through TC-117, TC-124 |
| AI data/model lifecycle and inference validity | TC-085 through TC-105, TC-111, TC-120, TC-122 |
| Independent authority, uncertainty and operator notification | TC-106 through TC-112, TC-118, TC-123, TC-128; retain TC-041 through TC-050 |
| Cross-domain identity, governance and common-cause resilience | TC-109, TC-113 through TC-128; retain TC-051 through TC-060 |

These are coverage links, not execution evidence. Review individual cases and all applicable contracts even when a family has representative coverage.

For FR2/sub-THz, maintain an entry for every original-case/exact-frequency-configuration pair and every applicable added-case/configuration pair. State feasible counts after reviewed constraints, not `128 x 3` as a presumed hardware test count. Partition by approved carriers, bandwidths, beam/aperture states, propagation conditions, impairments, modes and core/AI contracts. Record the base case, all overlay conditions, execution/evidence-reuse disposition, original run identifier, reviewers, missing evidence and residual risk. Reused logic evidence does not establish independent RF/OTA qualification.

Report simulated, conducted, shielded OTA and authorized benign live evidence separately. A configuration with only simulated support cannot be described as hardware-qualified, and one passed FR2-1 configuration cannot close FR2-2 or sub-THz coverage. If no approved hardware/permission exists, show the blocked/excluded hardware and live instances rather than silently dropping the profile.

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
| Cross-domain contract coverage | Contracts with reviewed end-to-end load/failure/recovery evidence / all applicable declared device-RAN-core-AI-consumer contracts |
| AI qualification coverage | Qualified model/preprocessing/runtime/data-stratum combinations / all applicable approved combinations; report abstention, expiry and unsupported strata separately |
| Frequency-overlay disposition completeness | Reviewed case/exact-frequency-configuration entries / all required entries, including reviewed exclusions and separately counted evidence reuse |
| Per-frequency execution and qualification | Actual passed/failed/blocked/aborted/not-run applicable instances per exact configuration, with simulation/conducted/OTA/live evidence separated; no reuse inflated into extra executions |

**Current coverage:** not assessed. All 152 cases, TC-001 through TC-152, are templates awaiting configuration-specific instantiation, approval and execution. The original 128 cases require frequency-overlay review, and 24 additional cases address high-frequency qualification. There are no measured pass rates, validated core capacities, qualified AI models, qualified FR2/sub-THz configurations or validated protection claims in this repository. Catalogue additions close design-scope gaps, not evidence or deployment gaps.

Suggested claim format:

> Catalogue revision [commit] covers the declared [system/configuration/requirements baseline]. Of [N] applicable enumerated instances, [P] passed, [F] failed, [B] were blocked, [A] aborted and [U] were not run. Interaction coverage is [strength and feasible combinations]. Reviewed exclusions and residual risks are [references]. Exhaustiveness applies only to [explicit finite domain]; no universal attack coverage or guaranteed infrastructure protection is claimed.

## References and standards applicability

Source-to-case mappings and exact edition/clauses must be recorded in instance records. A research framework or study is not evidence that a commercial gNodeB implements interoperable ISAC. Verify the applicable 3GPP release, product capability, regulatory permissions and certification separately.

- **SRC-RES:** NIST SP 800-160 Vol. 2 Rev. 1, *Developing Cyber-Resilient Systems: A Systems Security Engineering Approach*: https://doi.org/10.6028/NIST.SP.800-160v2r1. Resilience engineering guidance for REQ-RES, REQ-DAT and recovery/compound-fault cases; not an ISAC performance specification.
- **SRC-RISK:** NIST SP 800-30 Rev. 1, *Guide for Conducting Risk Assessments*: https://doi.org/10.6028/NIST.SP.800-30r1. Risk-assessment guidance supporting applicability, compound-failure selection, exclusions and residual-risk review across all cases.
- **SRC-IMT:** ITU-R Recommendation M.2160, *Framework and overall objectives of the future development of IMT for 2030 and beyond*: https://www.itu.int/rec/R-REC-M.2160. Framework context for integrated sensing and communication; not proof of implemented gNodeB features, radio conformance, or counter-drone performance.
- **SRC-3GPP:** 3GPP TR 22.837, *Study on Integrated Sensing and Communication*: https://www.3gpp.org/ftp/Specs/archive/22_series/22.837/. Study context for use cases and requirements investigation. A Technical Report is not a normative Technical Specification and does not establish commercial implementation or interoperability.
- **SRC-ETSI:** ETSI ISG ISAC deliverables portal: https://www.etsi.org/committee/isac. Consult the current published use-case, deployment, architecture and channel-modeling reports when qualifying the inventory. Record the exact document, edition and applicable clauses before using it as instance-level evidence; a Group Report is not a product certification.
- **SRC-CORE:** 3GPP TS 23.501, *System architecture for the 5G System (5GS)*: https://www.etsi.org/deliver/etsi_ts/123500_123599/123501/; TS 23.502, *Procedures for the 5G System (5GS)*: https://www.etsi.org/deliver/etsi_ts/123500_123599/123502/; TS 23.503, *Policy and charging control framework for the 5G System (5GS)*: https://www.etsi.org/deliver/etsi_ts/123500_123599/123503/. Normative 5GS specifications for applicable architecture/procedures/policy, not finalized 6G architecture or automatic ISAC capability.
- **SRC-ANALYTICS:** 3GPP TS 23.288, *Architecture enhancements for 5G System (5GS) to support network data analytics services*: https://www.etsi.org/deliver/etsi_ts/123200_123299/123288/. Normative analytics architecture in its applicable edition; NWDAF presence does not establish object-identification or response authority.
- **SRC-SEC:** 3GPP TS 33.501, *Security architecture and procedures for 5G System*: https://www.etsi.org/deliver/etsi_ts/133500_133599/133501/. Normative security reference where applicable to the implemented 5GS interfaces; supplementary sensing/AI APIs need their own declared controls.
- **SRC-ISAC-REQ:** 3GPP TS 22.137, *Integrated Sensing and Communication*: https://www.etsi.org/deliver/etsi_ts/122100_122199/122137/. Requirements-level source candidate; verify the selected published edition and scope before clause mapping. Stage-1 requirements do not alone define a deployable 6G core, AI hosting architecture, or conformance test suite.
- **SRC-AI:** NIST AI 100-1, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*: https://doi.org/10.6028/NIST.AI.100-1. Voluntary AI risk-management framework supporting governance, measurement, monitoring and lifecycle review; not a telecom performance standard or model certification.
- **SRC-NR-RF:** 3GPP TS 38.104, *NR; Base Station (BS) radio transmission and reception*: https://www.etsi.org/deliver/etsi_ts/138100_138199/138104/; TS 38.101-2, *NR; User Equipment (UE) radio transmission and reception; Part 2: Range 2 Standalone*: https://www.etsi.org/deliver/etsi_ts/138100_138199/13810102/. Normative NR RF references in the applicable edition for frequency ranges, operating bands and supported configurations; no automatic ISAC or sub-THz conformance.
- **SRC-NR-OTA:** 3GPP TS 38.141-2, *NR; Base Station (BS) conformance testing; Part 2: Radiated conformance testing*: https://www.etsi.org/deliver/etsi_ts/138100_138199/13814102/; TS 38.521-2, *NR; User Equipment (UE) conformance specification; Radio transmission and reception; Part 2: Range 2 standalone*: https://www.etsi.org/deliver/etsi_ts/138500_138599/13852102/. Applicable radio conformance methods, not a complete sensing/AI qualification suite; use separate approved methods for experimental hardware outside their scope.
- **SRC-PROP:** ITU-R P.676, atmospheric gas attenuation: https://www.itu.int/rec/R-REC-P.676/en; P.838, specific attenuation model for rain: https://www.itu.int/rec/R-REC-P.838/en; P.840, clouds/fog attenuation: https://www.itu.int/rec/R-REC-P.840/en. Propagation-model references: verify edition, frequency/environment validity and uncertainty. These models alone do not characterize target scattering, all multipath, hardware performance or end-to-end protection.

**Source-verification status:** the original research pass supplied candidate standards references, but independent retrieval of the ITU/3GPP/ETSI sources was unavailable in that pass. The core/AI and frequency extensions add search-located primary-source pointers, not a clause-level conformance review. Current editions, release applicability and clause-level mappings remain verification prerequisites, not completed checks. No unverified release/date, normative compliance, or regulatory-authority claim is used as an acceptance criterion here.

Local traceability: TC-001 through TC-026 require REQ-SEN/REQ-RAD capability and performance requirements supplied by the actual system owner; this catalogue does not invent normative radio thresholds. TC-027 through TC-040 and TC-051 through TC-060 use SRC-RES/SRC-RISK as engineering guidance. TC-041 through TC-050 additionally require jurisdiction-specific aviation, spectrum, privacy and site permissions; no general reference substitutes for those approvals.

SRC-IMT/SRC-3GPP/SRC-ETSI provide background for the mode/radio inventory and TC-001 through TC-026; they do not supply automatic pass/fail thresholds. Any normative claim must instead identify a verified applicable specification and product requirement. Aviation authorization, spectrum authorization, privacy compliance, and authority to take any response action are separate determinations.

Core/AI source-family mapping:

| Cases / requirements | Source families and limits |
|---|---|
| TC-061 through TC-084; REQ-CORE, REQ-COM, REQ-ID, REQ-CTL | SRC-CORE/SRC-SEC for applicable implemented 5GS contracts; SRC-ISAC-REQ for applicable sensing-service requirements only. Sensing-job and custom AI interfaces remain local contracts unless an applicable specification is verified. |
| TC-072, TC-106, TC-111; analytics dependencies | SRC-ANALYTICS plus the actual consumer/AI/control contracts; no implied standard object classifier or closed-loop permission. |
| TC-085 through TC-112; REQ-AI, REQ-UNC, REQ-GOV | SRC-AI/SRC-RISK/SRC-RES as lifecycle and resilience guidance, plus locally approved task-specific quality, identity and governance requirements. |
| TC-113 through TC-128; cross-domain obligations | Applicable families above plus SRC-RES/SRC-RISK and reviewed end-to-end contracts; per-function conformity cannot substitute for end-to-end evidence. |
| TC-001 through TC-128 frequency overlay; TC-129 through TC-152; REQ-HF | SRC-NR-RF/SRC-NR-OTA for in-scope implemented NR configurations; SRC-PROP only within verified model validity. Experimental sub-THz needs independently approved hardware/channel/OTA requirements. Retain all original case source mappings and core/AI guidance. |

This mapping is deliberately at source-family level. Each executable instance must identify actual applicable clauses or explicitly mark its requirement as a local engineering requirement. No reference establishes universal thresholds, exhaustive coverage, hostile intent, or authority to engage an aircraft.
