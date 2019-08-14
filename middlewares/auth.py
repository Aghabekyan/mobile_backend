from users.models import User
from rest_framework import authentication
from rest_framework import exceptions
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if (not len(firebase_admin._apps)):
            cred = credentials.Certificate("./key.json")
            firebase_admin.initialize_app(cred)
        # user = auth.get_user('DCET87AVove5lLCpLONpB3N39DS2')
        # token="deyJhbGciOiJSUzI1NiIsImtpZCI6IjY0MWU3OWQzZjUwOWUyYzdhNjQ1N2ZjOTVmY2U1MGNjOGM3M2VmMDMiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiSm9obiBEb2UiLCJwaWN0dXJlIjoiaHR0cDovL3d3dy5leGFtcGxlLmNvbS8xMjM0NTY3OC9waG90by5wbmciLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbW9iaWxlLXRlc3QtMzdiNTYiLCJhdWQiOiJtb2JpbGUtdGVzdC0zN2I1NiIsImF1dGhfdGltZSI6MTU2NTU5NzMwMiwidXNlcl9pZCI6IkZjQW9OMFRQOXlaN1VtaVBldDNmeVRyNzNucTEiLCJzdWIiOiJGY0FvTjBUUDl5WjdVbWlQZXQzZnlUcjczbnExIiwiaWF0IjoxNTY1NTk3MzAyLCJleHAiOjE1NjU2MDA5MDIsImVtYWlsIjoicy5hZ2hhYmVreWFuQHlhbmRleC5ydSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaG9uZV9udW1iZXIiOiIrMTU1NTU1NTAxMDAiLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7InBob25lIjpbIisxNTU1NTU1MDEwMCJdLCJlbWFpbCI6WyJzLmFnaGFiZWt5YW5AeWFuZGV4LnJ1Il19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.TfsVOsBswcczNbfMKn9BSTzyMdOVe79zQyAXrgo3xLCXeE4fVLpRNwEEF__Dbl0UkT4xbbOAT6vsDQngMBkK-nkqfG9-nB292j5VxFddIDOfstXXNHYMNrhJzcBWATVtEkF3OYqZCWAvzphcMXxY0ZlYJBFj3OlnSifmhF3fifpkFvXEBmbKC7VtfaKxRlKKI_s6dUcW5bq7PhFfDNd-jZWZL7yXCo4DPoniPcu6FDgX3Qxbku4AO_w3zeGYUUD2zNL39jkFRznBqPSVOGXqeNgYCNaJlKfR-yngqIEdVCxp-j7722czT1skSZw1oPvU0wsLfkRyF3xjau5Blj-1wA"
        # decoded_token = auth.verify_id_token(token)
        try:
            token = request.headers['Authorization'].split(' ')[-1]
            # token="deyJhbGciOiJSUzI1NiIsImtpZCI6IjY0MWU3OWQzZjUwOWUyYzdhNjQ1N2ZjOTVmY2U1MGNjOGM3M2VmMDMiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiSm9obiBEb2UiLCJwaWN0dXJlIjoiaHR0cDovL3d3dy5leGFtcGxlLmNvbS8xMjM0NTY3OC9waG90by5wbmciLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbW9iaWxlLXRlc3QtMzdiNTYiLCJhdWQiOiJtb2JpbGUtdGVzdC0zN2I1NiIsImF1dGhfdGltZSI6MTU2NTU5NzMwMiwidXNlcl9pZCI6IkZjQW9OMFRQOXlaN1VtaVBldDNmeVRyNzNucTEiLCJzdWIiOiJGY0FvTjBUUDl5WjdVbWlQZXQzZnlUcjczbnExIiwiaWF0IjoxNTY1NTk3MzAyLCJleHAiOjE1NjU2MDA5MDIsImVtYWlsIjoicy5hZ2hhYmVreWFuQHlhbmRleC5ydSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaG9uZV9udW1iZXIiOiIrMTU1NTU1NTAxMDAiLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7InBob25lIjpbIisxNTU1NTU1MDEwMCJdLCJlbWFpbCI6WyJzLmFnaGFiZWt5YW5AeWFuZGV4LnJ1Il19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.TfsVOsBswcczNbfMKn9BSTzyMdOVe79zQyAXrgo3xLCXeE4fVLpRNwEEF__Dbl0UkT4xbbOAT6vsDQngMBkK-nkqfG9-nB292j5VxFddIDOfstXXNHYMNrhJzcBWATVtEkF3OYqZCWAvzphcMXxY0ZlYJBFj3OlnSifmhF3fifpkFvXEBmbKC7VtfaKxRlKKI_s6dUcW5bq7PhFfDNd-jZWZL7yXCo4DPoniPcu6FDgX3Qxbku4AO_w3zeGYUUD2zNL39jkFRznBqPSVOGXqeNgYCNaJlKfR-yngqIEdVCxp-j7722czT1skSZw1oPvU0wsLfkRyF3xjau5Blj-1wA"
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            user = User.objects.get(pk=7) # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 
        except ValueError as e:
            # import pdb 
            # pdb.set_trace()
            raise exceptions.AuthenticationFailed({"error": str(e)}) # raise exception if user does not exist 
        except:
            raise exceptions.AuthenticationFailed('Unauthorized') # raise exception if user does not exist 

        return (user, None) # authentication successful