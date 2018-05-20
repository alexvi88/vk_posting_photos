import os
import vk
import settings
import time
from posting_photo_with_delay import post_photo_with_delay
from uploading_photo_to_album import upload_photo_to_album
from deleting_photos import delete_photo

all_photos = [file_name
              for file_name in os.listdir(settings.directory_with_photos)
              if os.path.splitext(file_name)[1] in settings.photo_formats]

cur_delay = 0

for photo_name in all_photos:
    photo_path = settings.directory_with_photos + '/' + photo_name
    photo_parameters = upload_photo_to_album(photo_path)

    try:
        post_photo_with_delay(photo_parameters, cur_delay)
        if settings.delete_photos_after_posting:
            delete_photo(photo_path)
    except Exception as e:
        print(e)

    cur_delay += settings.posts_interval
    time.sleep(settings.requests_interval)
