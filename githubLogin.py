import random
import string

import aiohttp
from fastapi import APIRouter, Response

from CreateUser import create_user

GITHUB_CLIENT_ID = "Iv1.81842689e0b389e6"
GITHUB_CLIENT_SECRET = "004df390236ab86430408c842a48658d745471f6"
GITHUB_URL_ACCESS_TOKEN = "https://github.com/login/oauth/access_token"
GITHUB_URL_USER_INFO = "https://api.github.com/user"

routerGit = APIRouter()


def createRandomPass():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(12))
    return password


@routerGit.post("/registerGitHubUser")
async def get_github_access_token(code: str, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    async with aiohttp.ClientSession() as session:
        params = f"?client_id={GITHUB_CLIENT_ID}&client_secret={GITHUB_CLIENT_SECRET}&code={code}"
        async with session.post(GITHUB_URL_ACCESS_TOKEN + params,
                                headers={"Accept": "application/json"}) as resp:
            data = await resp.json()
            access_token = data.get("access_token", False)
            if access_token:
                access_token
            else:
                return data

        async with session.get(GITHUB_URL_USER_INFO,
                               headers={"Authorization": "Bearer " + access_token}) as resp:
            user_data = await resp.json()
            githubEmail = str(user_data["id"]) + "@github.com"
            avatarUrl = user_data["url"]
            randomPass = createRandomPass()
            await create_user(githubEmail, randomPass, avatarUrl, False)
