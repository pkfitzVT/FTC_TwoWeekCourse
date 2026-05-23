# Proposed File Move Plan

This is an organization plan only. Do not move, rename, delete, or archive files until the plan is reviewed and approved.

The plan follows the current source policy:

- Markdown files are source files unless clearly utility/local.
- PDFs are generated exports unless otherwise noted.
- Packet PDFs should eventually have manifests listing their source Markdown files.
- Duplicate or overlapping files should be reviewed manually before any move/rename/archive action.

## Review Flags

- Day 1 Session 1 source-of-truth decision has been applied:
  - `02_student_materials/readings/day1_session1_what_is_first.md` and `02_student_materials/readings/day1_session1_what_is_first_tech_challenge.md` are the source files.
  - `99_archive_or_local/day1_session1_first_ftc_handouts.md` is kept only as an archived combined duplicate/reference.
- Packet PDFs were moved to `05_print_packets/`, but still need source manifests before relying on them as stable print packets.
- `02_student_materials/readings/future_human_controller_mapping_background.md` is useful course content but is not yet named by day/session.
- `index.js`, `package.json`, and `.idea/` appear local/project-scaffold files, not course content.
- `photo_rescue_notes.md` and related PowerShell scripts are utilities, not core course materials.

## 00_course_map

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `00_course_map/course_overview.md` | `00_course_map/course_overview.md` | Already in correct course-map folder. | source file | Safe to leave in place |
| `00_course_map/20_session_scope_sequence.md` | `00_course_map/20_session_scope_sequence.md` | Already in correct course-map folder. | source file | Safe to leave in place |

## 01_session_plans

No current files are complete session plans. Do not move existing readings, menus, prompts, or teacher guides here until full session-plan files are created.

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| None currently identified | `01_session_plans/` | Existing files are content components rather than complete timed session plans. | source file | Manual review first |

## 02_student_materials/readings

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `day1_session1_borrowed_equipment_expectations.md` | `02_student_materials/readings/day1_session1_borrowed_equipment_expectations.md` | Student background/norms reading for safety, borrowed equipment, and community trust. | source file | Safe to move automatically |
| `99_archive_or_local/day1_session1_first_ftc_handouts.md` | `99_archive_or_local/day1_session1_first_ftc_handouts.md` | Archived combined FIRST/FTC duplicate. Modular readings are the source of truth. | archive candidate | Completed |
| `day1_session1_robotics_safety_norms.md` | `02_student_materials/readings/day1_session1_robotics_safety_norms.md` | Student safety norms handout. | source file | Safe to move automatically |
| `02_student_materials/readings/day1_session1_what_is_first.md` | `02_student_materials/readings/day1_session1_what_is_first.md` | Modular FIRST background reading. | source file | Completed |
| `02_student_materials/readings/day1_session1_what_is_first_tech_challenge.md` | `02_student_materials/readings/day1_session1_what_is_first_tech_challenge.md` | Modular FTC background reading. | source file | Completed |
| `day1_session2_collaborative_engineering_teams.md` | `02_student_materials/readings/day1_session2_collaborative_engineering_teams.md` | Student background reading for team formation and engineering roles. | source file | Safe to move automatically |
| `day2_session3_why_team_names_matter.md` | `02_student_materials/readings/day2_session3_why_team_names_matter.md` | Student background reading for team identity/name decision. | source file | Safe to move automatically |
| `day2_session4_chassis_physics_space_background.md` | `02_student_materials/readings/day3_session5_chassis_physics_space_background.md` | Student background reading for chassis physics and space planning, now aligned to Day 3 Session 5 build planning. | source file | Safe to move automatically |
| `day2_session4_decode_scoring_strategy_background.md` | `02_student_materials/readings/day2_session4_decode_scoring_strategy_background.md` | Student background reading for DECODE scoring and strategy. | source file | Safe to move automatically |
| `02_student_materials/readings/future_human_controller_mapping_background.md` | `02_student_materials/readings/future_human_controller_mapping_background.md` | Student background reading for later robot-control/controller-mapping session. | source file | Completed |

