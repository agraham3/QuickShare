def header():
    return """
    <head>
    <h1 align=center>Quick Share</h1>
    <hr>
    </head>
    """
def topLinks(usr = None):
    to_add = ''
    if usr and usr != '':
        to_add = '?session=' + usr
    links = """
    <table cellpadding=8>
    <tr>
    <td><a href=main%s>Home</a></td>""" % to_add
    if usr and usr != '':
        links += "<td><a href=viewPhotos%s>View My Photos</a></td>\n" % to_add
        links += "<td><a href=uploadPhoto%s>Upload a Photo</a></td>\n" % to_add
        links += "<td><a href=settings%s>Settings</a></td>\n" %to_add
    links += "<td><a href=viewListOfUsers%s>View List of Users</a></td>\n" % to_add
    if usr and usr != '':
        links += "<td><a href=main>Logout</a></td>\n"
    else:
        links += "<td><a href=login>Login</a></td>\n"
    links += """
    </tr>
    </table>
    """
    return links
def loginBox(usr, password, dbpass):
    if usr and password == dbpass:
        return """
        %s <a href=main?session=%s>click here</a> to go to home page!
        """ % (usr,usr), False
    return """
    <b>Login</b>
    <form method=post action='login'>
    User Name: <input type=text name=username /></br>
    Password: &nbsp;&nbsp;<input type=password name=password /></br>
    Do not have an account? <a href=register>Click here</a> to register.</br>
    <input type=submit value=Submit />
    </form>
    """, True
