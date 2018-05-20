import vk
import settings
import requests


def upload_photo_to_album(path_of_file):

    session = vk.AuthSession(access_token=settings.user_access_token)
    vk_api = vk.API(session, v=settings.vk_api_version)

    upload_url = vk_api.photos.getUploadServer(group_id=settings.group_for_photos_id,
                                               album_id=settings.album_id)['upload_url']

    request = requests.post(upload_url,
                            files={'photo': open(path_of_file, "rb")})

    photo = vk_api.photos.save(album_id='255140841',
                               group_id=settings.group_for_photos_id,
                               server=request.json()['server'],
                               photos_list=request.json()['photos_list'],
                               hash=request.json()['hash'])[0]
    photo_id = photo['id']

    photo_parameters = 'photo-' + settings.group_for_photos_id + '_' + str(photo_id)
    return photo_parameters