## 02_student_materials/decision_menus

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `day1_session1_individual_goal_menu.md` | `02_student_materials/decision_menus/day1_session1_individual_goal_menu.md` | Student goal menu with Must/Should/Could and reflection structure. | source file | Safe to move automatically |
| `day2_session3_team_name_menu.md` | `02_student_materials/decision_menus/day2_session3_team_name_menu.md` | Student team-name decision menu. | source file | Safe to move automatically |
| `day2_session3_team_norms_menu.md` | `02_student_materials/decision_menus/day2_session3_team_norms_menu.md` | Student team-norms decision menu and agreement material. | source file | Safe to move automatically |
| `day2_session4_chassis_material_menu.md` | `02_student_materials/decision_menus/day2_session4_chassis_material_menu.md` | Student chassis-material decision menu. | source file | Safe to move automatically |
| `day2_session4_chassis_shape_menu.md` | `02_student_materials/decision_menus/day2_session4_chassis_shape_menu.md` | Student chassis-shape decision menu. | source file | Safe to move automatically |
| `day2_session4_electronics_battery_placement_menu.md` | `02_student_materials/decision_menus/day2_session4_electronics_battery_placement_menu.md` | Student electronics/battery layout decision menu. | source file | Safe to move automatically |
| `day2_session4_game_strategy_goals_menu.md` | `02_student_materials/decision_menus/day2_session4_game_strategy_goals_menu.md` | Student game-strategy decision menu. | source file | Safe to move automatically |
| `day2_session4_motor_placement_menu.md` | `02_student_materials/decision_menus/day2_session4_motor_placement_menu.md` | Student motor-placement decision menu. | source file | Safe to move automatically |
| `day2_session4_wheel_selection_menu.md` | `02_student_materials/decision_menus/day2_session4_wheel_selection_menu.md` | Student wheel-selection decision menu. | source file | Safe to move automatically |

## 02_student_materials/sld_prompts

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `day1_session1_sld_shared_materials_student.md` | `02_student_materials/sld_prompts/day1_session1_sld_shared_materials_student.md` | Student-facing SLD prompt for shared materials, borrowed equipment, and trust. | source file | Safe to move automatically |

## 02_student_materials/engineering_notebook

No current file is a consolidated engineering notebook. Several decision menus contain notebook/portfolio deliverables, but they should remain with decision menus until notebook extraction is intentionally designed.

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `02_student_materials/engineering_notebook/day1_session1_student_bio_template.md` | `02_student_materials/engineering_notebook/day1_session1_student_bio_template.md` | Student bio/team-formation template stored with engineering notebook materials. | source file | Completed |

## 03_teacher_materials/teacher_guides

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `day1_session1_sld_shared_materials_teacher_guide.md` | `03_teacher_materials/teacher_guides/day1_session1_sld_shared_materials_teacher_guide.md` | Teacher/mentor guide for SLD 1. | source file | Safe to move automatically |

## 03_teacher_materials/rubrics

No rubric files currently found.

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| None currently identified | `03_teacher_materials/rubrics/` | Future home for presentation, robot performance, notebook, and teamwork rubrics. | source file | Manual review first |

## 03_teacher_materials/setup_cleanup

No dedicated setup/cleanup files currently found. Safety and borrowed equipment materials may inform future setup/cleanup documents, but should not be moved here yet.

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| None currently identified | `03_teacher_materials/setup_cleanup/` | Future home for setup, cleanup, safety, checkout, and materials-management guides. | source file | Manual review first |

## 04_research_and_design_rationale

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `research_brief_design_menu_cards.md` | `04_research_and_design_rationale/research_brief_design_menu_cards.md` | Design rationale for menu cards and decision tables. | source file | Safe to move automatically |
| `research_brief_student_led_discussions.md` | `04_research_and_design_rationale/research_brief_student_led_discussions.md` | Design rationale for student-led discussions. | source file | Safe to move automatically |

