% Facts
disease(diabetes, low_carb_diet).
disease(hypertension, low_salt_diet).
disease(heart_disease, low_fat_diet).
disease(gout, low_purine_diet).
disease(obesity, balanced_diet).
% Rule to suggest diet based on disease
suggest_diet(Disease, Diet) :-
    disease(Disease, Diet).
