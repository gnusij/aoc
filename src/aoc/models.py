import os
import re
import requests
from pathlib import Path
import html

from .errors import AocError
from .errors import UserNotFoundError
from .errors import PuzzleNotStartedError 

class User:
    def __init__(self, session):
        self.session = session  

    @property
    def auth(self):
        return {"session": self.session}


def default_user():
    session = os.getenv("AOC_SESSION")
    if not session:
        raise UserNotFoundError("Session id not found")
    return User(session)


class Puzzle:
    def __init__(self, year, day, session=None):
        self.year = year
        self.day = day
        if session is None:
            user = default_user()
        else:
            user = User(session)
        self._user = user

    @property
    def url(self):
        return f"https://adventofcode.com/{self.year}/day/{self.day}"

    @property
    def user(self):
        return self._user
        
    @property
    def input(self):
        response = self._requestsGet(self.url+"/input")
        return str(response.text)

    @property
    def example(self):
        t = html.unescape(self._requestsGet(self.url).text)
        m = self._getCodes(t)
        if not m:
            raise AocError('Unexpected. Pattern did not appear in given url')
        return m 

    def _getCodes(self, html):
        r = lambda m: m.replace('\\n','\n')
        conf = r"(?<=your puzzle input).+?"
        patt = r"(?<=<pre><code>)(.*?)(?=</code></pre>)"
        matches = re.findall(re.compile(conf+patt), repr(html))
        if matches:
            return r(matches[0])
        print("WARNING: unable to find specific example. Getting all codes")
        matches = re.findall(re.compile(patt), repr(html))
        return [r(m) for m in matches]

    def _requestsGet(self, url):
        response = requests.get(
            url=url, cookies=self.user.auth, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        ) 
        if not response.ok:
            if response.status_code == 404:
                raise PuzzleNotStartedError("year {} day {:02d} has not started yet".format(self.year, self.day))
            raise AocError(f"Unexpected code {response.status_code}")
        return response 