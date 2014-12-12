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
        links += "<td>View My Photos</td>\n"
        links += "<td>Upload a Photo</td>\n"
        links += "<td>Settings</td>\n"
    links += "<td>View List of Users</td>\n"
    if usr and usr != '':
        links += "<td><a href=main>Logout</a></td>\n"
    else:
        links += "<td><a href=login>Login</a></td>\n"
    links += """
    </tr>
    </table>
    """
    return links
def loginBox(usr, password):
    if usr == 'andrew' and password == '123':
        return """
        %s <a href=main?session=%s>click here</a> to go to home page!
        """ % (usr,usr), False
    return """
    <b>Login</b>
    <form method=post action='login'>
    User Name: <input type=text name=username /></br>
    Password: &nbsp;&nbsp;<input type=text name=password /></br>
    Do not have an account? <a href=register>Click here</a> to register.</br>
    <input type=submit value=Submit />
    </form>
    """, True
