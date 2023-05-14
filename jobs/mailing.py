def send_job_created_mail(job_id):
    print(f"JOB {job_id} CREATED")


def send_job_updated_mail(job_id, old_title_rich_text, new_title_rich_text):
    print(f"JOB {job_id} UPDATED")
    print("OLD JOD TITLE: {}".format(old_title_rich_text))
    print("NEW JOB TITLE: {}".format(new_title_rich_text))