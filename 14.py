class User:
    def interact(self):
        pass


class Applicant(User):
    def interact(self):
        return self.apply_to_job()

    def apply_to_job(self):
        return "You have successfully applied to the job."


class Employer(User):
    def interact(self):
        return self.post_job()

    def post_job(self):
        return "You have successfully posted a new job."


applicant = Applicant()
employer = Employer()

print("Applicant:", applicant.interact())
print("Employer:", employer.interact())
