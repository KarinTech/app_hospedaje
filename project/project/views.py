from django.views.generic import TemplateView


class LandingPage (TemplateView):
 template_name="landing-page.html"
 extra-content== {"titulo_pagina": "LANDING PAGE"
 }