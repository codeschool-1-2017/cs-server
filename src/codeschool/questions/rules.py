import rules

from codeschool.lms.activities.rules import is_activity_editor

rules.add_perm('questions.edit_question', is_activity_editor)
