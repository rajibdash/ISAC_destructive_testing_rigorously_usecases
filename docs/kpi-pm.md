# ISAC KPI, performance measurement and event checks

[Scenario matrix](../README.md#traceable-scenario-coverage-matrix) | [Acceptance profiles](../README.md#acceptance-profiles) | [Evidence and stops](../README.md#evidence-and-safe-stop-codes)

**Status:** proposed test-observability contracts for all 175 catalogue cases. They are not deployed collectors, measured results, or standardized ISAC counter names. No vendor PM dictionary, approved thresholds, management interface or applicable specification edition has been supplied.

## What to check for a corresponding case

Find its ID in the case-focus table below. Collect **all measurement and event groups inherited from every acceptance profile in that case's README row**, then apply the focus checks. Compound cases inherit the union, not just a representative group. The original requirement, evidence and stop conditions still apply. If a quantity is genuinely inapplicable, record the reviewed rationale; missing telemetry is not an exclusion or a pass.

Distinguish:

- **Performance measurements (PM):** counters, gauges, sample distributions and timestamps from the actual radio, RAN, core, AI, application or facility. An event log is not automatically a PM counter.
- **KPI:** a defined aggregate or derived measure with units, denominator, window, dimensions and acceptance rule. Ground-truth detection quality cannot be inferred from network counters alone.
- **Event:** a timestamped state transition or request outcome. Count only unique logical occurrences under a declared deduplication rule. PM aggregates and event traces have separate completeness checks.
- **Alarm/audit evidence:** safety alarms, governance decisions and instrument records may be essential without being standardized PM events. PM exports must not be the sole independent safety-stop mechanism.

All `T-*` and `EV-*` identifiers here are **local documentation identifiers**. They do not assert a 3GPP measurement name, OID, vendor event code or production implementation. Map each to the real source dictionary before running a test. A specified 3GPP PM/KPI name can be used only with the exact applicable edition, clause, managed object, counting trigger, dimensions and implementation support. ISAC Stage-1 requirements alone do not define that mapping.

## Per-instance measurement contract

```text
instance_id, case_id, run_id, requirement_ids
acceptance_profiles, telemetry_contract_version, threshold_profile_version
measurement_id, kind: counter | gauge | histogram | raw-samples | timestamp-pair
definition, unit, source_component, actual_source_name, schema_version
standard_or_vendor_mapping: reference + edition/clause/object/trigger, or local
scope: site/cell/node/tenant/slice/job/stream + radio/mode/model/facility versions
window: start/end + baseline/fault/recovery phase + collection granularity
counter_semantics: cumulative or interval + reset/boot ID + wrap/drop handling
kpi: formula + numerator/denominator + percentile/matching rule + uncertainty
approval: limit + direction + units + approver/date + normative rule if applicable
events: event IDs + correlation IDs + ordering/deduplication/expiry rules
validity: missing/late/duplicate samples + time uncertainty + coverage status
evidence: raw artifacts + hashes + reduction script/version + result/disposition
```

Use synthetic/pseudonymous subscriber, object and tenant labels; do not expose production identifiers, personal data or secrets. Restrict detailed traces and retain them under approved policy. Use bounded-cardinality metric labels; correlate per-job/track detail in restricted event traces rather than creating an unbounded metric series.

## KPI calculation and validity rules

Approve exact thresholds before the run; this document supplies definitions, not universal numbers. Separate baseline, injected-fault and recovery windows, plus each required frequency, mode, scene and load stratum. Retain worst-required-stratum outcomes; pooled averages cannot hide a failure.

| Quantity | Definition and required qualification |
|---|---|
| Detection recall / miss fraction | Matched detections / independently labeled eligible object-observation opportunities; misses / the same denominator. Freeze matching tolerances and eligibility before execution. Report unobservable intervals separately; never remove observed failures after the fact. |
| Precision / false alarms | Matched true detections / all scored detections; unmatched false detections per declared scene time and, if relevant, area/volume. Define duplicate matching, class confusion, empty scenes and trial denominators. No truth labels means quality scoring is blocked. |
| Estimation error | Position/range/angle/velocity error against independently measured truth, with declared frame/units and truth uncertainty. Specify each observable's signed bias, error distribution and required percentiles. Resolution and estimation accuracy are different measurements. |
| Track continuity / freshness | Valid observed-track time / eligible truth-track time; separately count coasted/predicted, stale, lost and reacquired intervals. Observation age is consumer-use time minus original observation time, not inference duration. |
| Classification / uncertainty | Per-class precision/recall and confusion, unknown/abstention rates, and an approved confidence/uncertainty calibration measure with defined bins/scoring. Report output coverage and all rejected/expired/missing outcomes. A high confidence score proves neither identity nor intent. |
| Communication service | Delivered useful test payload bits / declared window; lost packets / eligible sent packets; required latency distributions and availability. Define service attempts, session lifecycle and protocol counting layer; retries and retransmissions must not silently inflate useful delivery. |
| Service/job outcomes | Offered, admitted, rejected, completed, failed, expired, cancelled and pending jobs, using unique logical IDs and a specified endpoint/window. Denominator and cohort are explicit; reconcile attempts separately from retried jobs and carry in-flight work across windows. |
| Queue/load behavior | Queue depth and oldest-item age, occupancy, offered/admitted/processed rates, shed/drop counts and retry-attempt amplification. Preserve peaks and distributions, not only means; declare capacities and counter resets. |
| Fault and restoration timing | Detection time minus injection/independent fault time; restored-valid time minus fault or recovery-start time, as approved. A restart is not restored validity. Track lost/duplicated accepted work and approved recovery point/time objectives. |
| Authorization/interlock correctness | Compare each test request against independently defined expected allow/deny and stop state; report unauthorized successes and missed prescribed stops explicitly. A zero failure count without the required attempts is not evidence. |
| OTA/RF validity | Use instrument quantities, corrections, method, units, traceability and expanded uncertainty as prescribed by the applicable method. Record valid/invalid runs and tested geometry; a software PM export cannot replace calibrated radiated measurement. |
| Telemetry completeness | Received unique required records / independently expected records or checkpoints under the approved collection contract; missing, late, duplicate, reset and dropped records are separate outcomes. Do not infer completeness from the same possibly broken collector. |

Never report a zero-denominator ratio as 0% or 100%; mark it unscorable and block any required criterion. Do not average percentiles or subtract cumulative counters across a reset. Specify histogram boundaries/overflow, percentile estimator, minimum samples and confidence rules. Account for clock offsets/uncertainty between components; absent synchronization blocks a required cross-component latency claim. Do not treat simulator steps as milliseconds.

## Measurement and event groups inherited by acceptance profile

Each group includes the measurements below, the listed lifecycle events, and visible collector failure (`EV-OBS`). Use the actual supported implementation names in the instance contract.

| Acceptance profile | Local group | PM/KPI inputs and owner | Required local event family |
|---|---|---|---|
| A-SEN | T-SEN | Sensing/fusion plus independent truth: eligible opportunities, matched/missed/false/duplicate detections, per-observable errors and valid/unobservable coverage | EV-SENSE |
| A-TRK | T-TRK | Track service: observed/coasted/lost/stale duration, association errors, observation age, reacquisition times | EV-TRACK |
| A-UNC | T-UNC | Classifier/fusion/operator: unknown, ambiguous, abstained and unsupported assertions; calibration and per-class outcomes with truth | EV-DECISION |
| A-COM | T-COM | RAN/transport/core/test endpoints: offered/delivered/lost payload, sessions, latency, resource use and service availability | EV-SERVICE |
| A-RAD | T-RAD | Radio/timing/calibration source: health, offset/drift, calibration residuals, invalid samples and equipment limit records | EV-RADIO |
| A-DAT | T-DAT | Ingestion/transport/audit: record counts, age/order, schema/frame validation, duplicates/drops, provenance and integrity outcomes | EV-DATA |
| A-RES | T-RES | Component/platform: fault/isolation/restart/degraded/restore times, rollback outcomes and accepted-work reconciliation | EV-RECOVERY |
| A-HUM | T-HUM | Mock notification/operator workflow: send/delivery/acknowledgement/escalation/ownership timings and outcomes | EV-NOTIFY |
| A-SAF | T-SAF | Independent facility/safety owner: authorization, stop/inhibit requests, independently observed safe-state times and missed stops | EV-SAFETY |
| A-CORE | T-CORE | Actual core/services: registration/session/API/job lifecycle counters, errors/timeouts, fan-out, queues/retries and state consistency | EV-CORE |
| A-ID | T-ID | Identity/track/tenant application: expected versus actual binding, scope checks, association conflicts and unauthorized disclosure outcomes | EV-IDENTITY |
| A-AI | T-AI | AI plus independent evaluator: per-model input/output/abstention/error counts, quality, runtime/queue age, compatible versions and drift | EV-AI |
| A-CTL | T-CTL | Independent policy/controller: recommendation/authorization/application/expiry/rollback counts and outcomes, rates and stability | EV-CONTROL |
| A-GOV | T-GOV | Data/model/access owner: approval/provenance, purpose/residency/access/retention decisions and revocation propagation | EV-GOVERNANCE |
| A-HF | T-HF | Radio/beam/instrument: exact band/waveform/panel, observation gaps/recovery, calibrated RF validity and impairment/thermal records | EV-HF |
| A-OTA | T-OTA | Facility/instrument/truth owner: calibration/quiet-zone/path corrections, valid/invalid runs, pose/scene/measurement uncertainty and repeatability | EV-OTA |

### Proposed event vocabulary

These are families, not a mandate to invent a standardized code. Preserve source, event name/version, unique event ID, event/ingest times, clock domain/uncertainty, run/instance, logical request/job/track correlation, before/after state, reason, validity and relevant configuration versions. Instrument and truth events must be correlated without being manufactured by the DUT.

| Family | Logical occurrences to map to real implementation evidence |
|---|---|
| EV-SENSE | Observation received/validated/invalidated; object present/absent truth checkpoint; detection produced/expired; sensing unavailable/unobservable |
| EV-TRACK | Track created/updated/coasted/stale/lost/reacquired/merged/split/retired; association conflict |
| EV-DECISION | Classification/unknown/ambiguous/abstention; unsupported assertion rejected; confidence/uncertainty validity change |
| EV-SERVICE | Test session/packet delivery outcomes; service unavailable/restored; communication resource/policy change |
| EV-RADIO | Timing/calibration validity transition; radio/chain health fault; limits/derating; readiness after recalibration |
| EV-DATA | Accepted/rejected/quarantined/late/duplicate record; schema/frame/provenance failure; stream gap; audit write failure |
| EV-RECOVERY | Independently applied fault; detected/isolated/degraded; restart/failover/rollback begun/completed/failed; restored-valid; work reconciliation |
| EV-NOTIFY | Notification requested/delivered/failed/expired; acknowledged/escalated; operator ownership changed |
| EV-SAFETY | Stop requested; independent inhibit applied/safe state verified/failed; permission/control/monitor lost; exercise abort |
| EV-CORE | Registration/session/API/job attempted/admitted/rejected/completed/failed/timed-out/cancelled/expired; discovery/routing/dependency change |
| EV-IDENTITY | Binding proposed/accepted/rejected/conflicting/expired; tenant boundary denial; authorization invalidated |
| EV-AI | Inference queued/started/completed/expired/failed/abstained; model loaded/rejected/promoted/rolled back; drift/evaluation unavailable |
| EV-CONTROL | Recommendation submitted; independently authorized/denied/applied/expired/cancelled; rollback and stop precedence |
| EV-GOVERNANCE | Data/model approved/rejected; restricted transfer/use denied; revocation issued/applied; retention/deletion disposition |
| EV-HF | Beam/panel/band state transition; acquisition/recovery; calibration/model compatibility failure; approved limit state |
| EV-OTA | Reference/calibration checked; setup/pose/scene changed; run started/valid/invalid; instrument/positioner/facility failure |
| EV-OBS | Collection/export stalled/dropped/duplicated/reset; schema/version mismatch; time-reference lost; evidence storage unavailable |

Expected event ordering and timing is instance-specific. Core-hosted AI does not make every component one clock or serial pipeline. An event trace may expose a missed/incorrect transition even when interval PM averages look healthy.

## Case-specific focus checks

For every row, also collect the complete profile-inherited groups above, their events, and EV-OBS. Case focus is **additional**, not a substitute for the acceptance profile or original diagram. Normative/local thresholds and expected event sequences are frozen per instance.

| Case | Focus measurements and events to inspect |
|---|---|
| TC-001 | Baseline detection/error distributions, service KPIs and calibration validity; observation-to-output trace. |
| TC-002 | Empty-scene duration, false/duplicate detections and unsupported assertions. |
| TC-003 | Metadata present/missing/conflicting, unknown decisions and authorization separation. |
| TC-004 | Per-confuser confusion/misses/false alarms; retain ambiguous decisions. |
| TC-005 | Per-weather/lighting quality and validity transitions, not pooled averages. |
| TC-006 | Observation gaps, track coast/stale/loss and unobservable state delivery. |
| TC-007 | Ghost/duplicate detections, multipath partitions, calibration validity. |
| TC-008 | Multi-object association swaps, duplicates, pending ambiguity and load. |
| TC-009 | Gap start, expiry/loss, reacquisition latency and identity lineage. |
| TC-010 | Independent communication/sensing availability and coverage-state disagreement. |
| TC-011 | With/without cooperation quality, missing identity and unknown outcomes. |
| TC-012 | Conflicting modality provenance, uncertainty and notification outcomes. |
| TC-013 | Communication resource reservation, sensing admission/quality and service tails. |
| TC-014 | Sensing-priority policy changes versus protected communication budgets. |
| TC-015 | Concurrent workloads, both service/quality budgets and oldest output age. |
| TC-016 | Inhibit/fallback events, communication continuity and stale sensing suppression. |
| TC-017 | Every directed mode transition, transient invalidity, rollback and latency. |
| TC-018 | Monostatic leakage/health limits and dependent observation invalidation. |
| TC-019 | Geometry/timing alignment errors, invalid transformations and estimates. |
| TC-020 | Node dropout/delay, surviving node set, degraded uncertainty and recovery. |
| TC-021 | Illumination loss versus object absence; passive availability state. |
| TC-022 | Actual interface units/frame/schema/calibration rejection and validity. |
| TC-023 | Configuration/beam/illumination changes and observation/service gaps. |
| TC-024 | UE/core state transitions and actual sensing/session dependencies. |
| TC-025 | Calibration residual/drift, invalidity declaration and revalidation. |
| TC-026 | Clock offset/drift/loss and dependent data age/validity and recovery. |
| TC-027 | Duplicate/reordered/stale counts, quarantine and track expiry. |
| TC-028 | Schema/unit/frame rejects; no success-shaped invalid outputs. |
| TC-029 | Unauthorized input/action attempts, explicit denials and audit completeness. |
| TC-030 | Stream/radio disconnect timing, stale suppression and health restoration. |
| TC-031 | Compute occupancy/queues, load shed, service tails and observation age. |
| TC-032 | Evidence-store/queue capacity, drops, write failures and visible invalidity. |
| TC-033 | Transport loss/delay, disconnected state, local continuity and restoration. |
| TC-034 | Dependency unavailability, retry amplification and service failures. |
| TC-035 | Restart/power-model state, readiness/calibration and accepted-work recovery. |
| TC-036 | Thermal warning/derating/shutdown and changed service resource budget. |
| TC-037 | Crash/restart loops, stale-state resurrection and restart resource growth. |
| TC-038 | Version compatibility rejection, update/rollback and qualified readiness. |
| TC-039 | Partition/failover, writer authority, duplicate decisions and reconciliation. |
| TC-040 | Notification delivery failure, acknowledgement absence and escalation. |
| TC-041 | Independently labeled benign exercise truth, service continuity and abort evidence. |
| TC-042 | Boundary/incursion notice, abort request and independent safe state. |
| TC-043 | Permission/control loss, escalation and independent stop authority. |
| TC-044 | Displayed age/uncertainty/conflicts versus actual evidence and operator decisions. |
| TC-045 | Alarm offered/delivered/acknowledged/expired load and handover ownership. |
| TC-046 | Unauthorized/expired mocked requests, denial reason and zero real actuation. |
| TC-047 | Missing/withdrawn approval, rejected actions and stop/revocation precedence. |
| TC-048 | Heartbeat/control loss, inhibit and independently verified stop latency. |
| TC-049 | Handoff delivery/acknowledgement and retained uncertainty/provenance. |
| TC-050 | Access/integrity/retention decisions, evidence availability and deletion policy. |
| TC-051 | Joint scene/load strata, sensing uncertainty and communication resource protection. |
| TC-052 | Combined clock/node loss, fusion-valid node set and restoration validity. |
| TC-053 | Compute backlog, oldest observation age and stale-work shedding. |
| TC-054 | Conflicting evidence plus failed delivery; no bypass of authorization. |
| TC-055 | Shared failure-domain losses, correlated state and recovery sequence. |
| TC-056 | Restart/version mismatch and rejected stale state before readiness. |
| TC-057 | Failover authority plus evidence loss; explicit missing-evidence state. |
| TC-058 | Stop during transition/recovery; no re-enable after inhibit. |
| TC-059 | Fault removal, dependency revalidation, calibrated restored-valid deadline. |
| TC-060 | Cycle counts, sustained queue/resource growth, drift and recurring faults. |
| TC-061 | Capability requests/admission/rejection, quotas and unsupported outcomes. |
| TC-062 | Registration/authentication cohorts, latency and synthetic identity decisions. |
| TC-063 | Session churn, retries, logical duplicates, pending states and resource leaks. |
| TC-064 | Mobility/paging events, session continuity and independent object association. |
| TC-065 | Actual sensing transport loss/age/QoS and communication contention. |
| TC-066 | Conflicting policy requests, independent precedence and enforced resources. |
| TC-067 | Per-tenant quotas/load/latency and unauthorized cross-binding/disclosure. |
| TC-068 | Authentication dependency loss, expiry/revocation propagation and stale caches. |
| TC-069 | Discovery/routing changes, retired endpoints and rediscovery timing. |
| TC-070 | Offered API attempts/jobs, errors/timeouts, retries and dependency pressure. |
| TC-071 | Fan-out, stalled consumers, cancellation/expiry and per-client authorization. |
| TC-072 | Analytics subscriptions, input/output age and unavailable analytics decisions. |
| TC-073 | Broker queue/age, duplicate/order/schema outcomes and dropped records. |
| TC-074 | Job cancel/retry/expiry ordering, orphan reservations and late outputs. |
| TC-075 | Leader/lease partition events, stale writers, conflict and convergence. |
| TC-076 | Failover/restore deadlines, session continuity and accepted-work loss/duplicates. |
| TC-077 | Partner boundary authorization, residency and provenance preservation. |
| TC-078 | Frame/time validation, transformation error and uncertainty propagation. |
| TC-079 | Quota/accounting state, rejected/admitted sensing and approved degraded policy. |
| TC-080 | Rollout/scale/drain events, incompatible APIs, service tails and rollback. |
| TC-081 | DNS/credential dependency failures, retries, rotation/expiry and recovery. |
| TC-082 | Revocation/deletion propagation, remaining copies and policy exceptions. |
| TC-083 | Per-priority test-service KPIs, sensing admission/rejection and resource limits. |
| TC-084 | Partial transaction state, lost replies, idempotent attempts and reconciliation. |
| TC-085 | Feature/version mismatches and explicit inference input rejection. |
| TC-086 | Non-finite/truncated inputs/outputs and failure/abstention outcomes. |
| TC-087 | Inference offered/admitted/completed/expired, queue/tail/age and communication budget. |
| TC-088 | Worker/accelerator faults, resource pressure and qualified restart/fallback. |
| TC-089 | Cold-start/cache/registry failures and readiness only after valid model load. |
| TC-090 | Late/cancelled inference, result discard/expiry and stale-track suppression. |
| TC-091 | Held-out strata quality, unsupported inputs and timely-output coverage. |
| TC-092 | Confidence calibration, ambiguity/abstention and coverage under load. |
| TC-093 | Unknown classes/identity claims, unsupported assertions and no hostility inference. |
| TC-094 | Drift signal, delayed labels, quality monitoring and revalidation gate. |
| TC-095 | Dataset overlap/skew, feature parity and independently reproduced scores. |
| TC-096 | Data purpose/residency/withdrawal, model lineage and approved disposition. |
| TC-097 | Corrupted labels/data, integrity failures and blocked model promotion. |
| TC-098 | Missing/misaligned modalities, valid-input set and qualified degraded outputs. |
| TC-099 | Correlated/duplicate sources, ensemble conflict and uncertainty inflation checks. |
| TC-100 | Per-runtime precision/numerical validity, quality distributions and compatibility. |
| TC-101 | Artifact digest/approval/dependency failures and denied model activation. |
| TC-102 | Canary/version mix, quality regression, track lineage and rollback convergence. |
| TC-103 | Training resource use versus inference/core queue and protected service budgets. |
| TC-104 | Training/evaluation lineage, reproducibility tolerance and approval gates. |
| TC-105 | Participant/update eligibility, dropout, convergence and transfer policy. |
| TC-106 | Feedback change rate/oscillation, policy denials and service impact. |
| TC-107 | Advisory/revoked control authority, independent denial and no real effector calls. |
| TC-108 | Decision age/model/evidence metadata and operator interpretation/notification. |
| TC-109 | Track/device/claimed identity lineage, conflicts and unauthorized bindings. |
| TC-110 | Untrusted-report handling, unsupported assertions and independent permissions. |
| TC-111 | Monitoring/evaluator unavailable, visible gaps and approved continued-use policy. |
| TC-112 | Independent AI stop, fallback validity, unknown state and communication continuity. |
| TC-113 | Original observation-to-consumer age, hop distributions, quality and notification. |
| TC-114 | Concurrent inference/registration/session cohorts, rejection and priority isolation. |
| TC-115 | Core partition and local observed/stale/degraded/fallback states. |
| TC-116 | Reconnection backlog age/version/authorization and discarded old decisions. |
| TC-117 | Shared cluster/storage/region outage, correlated loss and accepted-work restoration. |
| TC-118 | Ambiguous outputs plus notification failure, uncertainty and inhibited action. |
| TC-119 | In-flight revocation propagation at delivery/federation and remaining caches. |
| TC-120 | Timing/calibration invalidity versus model confidence and downstream status. |
| TC-121 | Multi-tenant pressure/failover, queues/resources and cache/authority boundaries. |
| TC-122 | Radio/mode/API/model compatibility, rejected transitions and rollback timing. |
| TC-123 | Stop/revocation ordering across recommendations/retries/failover/restart. |
| TC-124 | Backup versions/rights/accepted work and validated restoration readiness. |
| TC-125 | Cross-site association lineage independent of UE/session mobility events. |
| TC-126 | Evidence-store loss, governance enforcement gaps and restricted audit handling. |
| TC-127 | Long-duration jobs/sessions/resources/quality, resets and repeated restoration. |
| TC-128 | Every constituent contract and reviewer disposition, missing evidence and safe stop. |
| TC-129 | Per-band blockage opportunities, misses/gaps and unobservable state. |
| TC-130 | Separate sensing/communication beam recovery, scan gaps and resource cost. |
| TC-131 | Bandwidth/steering partitions, array response and unsupported regions. |
| TC-132 | Aperture/geometry model validity, measured bias and uncertainty. |
| TC-133 | Per-mechanism/path attenuation, selected model validity and service/sensing strata. |
| TC-134 | Material/aspect/polarization truth, scattering uncertainty and confusion. |
| TC-135 | Enclosure/configuration changes, loss/calibration invalidity and requalification. |
| TC-136 | Separate oscillator/phase/frequency impairments and estimator validity. |
| TC-137 | Calibrated saturation/leakage/dynamic range and approved RF limits. |
| TC-138 | Precision/clipping/bandwidth fixtures, input validity and AI quality. |
| TC-139 | Element/panel faults, aperture-valid state and recalibration readiness. |
| TC-140 | Thermal derating, resource/coverage changes and core notification. |
| TC-141 | Separate timing/frequency/phase/sample clocks and required uncertainty. |
| TC-142 | Supported waveform tuples, ambiguity/resolution/error and rejected configuration. |
| TC-143 | Instrument/quiet-zone/de-embedding validity and blocked hardware scoring. |
| TC-144 | Device/panel/UE state, sensing dependencies and distinct recovery timelines. |
| TC-145 | Band transition/fallback oscillation, stale carryover and service validity. |
| TC-146 | Band/hardware/model strata quality and rejected unsupported model domain. |
| TC-147 | Actual IQ/feature/track rates by interface, queue/age and core/AI pressure. |
| TC-148 | Cross-band time/frame/track lineage, duplicates and uncertainty. |
| TC-149 | Permission/limit/monitor withdrawal and independent inhibit verified. |
| TC-150 | Combined propagation/beam/load, quality/service degradation and restoration. |
| TC-151 | Radio/calibration/model manifest match before restart readiness. |
| TC-152 | Per-profile evidence closure and correct modality/reuse disposition. |
| TC-153 | Quiet-zone uniformity/usable volume/path loss/reflections and metrology validity. |
| TC-154 | Reference-plane/fixture correction, calibration expiry/mismatch and uncertainty. |
| TC-155 | Measured pattern/scan loss/sidelobes/polarization and untested regions. |
| TC-156 | Radiated power/emissions/exposure readings and independent interlock events. |
| TC-157 | Calibrated sensing RX noise/sensitivity/dynamic range/saturation invalidity. |
| TC-158 | Radiated truth-present/empty opportunities, misses/false alarms and strata. |
| TC-159 | Independent OTA range/angle/velocity errors, truth uncertainty and validity. |
| TC-160 | Fixture identity/aspect/geometry/model domain/time and invalid truth flags. |
| TC-161 | Chamber artifact/clutter/ghost/duplicate tracks and per-scene uncertainty. |
| TC-162 | Surveyed sensing coverage boundaries, blockage/gaps versus communication coverage. |
| TC-163 | Per-target aspect/polarization response and limited fixture generalization. |
| TC-164 | Sensing sweep gap/expiry/reacquisition separate from communication beam recovery. |
| TC-165 | Surveyed node/time geometry, dropout and estimator-specific synchronization. |
| TC-166 | Concurrent radiated sensing and communication budgets, transitions and gaps. |
| TC-167 | OTA acquisition-to-consumer timeline plus core/AI queues/rejection/quality. |
| TC-168 | Supported DUT pose/panel/UE states, motion and valid observation gaps. |
| TC-169 | Approved environmental corners, thermal/derating/recalibration/service validity. |
| TC-170 | Unit/panel/configuration spread, repeated runs and uncertainty without pooling failures. |
| TC-171 | Equivalent conducted/model/radiated quantities and separate validity evidence. |
| TC-172 | Pre/post reference drift, affected invalid runs and requalification timing. |
| TC-173 | OTA invalidity-to-RAN/core/AI/operator trace and suppression of confident stale tracks. |
| TC-174 | Independent facility/permission loss-to-RF-inhibit safe-state evidence. |
| TC-175 | All constituent OTA profiles, calibrated evidence, PM completeness and independent disposition. |

## Existing offline simulator: actual versus missing telemetry

`isac_lab.py` currently outputs only these `metrics` keys: `communication_dropped`, `sensing_dropped`, `peak_queue`, `queue_capacity`, `final_queue`, `rejected_observations`, `coasted_steps`, `lost_steps`, and `max_tracking_error`. `sensing_dropped` combines admission and queue-capacity losses; `rejected_observations` aggregates several validation causes. They cannot provide per-cause event counts without additional instrumentation.

The simulation's `steps`, coordinates, queues and radio units are abstract. It has no real clocked PM export, calibrated RF/OTA quantities, detector false-alarm scoring, standardized cell/core PM, model-quality evaluator or correlated lifecycle events. Its `passed` result evaluates its own limited rules, **not** a TC-001 through TC-175 instance, a deployment KPI, or the contracts here. This documentation change does not implement those missing collectors or change simulator behavior.

## Standards/vendor mapping prerequisites

Candidate official publication directories:

- **TS 28.552**, *Management and orchestration; 5G performance measurements*: https://www.etsi.org/deliver/etsi_ts/128500_128599/128552/.
- **TS 28.554**, *Management and orchestration; 5G end to end Key Performance Indicators (KPI)*: https://www.etsi.org/deliver/etsi_ts/128500_128599/128554/.
- **TS 28.550**, *Management and orchestration; Performance assurance*: https://www.etsi.org/deliver/etsi_ts/128500_128599/128550/.
- **TS 28.532**, *Management and orchestration; Generic management services*: https://www.etsi.org/deliver/etsi_ts/128500_128599/128532/.

Verify titles, applicable edition/clauses, managed object, reporting/collection method, counter/event semantics and vendor support before claiming normative mappings. Management-service specifications are not a universal catalogue of proprietary PM events. These references do not replace the README's ISAC service, RF/OTA, AI, safety and local requirement mappings.

**Verification boundary:** this change provides local measurement definitions and full case-focus traceability. It does not establish whether any particular current standard edition has standardized ISAC-specific measurements, nor assert their absence. No exact standard counter/event names or normative clauses have been validated. A product PM dictionary and applicable documents are required to complete the mapping.

## Acceptance gate

Every executed instance needs approved KPI definitions, actual PM/event sources, valid collection and time/truth references, and reproducible evidence reduction. Missing required PM/events or invalid metrology means blocked/unscorable for the affected criterion, never healthy-by-default. A missed independent stop remains a failure even if a PM collector failed.

Report separately: configured sources; applicable and unsupported measurements; expected/received records; valid/invalid windows; raw and derived KPI results; standard/vendor/local mapping status; failed/blocked criteria; residual gaps. A complete case-focus table is a coverage plan, not exhaustive implementation or executed evidence.
