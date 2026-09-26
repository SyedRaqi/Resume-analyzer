export type User = { id: number; name: string; email: string; created_at: string };
export type Resume = { id: number; filename: string; uploaded_at: string };
export type Analysis = { id: number; resume_id: number; overall_score: number; skills_score: number; education_score: number; projects_score: number; experience_score: number; formatting_score: number; extracted_data: { name?: string; email?: string; phone?: string; skills?: string[]; sections?: Record<string, boolean> }; suggestions: string[]; created_at: string };
export type Match = { id: number; resume_id: number; job_title: string; match_score: number; matching_skills: string[]; missing_skills: string[]; created_at: string };
