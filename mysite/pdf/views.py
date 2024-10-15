from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.http import HttpResponse
import pdfkit
from django.template import loader
from django.shortcuts import redirect
import io
# Create your views here.


def cv(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        summary = request.POST.get('summary', "")
        degree = request.POST.get('degree', "")
        school = request.POST.get('school', "")
        university = request.POST.get('university', "")
        prev_work = request.POST.get('prev_work', "")
        skills = request.POST.get('skills', "")

        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            prev_work=prev_work,
            skills=skills
        )
        profile.save()
        return redirect(f"/resume/{profile.id}")  # Redirect to the specific resume
    return render(request, 'main.html')


def submission(request):

    return redirect(f"/resume/{profile.id}")  # Redirect to the specific resume


def resume(request, id):
    profile = Profile.objects.get(pk=id)

    # Split the skills string into a list and trim whitespace
    skills_list = [skill.strip() for skill in profile.skills.split(',')]

    return render(request, 'resume.html', {'profile': profile, 'skills_list': skills_list})


def resume_pdf(request, id):
    profile = Profile.objects.get(pk=id)
    skills_list = [skill.strip() for skill in profile.skills.split(',')]
    template = loader.get_template('resume_pdf.html')
    html = template.render({'profile': profile, 'skills_list': skills_list})

    # Set options for PDF generation
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'no-outline': None,  # Don't include outlines (bookmarks)
        'disable-smart-shrinking': None,  # Prevent shrinking content
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
    }

    # Create PDF from HTML
    pdf = pdfkit.from_string(html, False, options)

    # Prepare the response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{profile.name}_resume.pdf"'  # Correctly set the filename
    return response


def home(request):
    return render(request, 'home.html')


def cvs(request):
    profiles = Profile.objects.all()

    return render(request, 'cvs.html', {'profiles': profiles})