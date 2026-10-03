# Duties and Responsibilities for Surgical Video Phase Recognition Node Agent

## Dual-Control Architecture
Maker:
phase-boundary-detector

Checker:
anatomical-safety-checker

## Operational Workflow
1. The Maker (phase-boundary-detector) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (anatomical-safety-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
