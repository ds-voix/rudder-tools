# Rudder API https://docs.rudder.io/api/v/21/
import json
import urllib, ssl
from urllib.request import urlopen, Request
import time
import sys

from colors import *


def wrap_args(func, *args):
  if len(args) == 0:
    return func()
  elif len(args) == 1:
    return func(*args[0])
  elif len(args) == 2:
    return func(*args[0], *args[1])
  elif len(args) == 3:
    return func(*args[0], *args[1], *args[2])
  else:
    return func(args) # *args must be parsed inside


# Retry N times
def retry(func, *args, RETRY = 3, RETRY_TIMEOUT = 1):
  ok = False
  for i in range(RETRY - 1):
    ok, res = wrap_args(func, args)
    if ok:
      return ok, res
    time.sleep(RETRY_TIMEOUT)
  return wrap_args(func, args)


def rudder_response(js):
  if "result" in js:
    if js["result"] == "success":
      return True, js
    else:
      return False, js
  else:
    print(f'{cr}rudder_response:{c_}', "No \"result\" field in JSON:", file=sys.stderr)
    print("%s" % json.dumps(js, indent=1), file=sys.stderr)
    return False, js


class JSON_API:
  def __init__(self, SRC = '', DST = '', HTTP_TIMEOUT = 5):
    self.SRC = SRC
    self.DST = DST
    self.HTTP_TIMEOUT = HTTP_TIMEOUT


  def HTTP(self, req, func):
    context = ssl._create_unverified_context()
    try:
      response = urlopen(req, context=context, timeout=self.HTTP_TIMEOUT)
      result = response.read()
      try:
        js = json.loads(result.decode("utf-8"))
        return rudder_response(js)
      except:
        print(f'{cr}HTTP({func}):{c_}', f"{cr}Non-JSON API reply:{c_}", file=sys.stderr)
        print("%s" % result, file=sys.stderr)
        return False, None

    except urllib.error.HTTPError as e:
      body = e.read()
      print(f'{cr}HTTP({func}):{c_}', req.get_full_url(), file=sys.stderr)
      print(f'{cr}HTTP({func}):{c_}',req.get_method(), file=sys.stderr)
      print(f'{cr}HTTP({func}):{c_}', 'HTTPError = ' + str(e.code) + "\n" + str(e.hdrs) + "\n" + str(body), file=sys.stderr)
      return False, None
    except urllib.error.URLError as e:
      print(f'{cr}HTTP({func}):{c_}', 'URLError = ' + str(e.reason), file=sys.stderr)
      return False, None
    except Exception:
      import traceback
      print(f'{cr}HTTP({func}):{c_}', 'Generic exception: ' + traceback.format_exc(), file=sys.stderr)
      return False, None

    return False, None


  def get_json(self, path, rudder = None): # GET
    if not rudder:
      rudder = self.SRC
    req = Request("%s%s" % (rudder, path))
    return self.HTTP(req, 'GET')


  def put_json(self, path, js, method='PUT', rudder = None): # PUT/POST
    if not rudder:
      rudder = self.DST
    js = json.dumps(js, indent=1)
    req = Request("%s%s" % (rudder, path), data=js.encode('utf-8'), headers={'Content-Type':'application/json; charset=utf-8'}, method=method)
    return self.HTTP(req, f'{method}')


  def delete(self, path, rudder = None): # DELETE
    if not rudder:
      rudder = self.DST
    req = Request("%s%s" % (rudder, path), method='DELETE')
    return self.HTTP(req, 'DELETE')
