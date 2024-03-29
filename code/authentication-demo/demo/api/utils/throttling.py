import random
import time
from rest_framework import throttling

class VisitThrottle(throttling.SimpleRateThrottle):
    scope = "reflact"

    def get_cache_key(self, request, view):
        return self.get_ident(request)



# class RandomRateThrottle(throttling.BaseThrottle):
#     def allow_request(self, request, view):
#         res = self.get_ident(request)
#         print(res)
#         return True


# class CustomThrottle(object):
#
#     def __init__(self):
#         self.history = None
#
#     def allow_request(self, request, view):
#         remote_addr = request.META.get('REMOTE_ADDR')
#         ctime = time.time()
#         if remote_addr not in VISIT_RECORD:
#             VISIT_RECORD[remote_addr] = [ctime, ]
#             return True
#         history = VISIT_RECORD.get(remote_addr)
#         self.history = history
#
#         while history and history[-1] < ctime - 60:
#             history.pop()
#
#         if len(history) < 3:
#             history.insert(0, ctime)
#             return True
#
        # def wait(self):
        #     ctime = time.time()
        #     return 60 - (ctime - self.history[-1])
