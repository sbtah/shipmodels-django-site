from django.db import models


# Model of Banner object and it's methods.
class Banner(models.Model):
    """Class for Banner object."""

    pass


# Model of BannerImage object and it's methods.
class BannerImage(models.Model):
    """Class for BannerImage object."""

    tytuł = models.CharField(max_length=50)

    pass
