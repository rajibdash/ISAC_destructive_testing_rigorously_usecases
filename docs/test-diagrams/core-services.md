# Core-network and sensing-service stress: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-061

**What you test:** Sensing capability discovery/admission.

**Setup:** `C/B/M/R=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded synthetic jobs requesting<br/>supported, unavailable and unsupported sensing<br/>capabilities"]
    exercise["Exercise: Sensing capability discovery/admission. Test<br/>boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; calibration residuals, clock drift and<br/>equipment health. Retain: E3,E4,E7"]
    checks["Check: admit only authorized supported jobs within<br/>resource budgets; return explicit unsupported/overload<br/>outcomes"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-RAD. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S2,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-RAD.

## TC-062

**What you test:** UE registration and re-registration burst.

**Setup:** `C/B/U=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated UE emulator with synthetic<br/>subscribers, including absent/invalid subscriptions"]
    exercise["Exercise: UE registration and re-registration burst. Test<br/>boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput; identity/tenant binding, track lineage and<br/>access decisions. Retain: E2,E4,E7"]
    checks["Check: bound authentication/registration load; do not<br/>authenticate a sensed object from UE attachment"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM,A-ID. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S2,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-ID.

## TC-063

**What you test:** Session setup/modify/release churn.

**Setup:** `C/B/N=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic sessions, duplicated<br/>requests and delayed completions in isolated core"]
    exercise["Exercise: Session setup/modify/release churn. Test<br/>boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput. Retain: E2,E4,E7"]
    checks["Check: bound latency/state/resource leakage; reconcile<br/>retries without duplicate logical session effects"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-RES.

## TC-064

**What you test:** Device mobility, idle/paging and serving-node changes.

**Setup:** `C/B/U/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: UE/RAN emulator transitions with<br/>labeled sensing tracks"]
    exercise["Exercise: Device mobility, idle/paging and serving-node<br/>changes. Test boundary: Declared isolated core and sensing<br/>services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; track continuity, identity swaps, age and<br/>reacquisition time; identity/tenant binding, track lineage<br/>and access decisions. Retain: E1,E2,E7"]
    checks["Check: preserve only valid service continuity; UE mobility<br/>must not silently reassign object identity"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-TRK,A-ID. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S2,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-SEN,REQ-ID.

## TC-065

**What you test:** Sensing-data transport/UPF contention where applicable.

**Setup:** `C/B/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded isolated microbursts and<br/>sustained test traffic"]
    exercise["Exercise: Sensing-data transport/UPF contention where<br/>applicable. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput; track continuity, identity swaps, age and<br/>reacquisition time. Retain: E1,E2,E4,E7"]
    checks["Check: enforce declared QoS and freshness; measure<br/>loss/age across the actual sensing transport"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM,A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S1,S2,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-SEN.

## TC-066

**What you test:** Policy conflicts and admission priority.

**Setup:** `C/B/M/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock competing communication/sensing<br/>policy updates"]
    exercise["Exercise: Policy conflicts and admission priority. Test<br/>boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput; control permissions, scope/expiry, stability<br/>and stop precedence. Retain: E2,E6,E7,E9"]
    checks["Check: explicit policy precedence and rejection; RAN/core<br/>enforcement agree without unapproved priority escalation"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S5,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM,A-CTL. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E6: operator actions, mock calls, interlocks and stops; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S2,S5,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-CTL.

## TC-067

**What you test:** Tenant/slice isolation and noisy neighbors.

**Setup:** `C/B/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic tenants with independently<br/>bounded load and overlapping job identifiers"]
    exercise["Exercise: Tenant/slice isolation and noisy neighbors. Test<br/>boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput; identity/tenant binding, track lineage and<br/>access decisions. Retain: E2,E4,E7,E9"]
    checks["Check: enforce per-tenant resource/data isolation; no<br/>cross-tenant result delivery"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM,A-ID. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S2,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-ID.

## TC-068

**What you test:** Authentication/subscription dependency loss and revocation.

**Setup:** `C/B/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock AUSF/UDM/UDR unavailability,<br/>expiry and test credential revocation"]
    exercise["Exercise: Authentication/subscription dependency loss and<br/>revocation. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; identity/tenant binding, track lineage and<br/>access decisions; purpose/residency, approvals, revocation<br/>and retention/deletion. Retain: E4,E5,E7"]
    checks["Check: bounded failure and approved existing-session<br/>policy; no unauthorized access via stale caches"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S4,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-ID,A-GOV. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-ID,REQ-GOV.

## TC-069

**What you test:** Discovery/routing staleness during scaling.

**Setup:** `C/B/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated NRF/service-registry updates<br/>and stale endpoint fixtures"]
    exercise["Exercise: Discovery/routing staleness during scaling. Test<br/>boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; fault isolation, degraded state, restoration<br/>and rollback. Retain: E4,E7"]
    checks["Check: avoid retired/unready endpoints, bound rediscovery<br/>and preserve explicit failures"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-RES.

## TC-070

**What you test:** Service API/SCP overload and retry amplification.

**Setup:** `C/B=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Bounded API load, timeouts and<br/>explicit overload responses in isolated services"]
    exercise["Exercise: Service API/SCP overload and retry<br/>amplification. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput. Retain: E4,E7"]
    checks["Check: honor retry/deadline budgets and backpressure;<br/>dependency load stays within approved limits"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S1,S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-RES.

## TC-071

**What you test:** Exposure/subscription fan-out and slow consumers.

**Setup:** `C/B/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock NEF/AF or declared service<br/>clients, stalled callbacks and cancellations"]
    exercise["Exercise: Exposure/subscription fan-out and slow<br/>consumers. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; freshness, ordering, validation, access and<br/>audit completeness; identity/tenant binding, track lineage<br/>and access decisions. Retain: E4,E5,E7"]
    checks["Check: quota/authorization enforced; slow consumer does<br/>not block others or receive expired data"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-DAT,A-ID. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-DAT,REQ-ID.

## TC-072

**What you test:** NWDAF analytics load, expiry and unavailable input.

**Setup:** `C/B/J=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic analytics subscriptions and<br/>stale/missing network counters"]
    exercise["Exercise: NWDAF analytics load, expiry and unavailable<br/>input. Test boundary: Declared isolated core and sensing<br/>services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; freshness, ordering, validation, access and<br/>audit completeness; control permissions, scope/expiry,<br/>stability and stop precedence. Retain: E4,E7,E8"]
    checks["Check: expose stale/unavailable analytics; no substitution<br/>for physical-object ground truth or unchecked control"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-DAT,A-CTL. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-DAT,REQ-CTL.

## TC-073

**What you test:** Event/observation broker backlog and schema evolution.

**Setup:** `C/B/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Versioned fixtures with duplicates,<br/>reordering and bounded broker pressure"]
    exercise["Exercise: Event/observation broker backlog and schema<br/>evolution. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; freshness, ordering, validation, access and<br/>audit completeness; track continuity, identity swaps, age<br/>and reacquisition time. Retain: E4,E5,E7"]
    checks["Check: validate compatibility, bound age and make<br/>loss/replay visible"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-DAT,A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-DAT,REQ-SEN.

## TC-074

**What you test:** Sensing-job cancel/retry/expiry race.

**Setup:** `C/B/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Test job requests with delayed<br/>acknowledgements and cancellation during execution"]
    exercise["Exercise: Sensing-job cancel/retry/expiry race. Test<br/>boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; control permissions, scope/expiry, stability<br/>and stop precedence. Retain: E4,E6,E7"]
    checks["Check: one authoritative lifecycle, no orphan resources or<br/>output accepted after cancellation/expiry"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S4,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-CTL. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-RES,REQ-CTL.

## TC-075

**What you test:** Core/application state-store partition and leader conflict.

**Setup:** `C/N=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated replica partition and stale<br/>lease fixture"]
    exercise["Exercise: Core/application state-store partition and<br/>leader conflict. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; fault isolation, degraded state, restoration<br/>and rollback; control permissions, scope/expiry, stability<br/>and stop precedence. Retain: E4,E7,E9"]
    checks["Check: fence stale writers and reconcile state;<br/>unavailable authority is not silently duplicated"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S4,S5,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-RES,A-CTL. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S4,S5,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-RES,REQ-CTL.

## TC-076

**What you test:** Regional/core-service failover and restoration.

**Setup:** `C/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated service outage with<br/>synthetic accepted jobs/sessions"]
    exercise["Exercise: Regional/core-service failover and restoration.<br/>Test boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput; fault isolation, degraded state, restoration<br/>and rollback. Retain: E2,E4,E7,E9"]
    checks["Check: meet approved recovery point/time objectives and<br/>reconcile accepted/lost work explicitly"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-RES.

## TC-077

**What you test:** Inter-operator/federated/roaming boundary where supported.

**Setup:** `C/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock partner core and purpose-limited<br/>synthetic observations"]
    exercise["Exercise: Inter-operator/federated/roaming boundary where<br/>supported. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; identity/tenant binding, track lineage and<br/>access decisions; purpose/residency, approvals, revocation<br/>and retention/deletion. Retain: E5,E7,E9"]
    checks["Check: enforce authorization, residency and uncertainty<br/>provenance across boundary; no implied sensing-data<br/>sharing right"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-ID,A-GOV. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-ID,REQ-GOV.

## TC-078

**What you test:** Core location/time/frame metadata stale or conflicting.

**Setup:** `C/G/R=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Labeled coordinate/time fixtures<br/>through declared location/fusion services"]
    exercise["Exercise: Core location/time/frame metadata stale or<br/>conflicting. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures: calibration<br/>residuals, clock drift and equipment health; freshness,<br/>ordering, validation, access and audit completeness; track<br/>continuity, identity swaps, age and reacquisition time.<br/>Retain: E1,E3,E7"]
    checks["Check: reject invalid transformations and propagate<br/>clock/frame uncertainty to consumers"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-RAD,A-DAT,A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-RAD,REQ-DAT,REQ-SEN.

## TC-079

**What you test:** Quota/accounting/charging dependency outage.

**Setup:** `C/B/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated counters, quota changes and<br/>mock accounting unavailability"]
    exercise["Exercise: Quota/accounting/charging dependency outage.<br/>Test boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput; purpose/residency, approvals, revocation and<br/>retention/deletion. Retain: E2,E4,E7,E9"]
    checks["Check: explicit approved entitlement/degraded policy; no<br/>silent service denial or unbounded sensing admission"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM,A-GOV. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S2,S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-GOV.

## TC-080

**What you test:** Core rolling upgrade/autoscale with active jobs.

**Setup:** `C/B/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved isolated rollout, scale-in<br/>and incompatible API fixture"]
    exercise["Exercise: Core rolling upgrade/autoscale with active jobs.<br/>Test boundary: Declared isolated core and sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; session availability, loss, latency and<br/>throughput; fault isolation, degraded state, restoration<br/>and rollback. Retain: E2,E4,E7,E9"]
    checks["Check: drain/reassign work, reject incompatible versions<br/>and restore qualified baseline"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-COM,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-COM,REQ-RES.

## TC-081

**What you test:** Shared DNS/PKI/secret service failure or rotation.

**Setup:** `C/H/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock resolution failure and test<br/>certificate/token expiry/rotation"]
    exercise["Exercise: Shared DNS/PKI/secret service failure or<br/>rotation. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; identity/tenant binding, track lineage and<br/>access decisions; fault isolation, degraded state,<br/>restoration and rollback. Retain: E4,E5,E7"]
    checks["Check: bounded retries and recovery without disabling<br/>authentication or accepting revoked identities"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S4,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-ID,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S4,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-ID,REQ-RES.

## TC-082

**What you test:** Purpose/permission withdrawal and retention propagation.

**Setup:** `C/H=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Synthetic revocation/deletion<br/>fixtures across caches, replicas and derived outputs"]
    exercise["Exercise: Purpose/permission withdrawal and retention<br/>propagation. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures: freshness,<br/>ordering, validation, access and audit completeness;<br/>purpose/residency, approvals, revocation and<br/>retention/deletion. Retain: E5,E7,E9"]
    checks["Check: enforce approved legal retention/deletion basis and<br/>approved propagation deadline; expose residual copies"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3,S7. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-DAT,A-GOV. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E5: input provenance, validation, access and integrity; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S3,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-DAT,REQ-GOV.

## TC-083

**What you test:** Communication/emergency-service priority under sensing load.

**Setup:** `C/B/M/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Isolated test sessions representing<br/>approved priority classes, never real emergency numbers"]
    exercise["Exercise: Communication/emergency-service priority under<br/>sensing load. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures: session<br/>availability, loss, latency and throughput;<br/>admission/completion/rejection, queues, retries and state<br/>consistency. Retain: E2,E4,E7"]
    checks["Check: preserve approved service budgets and visibly<br/>reject excess sensing demand"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S2,S4. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-COM,A-CORE. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces.

**Stop plan:** S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-COM,REQ-CORE,REQ-SAF.

## TC-084

**What you test:** Partial core transaction completion and lost acknowledgement.

**Setup:** `C/B/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Fail isolated service between<br/>resource reservation, state update and reply"]
    exercise["Exercise: Partial core transaction completion and lost<br/>acknowledgement. Test boundary: Declared isolated core and<br/>sensing services"]
    capture["Measure against approved truth / fixtures:<br/>admission/completion/rejection, queues, retries and state<br/>consistency; fault isolation, degraded state, restoration<br/>and rollback. Retain: E4,E7,E9"]
    checks["Check: idempotent retry or explicit reconciliation; no<br/>false success, orphan reservation or duplicate logical<br/>action"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S4,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-CORE,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E9: approvals, lineage, rollout and governance/control audit.

**Stop plan:** S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-CORE,REQ-RES,REQ-CTL.
