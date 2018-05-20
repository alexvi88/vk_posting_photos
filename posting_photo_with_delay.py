import settings
import vk
import datetime


def post_photo_with_delay(photo_parameters, delay):

    session = vk.AuthSession(access_token=settings.user_access_token)
    vk_api = vk.API(session, v=settings.vk_api_version)

    now_temp_d = datetime.datetime.now()
    now_date = int(now_temp_d.timestamp())

    time_to_post = (round((now_date + 2 + delay) / 60 + 0.5))*60

    return vk_api.wall.post(owner_id='-' + settings.group_for_posting_id,
                            attachments=photo_parameters,
                            from_group=1,
                            mark_as_ads=0,
                            publish_date=time_to_post)
