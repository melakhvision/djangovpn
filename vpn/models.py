from django.db import models

# Create your models here.
# create profile class for openvpn .ovpn file. ovpn file is not uploaded but created from lunix command line


class Profile(models.Model):
    STATUS_ACTIVE = 'A'
    STATUS_REVOKED = 'R'
    PROFILE_STATUS = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_REVOKED, 'Revoked'),
    ]

    name = models.CharField(max_length=50)
    ovpn = models.CharField(max_length=50)
    status = models.CharField(
        max_length=8, choices=PROFILE_STATUS, default=STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def ovpn(self):
        return self.name + '.ovpn'

    class Meta:
        ordering = ['created_at']
