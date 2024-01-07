from datascience import GitHubAPI

def test_github_api():
    api = GitHubAPI()
    user = api.get_github_user('karpathy')
    expected_user = {}
    expected_user.update({
        'login':'karpathy',
        'html_url':'https://github.com/karpathy',
        'url':"https://api.github.com/users/karpathy",
        "followers":59766,
        'following':7
    })
    assert user['login']==expected_user['login'],'login doesnt match'
    assert user['html_url']==expected_user['html_url'],'html_url doesnt match'
    assert user['url']==expected_user['url'],'url doesnt match'
    assert user['followers']==expected_user['followers'],'followers doesnt match'
    assert user['following']==expected_user['following'],'following doesnt match'
    
    
    
    
    