# Radiated OTA qualification for ISAC-enabled systems: designer test diagrams

[Visual guide and shared execution rules](../../README.md#designer-visual-test-guide) | [Authoritative scenario matrix](../../README.md#traceable-scenario-coverage-matrix)

**KPI / PM events:** use each TC ID in the [case-focus table](../kpi-pm.md#case-specific-focus-checks), plus all measurement/event groups inherited from its acceptance profiles. Actual collector names and thresholds need approval; local event labels are not standardized counters.

These are test-design flows, not measured results or an asserted deployment architecture. Solid arrows show the test/evidence flow; dashed arrows show independent stop control. Apply the shared approval gate before every instance. Expand the declared axes and frequency overlay; never treat one diagram as coverage of every configuration.

## TC-153

**What you test:** OTA facility, quiet-zone and range qualification.

**Setup:** `K/R=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Calibrated reference antenna/probe,<br/>approved positioner grid and facility-monitor checks"]
    exercise["Exercise: OTA facility, quiet-zone and range<br/>qualification. Test boundary: Qualified shielded OTA setup<br/>and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>calibration residuals, clock drift and equipment health.<br/>Retain: E3,E10,E11"]
    checks["Check: validate quiet-zone/field uniformity, usable<br/>volume, path loss, reflections and measurement uncertainty<br/>at each test frequency; invalid volume blocks DUT<br/>acceptance"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-RAD. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-RAD,REQ-HF.

## TC-154

**What you test:** Reference-plane, cable/fixture de-embedding and path-loss calibration.

**Setup:** `K/R/D=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Traceable reference artifacts and<br/>approved cable/fixture configuration"]
    exercise["Exercise: Reference-plane, cable/fixture de-embedding and<br/>path-loss calibration. Test boundary: Qualified shielded<br/>OTA setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>calibration residuals, clock drift and equipment health.<br/>Retain: E3,E10,E11"]
    checks["Check: calibration applies to the actual ports,<br/>polarization, frequency and setup; retain correction<br/>uncertainty and reject expired/mismatched calibration"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-RAD. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-RAD.

## TC-155

**What you test:** Radiated antenna/array pattern, scan-volume and polarization coverage.

**Setup:** `K/R/W/D=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Shielded chamber angular/polarization<br/>sweep within the declared supported envelope"]
    exercise["Exercise: Radiated antenna/array pattern, scan-volume and<br/>polarization coverage. Test boundary: Qualified shielded<br/>OTA setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>per-band calibration, beam gaps, RF quality and operating<br/>limits. Retain: E1,E3,E10,E11"]
    checks["Check: map realized pattern, scan loss, sidelobe behavior<br/>and unsupported regions against approved requirements; do<br/>not infer sensing coverage from communication pattern<br/>alone"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-HF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-HF,REQ-SEN.

## TC-156

**What you test:** Transmit power, radiated emissions and configuration-dependent limits.

**Setup:** `K/R/D/W=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved test waveform at authorized<br/>settings with independent calibrated monitoring"]
    exercise["Exercise: Transmit power, radiated emissions and<br/>configuration-dependent limits. Test boundary: Qualified<br/>shielded OTA setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>per-band calibration, beam gaps, RF quality and operating<br/>limits; authorization, interlocks, stop deadlines and safe<br/>state. Retain: E2,E3,E10,E11"]
    checks["Check: verify applicable normative/local emission and<br/>exposure limits for each supported transmit state;<br/>interlock prevents output outside the approved envelope"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S5. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-HF,A-SAF. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-HF,REQ-SAF.

## TC-157

**What you test:** OTA receiver sensitivity, noise floor, dynamic range and saturation.

**Setup:** `K/R/D=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Calibrated chamber reference levels<br/>and bounded attenuation/level steps"]
    exercise["Exercise: OTA receiver sensitivity, noise floor, dynamic<br/>range and saturation. Test boundary: Qualified shielded<br/>OTA setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>calibration residuals, clock drift and equipment health;<br/>detections, misses, false alarms, position/velocity error.<br/>Retain: E1,E3,E10,E11"]
    checks["Check: characterize sensing receiver valid-input range and<br/>invalid/saturated indication; do not substitute UE/BS<br/>communication conformance for sensing-receiver<br/>qualification"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-RAD,A-SEN. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-RAD,REQ-SEN.

## TC-158

**What you test:** Radiated reference-scene detection and false-alarm performance.

**Setup:** `K/G/R/V=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Repeatable shielded OTA scene with<br/>independently labeled object-present and empty-scene<br/>trials"]
    exercise["Exercise: Radiated reference-scene detection and false-<br/>alarm performance. Test boundary: Qualified shielded OTA<br/>setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>detections, misses, false alarms, position/velocity error;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E3,E10,E11"]
    checks["Check: report per-stratum detection, misses and false<br/>alarms with declared denominators; preserve<br/>unknown/unobservable outcomes and approved confidence<br/>bounds"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-SEN,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-UNC.

## TC-159

**What you test:** OTA range, angle and velocity estimation accuracy/uncertainty.

**Setup:** `K/G/R/D=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Non-hazardous calibrated<br/>static/moving reference fixture with independent truth and<br/>uncertainty"]
    exercise["Exercise: OTA range, angle and velocity estimation<br/>accuracy/uncertainty. Test boundary: Qualified shielded<br/>OTA setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>detections, misses, false alarms, position/velocity error;<br/>track continuity, identity swaps, age and reacquisition<br/>time; unknown/ambiguous decisions and confidence<br/>calibration. Retain: E1,E3,E10,E11"]
    checks["Check: score each implemented observable independently<br/>over the declared measurement volume; no inferred<br/>identification or intent"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-SEN,A-TRK,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-UNC.

## TC-160

**What you test:** OTA target/reference-fixture and scene-truth validity.

**Setup:** `K/G/X/V=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Characterized reference targets or<br/>validated target emulator at recorded positions/aspects"]
    exercise["Exercise: OTA target/reference-fixture and scene-truth<br/>validity. Test boundary: Qualified shielded OTA setup and<br/>isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>freshness, ordering, validation, access and audit<br/>completeness; unknown/ambiguous decisions and confidence<br/>calibration. Retain: E1,E3,E5,E10,E11"]
    checks["Check: verify fixture identity, geometry, material/model<br/>domain and truth timestamps; invalid or out-of-domain<br/>truth invalidates scoring"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-DAT,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E5: input provenance, validation, access and integrity; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-DAT,REQ-UNC.

## TC-161

**What you test:** Chamber multipath, clutter and ghost-track response.

**Setup:** `K/G/V=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Qualified absorber/reflector<br/>arrangements and labeled benign clutter configurations"]
    exercise["Exercise: Chamber multipath, clutter and ghost-track<br/>response. Test boundary: Qualified shielded OTA setup and<br/>isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>detections, misses, false alarms, position/velocity error;<br/>track continuity, identity swaps, age and reacquisition<br/>time. Retain: E1,E3,E10,E11"]
    checks["Check: quantify false/duplicate tracks and uncertainty by<br/>scene; expose chamber artifacts rather than attributing<br/>them to the target or system performance"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-SEN,A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-UNC.

## TC-162

**What you test:** Radiated blockage and sensing-coverage boundary.

**Setup:** `K/G/R/U/V=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Approved absorber/occluder fixtures<br/>and surveyed positions inside the chamber"]
    exercise["Exercise: Radiated blockage and sensing-coverage boundary.<br/>Test boundary: Qualified shielded OTA setup and isolated<br/>services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>detections, misses, false alarms, position/velocity error;<br/>track continuity, identity swaps, age and reacquisition<br/>time. Retain: E1,E3,E10,E11"]
    checks["Check: map valid, degraded and unobservable regions;<br/>distinguish sensing gaps from communication coverage and<br/>target absence"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-SEN,A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-UNC.

## TC-163

**What you test:** Target aspect, polarization and orientation sensitivity.

**Setup:** `K/G/R/X=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Positioner-controlled non-hazardous<br/>reference fixture with recorded orientation/polarization"]
    exercise["Exercise: Target aspect, polarization and orientation<br/>sensitivity. Test boundary: Qualified shielded OTA setup<br/>and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>detections, misses, false alarms, position/velocity error;<br/>unknown/ambiguous decisions and confidence calibration.<br/>Retain: E1,E3,E10,E11"]
    checks["Check: report per-aspect/polarization performance and<br/>model limitations; do not generalize one fixture<br/>orientation to all objects"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-SEN,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-UNC.

## TC-164

**What you test:** Sensing-beam sweep, acquisition gaps and reacquisition.

**Setup:** `K/W/R/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Scripted supported beam states and<br/>reference target motion in shielded OTA"]
    exercise["Exercise: Sensing-beam sweep, acquisition gaps and<br/>reacquisition. Test boundary: Qualified shielded OTA setup<br/>and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>track continuity, identity swaps, age and reacquisition<br/>time; session availability, loss, latency and throughput.<br/>Retain: E1,E2,E3,E4,E10,E11"]
    checks["Check: measure observation gaps and reacquisition<br/>separately from communication beam recovery; invalidate<br/>stale tracks until sensing evidence is current"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-TRK,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S2,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-COM.

## TC-165

**What you test:** Multi-radio/bistatic/multistatic OTA alignment and fusion.

**Setup:** applicable `K/G/N/X`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Surveyed shielded multi-node geometry<br/>with independent timing/position truth and node dropout<br/>replay"]
    exercise["Exercise: Multi-radio/bistatic/multistatic OTA alignment<br/>and fusion. Test boundary: Qualified shielded OTA setup<br/>and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>calibration residuals, clock drift and equipment health;<br/>track continuity, identity swaps, age and reacquisition<br/>time; unknown/ambiguous decisions and confidence<br/>calibration. Retain: E1,E3,E4,E7,E10,E11"]
    checks["Check: enforce only declared synchronization/coherence<br/>needs and propagate geometry/time uncertainty; degraded<br/>node sets cannot appear fully healthy"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-RAD,A-TRK,A-UNC. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-RAD,REQ-SEN,REQ-UNC.

## TC-166

**What you test:** Joint communication-and-sensing radiated operation.

**Setup:** `K/M/W/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: OTA reference scene during bounded<br/>synthetic communication traffic over an isolated network"]
    exercise["Exercise: Joint communication-and-sensing radiated<br/>operation. Test boundary: Qualified shielded OTA setup and<br/>isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>detections, misses, false alarms, position/velocity error;<br/>session availability, loss, latency and throughput.<br/>Retain: E1,E2,E3,E4,E10,E11"]
    checks["Check: meet approved sensing and communications bounds<br/>simultaneously, including resource transitions and<br/>observation gaps"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-SEN,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S2,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-COM.

## TC-167

**What you test:** End-to-end OTA sensing path under core/AI load.

**Setup:** `K/C/B/J/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Timestamped OTA truth/observations<br/>and bounded synthetic core/AI/API workloads in isolation"]
    exercise["Exercise: End-to-end OTA sensing path under core/AI load.<br/>Test boundary: Qualified shielded OTA setup and isolated<br/>services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>admission/completion/rejection, queues, retries and state<br/>consistency; AI quality, abstention, calibration,<br/>numerical validity and latency; track continuity, identity<br/>swaps, age and reacquisition time; session availability,<br/>loss, latency and throughput. Retain:<br/>E1,E2,E4,E7,E8,E10,E11"]
    checks["Check: correlate radiated acquisition through consumer<br/>delivery, enforce age/quality budgets and show<br/>rejected/expired work; no fabricated result on overload"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3,S4. Watch throughout<br/>the run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-CORE,A-AI,A-TRK,A-COM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E4: faults, queues, alarms and recovery state; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S2,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-CORE,REQ-AI,REQ-SEN.

## TC-168

**What you test:** Supported device/panel orientation, state and repeatable mobility profile.

**Setup:** `K/R/U/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Shielded OTA positioner or UE/panel<br/>emulator with synthetic sessions and bounded motion"]
    exercise["Exercise: Supported device/panel orientation, state and<br/>repeatable mobility profile. Test boundary: Qualified<br/>shielded OTA setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>session availability, loss, latency and throughput; track<br/>continuity, identity swaps, age and reacquisition time.<br/>Retain: E1,E2,E3,E10,E11"]
    checks["Check: test only supported orientations/states; separate<br/>UE-dependent behavior from network-side sensing and report<br/>coverage gaps"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-COM,A-TRK. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S2,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-COM.

## TC-169

**What you test:** Approved environmental/thermal operating corners during OTA.

**Setup:** `K/R/V/Q=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Chamber environmental setpoints and<br/>bounded workload within equipment/facility ratings; no<br/>deliberate overheating"]
    exercise["Exercise: Approved environmental/thermal operating corners<br/>during OTA. Test boundary: Qualified shielded OTA setup<br/>and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>per-band calibration, beam gaps, RF quality and operating<br/>limits; fault isolation, degraded state, restoration and<br/>rollback. Retain: E2,E3,E4,E10,E11"]
    checks["Check: verify derating, recalibration and<br/>sensing/communication validity at approved corners; stop<br/>before any equipment or facility limit is approached"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-HF,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S2,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-HF,REQ-RES.

## TC-170

**What you test:** Unit-to-unit, panel and configuration repeatability.

**Setup:** `K/R/D/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Multiple approved units or repeated<br/>fixture runs using controlled setup and reference<br/>artifacts"]
    exercise["Exercise: Unit-to-unit, panel and configuration<br/>repeatability. Test boundary: Qualified shielded OTA setup<br/>and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>calibration residuals, clock drift and equipment health;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E3,E9,E10,E11"]
    checks["Check: report unit/configuration spread and<br/>reproducibility with measurement uncertainty; do not pool<br/>away a failing unit or unsupported configuration"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-RAD,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E3: radio, timing, calibration and instrument health; E9: approvals, lineage, rollout and governance/control audit; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-RAD,REQ-RES.

## TC-171

**What you test:** Conducted/model-to-radiated correlation and evidence separation.

**Setup:** `K/R=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Matched reference configuration<br/>measured in conducted setup, qualified OTA facility and<br/>simulator"]
    exercise["Exercise: Conducted/model-to-radiated correlation and<br/>evidence separation. Test boundary: Qualified shielded OTA<br/>setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>calibration residuals, clock drift and equipment health.<br/>Retain: E1,E3,E10,E11"]
    checks["Check: compare only equivalent quantities and document<br/>uncertainty/domain differences; conducted or simulated<br/>evidence cannot substitute for antenna/chamber evidence"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3. Watch throughout the run;<br/>use the approved trigger and safe action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-RAD. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-RAD.

## TC-172

**What you test:** OTA setup drift, recalibration and before/after stability.

**Setup:** `K/R/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Repeat reference checks across<br/>approved run duration and setup changes"]
    exercise["Exercise: OTA setup drift, recalibration and before/after<br/>stability. Test boundary: Qualified shielded OTA setup and<br/>isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>calibration residuals, clock drift and equipment health;<br/>fault isolation, degraded state, restoration and rollback.<br/>Retain: E3,E4,E10,E11"]
    checks["Check: detect drift beyond approved limits, invalidate<br/>affected runs and require documented recalibration/retest<br/>before resuming"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3,S4. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-RAD,A-RES. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3,S4; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-RAD,REQ-RES.

## TC-173

**What you test:** OTA fault/degraded-state propagation to RAN, core, AI and operator.

**Setup:** `K/R/C/J/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Shielded OTA reference scene with<br/>isolated calibration/beam-health fault and mocked consumer"]
    exercise["Exercise: OTA fault/degraded-state propagation to RAN,<br/>core, AI and operator. Test boundary: Qualified shielded<br/>OTA setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>unknown/ambiguous decisions and confidence calibration;<br/>admission/completion/rejection, queues, retries and state<br/>consistency; AI quality, abstention, calibration,<br/>numerical validity and latency; alarm delivery,<br/>acknowledgement, decisions and operator workload. Retain:<br/>E1,E3,E4,E6,E7,E8,E10,E11"]
    checks["Check: invalid radiated observations become visibly<br/>degraded/unavailable end-to-end and are not presented as<br/>confident current tracks"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S3,S4,S5. Watch throughout<br/>the run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-UNC,A-CORE,A-AI,A-HUM. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S3,S4,S5; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SEN,REQ-CORE,REQ-AI,REQ-HUM.

## TC-174

**What you test:** Facility loss, RF inhibit and independent safe-stop behavior.

**Setup:** `K/R/H/L=ALL`. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Mock facility-monitor, authorization<br/>or containment-state withdrawal with RF source in approved<br/>isolated setup"]
    exercise["Exercise: Facility loss, RF inhibit and independent safe-<br/>stop behavior. Test boundary: Qualified shielded OTA setup<br/>and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>authorization, interlocks, stop deadlines and safe state;<br/>purpose/residency, approvals, revocation and<br/>retention/deletion. Retain: E3,E4,E6,E9,E10,E11"]
    checks["Check: independently inhibit radiated output on invalid<br/>permission/monitor state, preserve event evidence and<br/>verify safe-state indication"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S5,S7. Watch throughout the<br/>run; use the approved trigger and safe action for each<br/>code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA,A-SAF,A-GOV. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E6: operator actions, mock calls, interlocks and stops; E9: approvals, lineage, rollout and governance/control audit; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S5,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-SAF,REQ-GOV.

## TC-175

**What you test:** OTA acceptance pack, traceability and independent evidence review.

**Setup:** all applicable axes. Create an approved instance with ground truth, baseline, limits and a named independent stop owner. Apply the exact frequency configuration and its reviewed applicability.

<details>
<summary>Show test flow and independent stop path</summary>

```mermaid
flowchart TD
    stimulus["Apply safe stimulus: Replay approved OTA acceptance pack<br/>with independent facility, RF, sensing, core/AI and safety<br/>reviewers"]
    exercise["Exercise: OTA acceptance pack, traceability and<br/>independent evidence review. Test boundary: Qualified<br/>shielded OTA setup and isolated services"]
    capture["Measure against approved truth / fixtures: radiated<br/>metrology, sensing error/uncertainty and repeatability;<br/>every metric required by constituent instances. Retain:<br/>E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11"]
    checks["Check: close each applicable configuration/requirement<br/>with linked calibrated radiated evidence, uncertainty,<br/>limitations and disposition; no unresolved blocker<br/>reported as pass"]
    disposition["Record pass / fail / blocked / aborted with evidence;<br/>restore and revalidate if applicable"]
    monitor["Independent stop monitor: S1,S2,S3,S4,S5,S7. Watch<br/>throughout the run; use the approved trigger and safe<br/>action for each code."]
    safe["Stop stimulus / dependent outputs as prescribed; preserve<br/>evidence and record disposition before retest"]
    stimulus --> exercise --> capture --> checks --> disposition
    monitor -. "monitors / can cut off" .-> stimulus
    monitor -. "on trigger: stop takes precedence" .-> safe
```

</details>

**Measure against:** A-OTA plus all constituent profiles. [Use every applicable metric and the approved limits](../../README.md#acceptance-profiles); the case-specific check does not replace those profiles.

**Retain:** E1: scene truth, detections, tracks and scores; E2: test communication traffic and service KPIs; E3: radio, timing, calibration and instrument health; E4: faults, queues, alarms and recovery state; E5: input provenance, validation, access and integrity; E6: operator actions, mock calls, interlocks and stops; E7: synthetic identities, core APIs and distributed traces; E8: dataset/model versions, AI outputs and quality telemetry; E9: approvals, lineage, rollout and governance/control audit; E10: frequency/beam manifest and qualified RF/model evidence; E11: calibrated radiated OTA setup, truth and uncertainty.

**Stop plan:** S1,S2,S3,S4,S5,S7; [trigger definitions and safe outcomes](../../README.md#evidence-and-safe-stop-codes). **Requirements:** REQ-OTA,REQ-HF,REQ-SEN,REQ-COM,REQ-CORE,REQ-AI,REQ-SAF.
