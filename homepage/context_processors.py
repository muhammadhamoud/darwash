from .models import SiteInformation

def site_information(request):
    # Retrieve the SiteInformation object (adjust the logic as needed)
    try:
        site_info = SiteInformation.objects.get(pk=1)
    except SiteInformation.DoesNotExist:
        site_info = None

    return {'site_information': site_info}
