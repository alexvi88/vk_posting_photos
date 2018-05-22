import vk
import settings


def last_postponed_post_time():
    session = vk.AuthSession(access_token=settings.user_access_token)
    vk_api = vk.API(session, v=settings.vk_api_version)

    postponed_posts = vk_api.wall.get(owner_id='-' + settings.group_for_posting_id,
                                      filter='postponed')

    if postponed_posts['count'] == 0:
        return 0
    else:
        last_postponed_post_date = postponed_posts['items'][-1]['date']
        return last_postponed_post_date
