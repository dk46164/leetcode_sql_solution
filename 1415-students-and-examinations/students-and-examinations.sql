with cte_base as (
    select 
        student_id,
        student_name,
        subject_name
    from 
        Students s1 cross join Subjects s2

)

select 
distinct
    b.student_id,
    b.student_name,
    b.subject_name,
    count(e.subject_name) over( partition by b.student_id,b.student_name,b.subject_name) as attended_exams
from  
    cte_base b 
    left join  Examinations e on e.student_id = b.student_id and e.subject_name = b.subject_name
;