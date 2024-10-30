from django.contrib import admin
from Pages.models import (
    Comment, ContactMessage, Service, Process, CaseCategory, Client, Case, Skill, TeamMember,
    Post, Block, blogImage  # Add the new models
)

# Inline for blogImage model
class BlogImageInline(admin.TabularInline):
    model = blogImage
    extra = 1  # Number of empty image forms to display
    fields = ('image',)  # Display only the image field

# Inline for Block model
class BlockInline(admin.TabularInline):
    model = Block
    extra = 1  # Number of empty block forms to display
    fields = ('title', 'content')
    inlines = [BlogImageInline]  # Nest blogImage inline within each Block

# Admin for Post model with BlockInline
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_title', 'op', 'date', 'read_time')  # Customize list display
    search_fields = ('title', 'url_title', 'tags')  # Enable search on title, URL title, and tags
    list_filter = ('op', 'date')  # Filter by author and date
    inlines = [BlockInline]  # Add Block inline to manage Blocks within each Post

# Inline admin for Process model
class ProcessInline(admin.TabularInline):
    model = Process

# Inline admin for Skill model
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1  # Number of empty forms to display

# Admin configuration for Service model
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_title')
    search_fields = ('title', 'tags')
    inlines = [ProcessInline]

# Admin configuration for CaseCategory model
@admin.register(CaseCategory)
class CaseCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Admin configuration for Client model
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Admin configuration for Case model
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'category', 'timeframe')
    search_fields = ('title', 'client__name', 'category__title')
    list_filter = ('category', 'client')

# Admin configuration for TeamMember model
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')  # Customize fields as needed
    search_fields = ('name', 'role')  # Allow searching by name and role
    inlines = [SkillInline]  # Add inline for skills

# Admin configuration for Skill model
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'member')  # Customize fields as needed
    search_fields = ('name', 'member__name') 

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'budget', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'company', 'email')  # Fields to add search functionality
    list_filter = ('created_at',)  # Add filter options for date
    readonly_fields = ('created_at',)  # Make created_at read-only

    # Optionally, you can add fieldsets to organize fields in the detail view
    fieldsets = (
        (None, {
            'fields': ('name', 'company', 'email', 'budget', 'project_details', 'attachment')
        }),
        ('Date Information', {
            'fields': ('created_at',),  # Add it here, but it will be read-only
            'classes': ('collapse',),  # Makes the section collapsible
        }),
    )

# Register the ContactMessage with custom admin
admin.site.register(ContactMessage, ContactMessageAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')
    search_fields = ('name', 'email', 'content')
    
    
class BlogImageInline(admin.TabularInline):  # or use admin.StackedInline for a different style
    model = blogImage
    extra = 1  # Number of extra empty forms displayed; adjust as needed

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]