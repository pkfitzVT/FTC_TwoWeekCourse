# Reorganization Log

## Summary

This pass implemented only the approved safe parts of `docs/proposed_file_move_plan.md`.

No files marked `Manual review first` were moved. The `.idea` directory, `package.json`, `index.js`, `future_human_controller_mapping_background.md`, and Day 1 Session 1 duplicate/overlapping source files were intentionally left in place.

## Files Moved

### Student Readings

- `day1_session1_borrowed_equipment_expectations.md` -> `02_student_materials/readings/day1_session1_borrowed_equipment_expectations.md`
- `day1_session1_robotics_safety_norms.md` -> `02_student_materials/readings/day1_session1_robotics_safety_norms.md`
- `day1_session2_collaborative_engineering_teams.md` -> `02_student_materials/readings/day1_session2_collaborative_engineering_teams.md`
- `day2_session3_why_team_names_matter.md` -> `02_student_materials/readings/day2_session3_why_team_names_matter.md`
- `day2_session4_chassis_physics_space_background.md` -> `02_student_materials/readings/day3_session5_chassis_physics_space_background.md`
- `day2_session4_decode_scoring_strategy_background.md` -> `02_student_materials/readings/day2_session4_decode_scoring_strategy_background.md`

### Student Decision Menus

- `day1_session1_individual_goal_menu.md` -> `02_student_materials/decision_menus/day1_session1_individual_goal_menu.md`
- `day2_session3_team_name_menu.md` -> `02_student_materials/decision_menus/day2_session3_team_name_menu.md`
- `day2_session3_team_norms_menu.md` -> `02_student_materials/decision_menus/day2_session3_team_norms_menu.md`
- `day2_session4_chassis_material_menu.md` -> `02_student_materials/decision_menus/day2_session4_chassis_material_menu.md`
- `day2_session4_chassis_shape_menu.md` -> `02_student_materials/decision_menus/day2_session4_chassis_shape_menu.md`
- `day2_session4_electronics_battery_placement_menu.md` -> `02_student_materials/decision_menus/day2_session4_electronics_battery_placement_menu.md`
- `day2_session4_game_strategy_goals_menu.md` -> `02_student_materials/decision_menus/day2_session4_game_strategy_goals_menu.md`
- `day2_session4_motor_placement_menu.md` -> `02_student_materials/decision_menus/day2_session4_motor_placement_menu.md`
- `day2_session4_wheel_selection_menu.md` -> `02_student_materials/decision_menus/day2_session4_wheel_selection_menu.md`

### Student SLD Prompts

- `day1_session1_sld_shared_materials_student.md` -> `02_student_materials/sld_prompts/day1_session1_sld_shared_materials_student.md`

### Teacher Guides

- `day1_session1_sld_shared_materials_teacher_guide.md` -> `03_teacher_materials/teacher_guides/day1_session1_sld_shared_materials_teacher_guide.md`

### Research and Design Rationale

- `research_brief_design_menu_cards.md` -> `04_research_and_design_rationale/research_brief_design_menu_cards.md`
- `research_brief_student_led_discussions.md` -> `04_research_and_design_rationale/research_brief_student_led_discussions.md`

### Generated PDF Exports

- `day2_session4_chassis_material_menu.pdf` -> `05_print_packets/day2_session4_chassis_material_menu.pdf`
- `day2_session4_chassis_physics_space_background.pdf` -> `05_print_packets/day3_session5_chassis_physics_space_background.pdf`
- `day2_session4_chassis_shape_menu.pdf` -> `05_print_packets/day2_session4_chassis_shape_menu.pdf`
- `day2_session4_decode_scoring_strategy_background.pdf` -> `05_print_packets/day2_session4_decode_scoring_strategy_background.pdf`
- `day2_session4_electronics_battery_placement_menu.pdf` -> `05_print_packets/day2_session4_electronics_battery_placement_menu.pdf`
- `day2_session4_game_strategy_goals_menu.pdf` -> `05_print_packets/day2_session4_game_strategy_goals_menu.pdf`
- `day2_session4_motor_placement_menu.pdf` -> `05_print_packets/day2_session4_motor_placement_menu.pdf`
- `day2_session4_wheel_selection_menu.pdf` -> `05_print_packets/day2_session4_wheel_selection_menu.pdf`
- `future_human_controller_mapping_background.pdf` -> `05_print_packets/future_human_controller_mapping_background.pdf`

### Templates

- `menu_prompt_template.md` -> `90_templates/menu_prompt_template.md`
- `research_brief_template.md` -> `90_templates/research_brief_template.md`
- `sld_prompt_template.md` -> `90_templates/sld_prompt_template.md`

### Utilities

- `photo_rescue_notes.md` -> `91_utilities/photo_rescue_notes.md`
- `run_ipad_frame_export.ps1` -> `91_utilities/run_ipad_frame_export.ps1`
- `video_frame_exporter.ps1` -> `91_utilities/video_frame_exporter.ps1`

## Files Intentionally Not Moved

- `.idea/` and all `.idea` files
- `package.json`
- `index.js`
- `future_human_controller_mapping_background.md`
- `day1_session1_first_ftc_handouts.md`
- `day1_session1_what_is_first.md`
- `day1_session1_what_is_first_tech_challenge.md`
- `day1_session1_student_bio_template.md`
- `background_documents_print_packet.pdf`
- `chassis_menus_shape_material_motor_wheel_packet.pdf`
- `day2_session4_chassis_design_discussion_packet.pdf`

## Manual Review Items Remaining

1. Decide whether `day1_session1_first_ftc_handouts.md` or the two modular readings should be the Day 1 Session 1 source of truth.
2. Decide where `day1_session1_student_bio_template.md` belongs: engineering notebook, workbook packet, or team-formation materials.
3. Create source manifests for packet PDFs:
   - `background_documents_print_packet.pdf`
   - `chassis_menus_shape_material_motor_wheel_packet.pdf`
   - `day2_session4_chassis_design_discussion_packet.pdf`
4. Decide the final session/path assignment for `future_human_controller_mapping_background.md`.
5. Decide whether `.idea/`, `package.json`, and `index.js` should remain, be ignored, or be archived later.

## Other Changes

- Added root `.gitignore` with the requested ignore rules.
- Created target organizing folders from the proposed move plan.
- Updated `docs/course_content_inventory.md` so file paths match the new folder structure.

## Day 2 / Day 3 Reading Realignment

- Renamed `02_student_materials/readings/day2_session4_chassis_physics_space_background.md` -> `02_student_materials/readings/day3_session5_chassis_physics_space_background.md`.
- Renamed `05_print_packets/day2_session4_chassis_physics_space_background.pdf` -> `05_print_packets/day3_session5_chassis_physics_space_background.pdf`.
- Renamed the Day 2 Session 4 plan shell to `01_session_plans/day02/session_04_first_programming_session.md`.
- Updated the scope sequence, session plans, engineering notebook, inventory, course overview, teacher overview, and coteacher review packet so Day 2 Session 4 focuses on first programming and Day 3 Session 5 carries chassis physics / space constraints.
