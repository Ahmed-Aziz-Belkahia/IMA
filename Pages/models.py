from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=50)
    url_title = models.SlugField()
    big_image = models.ImageField(upload_to='images/')
    small_image = models.ImageField(upload_to='images/')
    text = models.TextField(blank=True)
    approach = models.TextField()
    what_we_offer = models.TextField()
    tags = models.CharField(max_length=255)
    mini_image_text = models.TextField()
    process_text = models.TextField()
    
class Process(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True, related_name="processes")
    number = models.IntegerField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    
class CaseCategory(models.Model):
    title = models.CharField(max_length=100)

class Client(models.Model):
    name=models.CharField(max_length=100)
    logo = models.ImageField(upload_to='image/', blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    description = models.TextField(blank=True)
    testimonial = models.TextField(blank=True)
    bussiness_name = models.CharField(blank=True, max_length=100)
    bussiness_role = models.CharField(blank=True, max_length=100)

class Case(models.Model):
    url_title = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(CaseCategory, on_delete=models.CASCADE, related_name="cases")
    big_image = models.ImageField(upload_to='image/')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="cases")
    timeframe = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    approach = models.TextField()
    solution = models.TextField()
    left_big_image = models.ImageField(upload_to='image/')
    left_small_image1 = models.ImageField(upload_to='image/')
    left_small_image2 = models.ImageField(upload_to='image/')
    requierments = models.TextField(null=True)
    challenge = models.TextField()
    result = models.TextField()
    small_overview = models.TextField(default="small_overview")
    
class TeamMember(models.Model):
    url_title = models.SlugField(blank=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')
    role = models.CharField(max_length=50)
    twitter = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, default="+216 22 222 222")
    email = models.EmailField(max_length=254, default="ahmadazizbelkahia@gmail.com")
    experience = models.IntegerField(default=5)
    bio = models.TextField(default="test")
    skills_bio = models.TextField(default="test")
    
class Skill(models.Model):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="skills")
    image = models.ImageField(upload_to="image/")
    name = models.CharField(max_length=50)
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    budget = models.CharField(max_length=20)  # Adjust the length as needed
    project_details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} ({self.company})'

class Post(models.Model):
    url_title = models.SlugField()
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=100)
    op = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="posts")
    date = models.CharField(max_length=50)
    read_time = models.CharField(max_length=50)
    mini_description = models.TextField()
    tags = models.CharField(max_length=50)
    quote = models.TextField()
    quote_image = models.ImageField(upload_to='image/')
    quote_name = models.CharField(max_length=50)
    quote_role = models.CharField(max_length=50)

    def get_blocks(self):
        return self.blocks.order_by("index")

class Block(models.Model):
    index = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="blocks")
    title = models.CharField(max_length=100)
    content = models.TextField()

class blogImage(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="image/")
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"