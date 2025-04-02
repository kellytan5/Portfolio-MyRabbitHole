from django.db import models

# Create your models here.
class Contact(models.Model):
  #title
  name = models.CharField(max_length = 100) # name
  email = models.EmailField(unique=True) # email
  message = models.TextField(blank = True, null = True) # description 
  created_at = models.DateTimeField(auto_now_add = True) # created_at 

  def __str__ (self): 
    # return the contact name 
    return self.name 

# Projects model
class Project(models.Model):
  title = models.CharField(max_length = 200) # title
  description = models.CharField(max_length = 1000) # description
  conclusion = models.CharField(max_length = 200) # conclusion 
  location = models.CharField(max_length = 100) # location
  start_date = models.CharField(max_length=7)  # Format: YYYY-MM
  end_date = models.CharField(max_length=7)    # Format: YYYY-MM
  position = models.CharField(max_length = 100) # position 
  github = models.URLField(max_length=200, blank=True, null=True) # github URL field
  figma = models.URLField(max_length=200, blank=True, null=True) # figma URL field 

  def __str__(self):
    return self.title

class ProjectImage(models.Model):
  project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
  image = models.ImageField(upload_to="project_images/")
  uploaded_at = models.DateTimeField(auto_now_add=True)

class Education(models.Model):
  start_date = models.CharField(max_length=7)  # Format: YYYY-MM
  end_date = models.CharField(max_length=7)    # Format: YYYY-MM
  title = models.CharField(max_length = 200) # title
  description = models.CharField(max_length = 200) # description
  location = models.CharField(max_length = 100) # location
  image = models.URLField(max_length=200, blank=True, null=True) # image URL field 
  name = models.CharField(max_length = 100) # name
  position = models.CharField(max_length = 100) # position
  link = "Related Projects"
  projects = models.ManyToManyField(Project, related_name="educations")

  def __str__(self):
    return self.title

class Experience(models.Model):
  start_date = models.CharField(max_length=7)  # Format: YYYY-MM
  end_date = models.CharField(max_length=7)    # Format: YYYY-MM
  title = models.CharField(max_length = 250) # title
  company = models.CharField(max_length = 100) # company
  description = models.JSONField(default = list) # description (list format)
  location = models.CharField(max_length = 100) # location
  projects = models.ManyToManyField(Project, related_name="experiences")

  def __str__(self):
    return self.company