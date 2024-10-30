from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from Pages.forms import CommentForm, ContactForm
from Pages.models import Case, Client, Comment, ContactMessage, Post, Service, TeamMember

# Hard-coded approach: adding `services` to each view
def indexView(request, *args, **kwargs):
    clients = Client.objects.all()
    team_members = TeamMember.objects.all()
    services = Service.objects.all()
    cases = Case.objects.all()
    posts = Post.objects.all()
    return render(request, 'home-2.html', {
        "clients": clients,
        "team_members": team_members,
        "services": services,
        'cases': cases,
        "posts": posts
    })


def aboutView(request, *args, **kwargs):
    services = Service.objects.all()
    return render(request, 'about.html', {"services": services})


@csrf_exempt
def contactView(request, *args, **kwargs):
    services = Service.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        budget = request.POST.get('budget')
        project_details = request.POST.get('project-details')
        attachment = request.FILES.get('attachment')

        errors = {}
        if not name: errors['name'] = 'This field is required.'
        if not company: errors['company'] = 'This field is required.'
        if not email: errors['email'] = 'This field is required.'
        if not budget: errors['budget'] = 'This field is required.'
        if not project_details: errors['project_details'] = 'This field is required.'

        if errors:
            return JsonResponse({"success": False, "errors": errors}, status=400)

        ContactMessage.objects.create(
            name=name,
            company=company,
            email=email,
            budget=budget,
            project_details=project_details,
            attachment=attachment
        )

        return JsonResponse({"success": True})

    return render(request, 'contact.html', {"services": services})


def serviceView(request, url_title, *args, **kwargs):
    services = Service.objects.all()
    service = Service.objects.get(url_title=url_title)
    return render(request, 'service-single.html', {"service": service, "services": services})


def caseView(request, url_title, *args, **kwargs):
    services = Service.objects.all()
    case = Case.objects.get(url_title=url_title)
    elements = case.requierments.split(', ')
    sub_arrays = [elements[i:i + 3] for i in range(0, len(elements), 3)]
    return render(request, 'case-single.html', {"case": case, "sub_arrays": sub_arrays, "services": services})


def teamView(request, url_title, *args, **kwargs):
    services = Service.objects.all()
    member = TeamMember.objects.get(url_title=url_title)
    return render(request, 'team-single.html', {"member": member, "services": services})


def teamMembersView(request, *args, **kwargs):
    services = Service.objects.all()
    members = TeamMember.objects.all()
    return render(request, 'team.html', {"team_members": members, "services": services})


def blogPostView(request, url_title, *args, **kwargs):
    services = Service.objects.all()
    post = get_object_or_404(Post, url_title=url_title)
    comments = post.comments.all()
    posts = Post.objects.all()[:3]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        errors = {}

        if not name: errors['name'] = 'Name is required.'
        if not email: errors['email'] = 'Email is required.'
        if not content: errors['content'] = 'Comment content is required.'

        if errors:
            return JsonResponse({"success": False, "errors": errors}, status=400)

        Comment.objects.create(post=post, name=name, email=email, content=content)
        return redirect(request.path_info)

    return render(request, 'blog-single.html', {
        'post': post,
        'comments': comments,
        'posts': posts,
        'services': services
    })


def blogView(request, *args, **kwargs):
    services = Service.objects.all()
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts, "services": services})


def casesView(request, *args, **kwargs):
    services = Service.objects.all()
    clients = Client.objects.all()
    cases = Case.objects.all()
    return render(request, "case.html", {"cases": cases, "clients": clients, "services": services})


def privacyView(request, *args, **kwargs):
    services = Service.objects.all()
    return render(request, "privacy.html", {"services": services})


def termsView(request, *args, **kwargs):
    services = Service.objects.all()
    return render(request, "terms.html", {"services": services})


def servicesView(request, *args, **kwargs):
    services = Service.objects.all()
    cases = Case.objects.all()
    clients = Client.objects.all()
    return render(request, "services.html", {
        'services': services,
        'cases': cases,
        'clients': clients,
    })
