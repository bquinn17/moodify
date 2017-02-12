from django.db import models


class SpotifyUser(models.Model):
    access_token = models.CharField(max_length=50, default='')
    expires_at = models.DateTimeField()
    refresh_token = models.CharField(max_length=50, default='')

    def __str__(self):
        return "User: " + str(self.access_token)

    def __repr__(self):
        return self.__str__()
