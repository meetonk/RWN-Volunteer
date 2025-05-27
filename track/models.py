from django.db import models
from django.contrib.auth.models import User




class ApplicationStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # null for default statuses
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, verbose_name="Name")
    position = models.CharField(max_length=100)
    # location = models.CharField(max_length=100, blank=True)
    application_date = models.DateField(auto_now_add=True)
    # status = models.ForeignKey(ApplicationStatus, on_delete=models.SET_NULL, null=True)
    # job_link = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.company} - {self.position}"
        # return f"{self.company} - {self.position} ({self.status})"

    @property
    def latest_status_update(self):
        return self.status_updates.order_by('-date').first()


class ApplicationStatusUpdate(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='status_updates')
    status = models.ForeignKey(ApplicationStatus, on_delete=models.PROTECT)
    date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.display_status()} on {self.date}"

    def display_status(self):
        """Return status with numbering if it's a Session or Driving."""
        name = self.status.name.lower()
        if name in ["session", "driving"]:
            # Get all status updates for this job with this status name
            relevant_updates = [
                update for update in self.job_application.status_updates.all()
                if update.status.name.lower() == name
            ]
            index = relevant_updates.index(self) + 1 if self in relevant_updates else 1
            # Capitalize the status name for display
            display_name = self.status.name.capitalize()
            return f"{display_name} #{index}"
        return self.status.name