## 05_print_packets

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `05_print_packets/background_documents_print_packet.pdf` | `05_print_packets/background_documents_print_packet.pdf` | Generated early-course print packet. Needs source manifest. | generated export | Completed |
| `05_print_packets/chassis_menus_shape_material_motor_wheel_packet.pdf` | `05_print_packets/chassis_menus_shape_material_motor_wheel_packet.pdf` | Generated chassis menu packet. Needs source manifest. | generated export | Completed |
| `05_print_packets/day2_session4_chassis_design_discussion_packet.pdf` | `05_print_packets/day2_session4_chassis_design_discussion_packet.pdf` | Generated Day 2 Session 4 discussion/design packet. Needs source manifest. | generated export | Completed |
| `day2_session4_chassis_material_menu.pdf` | `05_print_packets/day2_session4_chassis_material_menu.pdf` | PDF export of matching Markdown source. | generated export | Safe to move automatically |
| `day2_session4_chassis_physics_space_background.pdf` | `05_print_packets/day3_session5_chassis_physics_space_background.pdf` | PDF export of matching Markdown source, now aligned to Day 3 Session 5 build planning. | generated export | Safe to move automatically |
| `day2_session4_chassis_shape_menu.pdf` | `05_print_packets/day2_session4_chassis_shape_menu.pdf` | PDF export of matching Markdown source. | generated export | Safe to move automatically |
| `day2_session4_decode_scoring_strategy_background.pdf` | `05_print_packets/day2_session4_decode_scoring_strategy_background.pdf` | PDF export of matching Markdown source. | generated export | Safe to move automatically |
| `day2_session4_electronics_battery_placement_menu.pdf` | `05_print_packets/day2_session4_electronics_battery_placement_menu.pdf` | PDF export of matching Markdown source. | generated export | Safe to move automatically |
| `day2_session4_game_strategy_goals_menu.pdf` | `05_print_packets/day2_session4_game_strategy_goals_menu.pdf` | PDF export of matching Markdown source. | generated export | Safe to move automatically |
| `day2_session4_motor_placement_menu.pdf` | `05_print_packets/day2_session4_motor_placement_menu.pdf` | PDF export of matching Markdown source. | generated export | Safe to move automatically |
| `day2_session4_wheel_selection_menu.pdf` | `05_print_packets/day2_session4_wheel_selection_menu.pdf` | PDF export of matching Markdown source. | generated export | Safe to move automatically |
| `future_human_controller_mapping_background.pdf` | `05_print_packets/future_human_controller_mapping_background.pdf` | PDF export of matching Markdown source. | generated export | Safe to move automatically |

## 90_templates

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `menu_prompt_template.md` | `90_templates/menu_prompt_template.md` | Template for future design menus and decision records. | source file | Safe to move automatically |
| `research_brief_template.md` | `90_templates/research_brief_template.md` | Template for future research briefs. | source file | Safe to move automatically |
| `sld_prompt_template.md` | `90_templates/sld_prompt_template.md` | Template for student-facing SLD prompts and teacher/mentor SLD guides. | source file | Safe to move automatically |

## 91_utilities

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `photo_rescue_notes.md` | `91_utilities/photo_rescue_notes.md` | Notes for photo/video rescue workflow; not core course content. | utility | Safe to move automatically |
| `run_ipad_frame_export.ps1` | `91_utilities/run_ipad_frame_export.ps1` | Wrapper script for iPad frame export workflow. | utility | Safe to move automatically |
| `video_frame_exporter.ps1` | `91_utilities/video_frame_exporter.ps1` | PowerShell utility for exporting video frames. | utility | Safe to move automatically |

## 99_archive_or_local

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `.idea/.gitignore` | `99_archive_or_local/.idea/.gitignore` | Local IDE configuration, not course content. | archive candidate | Manual review first |
| `.idea/FTC_TwoWeekCourse.iml` | `99_archive_or_local/.idea/FTC_TwoWeekCourse.iml` | Local IDE module file, not course content. | archive candidate | Manual review first |
| `.idea/modules.xml` | `99_archive_or_local/.idea/modules.xml` | Local IDE configuration, not course content. | archive candidate | Manual review first |
| `.idea/workspace.xml` | `99_archive_or_local/.idea/workspace.xml` | Local IDE workspace state, not course content. | archive candidate | Manual review first |
| `index.js` | `99_archive_or_local/index.js` | Placeholder JavaScript file, not course content. | archive candidate | Manual review first |
| `package.json` | `99_archive_or_local/package.json` | Placeholder package metadata with no course build/export workflow yet. | archive candidate | Manual review first |

## Docs Folder

The `docs` folder should keep repository-management documentation rather than student-facing or teacher-facing course content.

| Current path | Proposed new path | Reason for move | File category | Move safety |
|---|---|---|---|---|
| `docs/course_content_inventory.md` | `docs/course_content_inventory.md` | Already in appropriate repository documentation folder. | source file | Safe to leave in place |
| `docs/source_file_policy.md` | `docs/source_file_policy.md` | Already in appropriate repository documentation folder. | source file | Safe to leave in place |
| `docs/proposed_file_move_plan.md` | `docs/proposed_file_move_plan.md` | This proposed move plan. | source file | Safe to leave in place |

## Suggested Manual Review Before Moving

Before any move script or bulk reorganization, review these decisions:

1. Create manifests for `05_print_packets/background_documents_print_packet.pdf`, `05_print_packets/chassis_menus_shape_material_motor_wheel_packet.pdf`, and `05_print_packets/day2_session4_chassis_design_discussion_packet.pdf`.
2. Decide whether `02_student_materials/readings/future_human_controller_mapping_background.md` should be renamed later to a specific day/session once the programming/control sequence is finalized.
3. Decide whether `.idea/`, `index.js`, and `package.json` should be archived, ignored, or kept if a future build/export workflow will use them.
