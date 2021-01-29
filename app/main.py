import os

from flask import flash, Flask, render_template, request, redirect, url_for, send_file, after_this_request

app = Flask(__name__)
app.secret_key = b'mypass'

# ----------------------------------------------------------------------
# Top page
# ----------------------------------------------------------------------
@app.route('/')
def index():
    """
    Display the index page.

    Parameters
    ----------

    Returns
    -------
    render_template ： function
        Web page to display

    Notes
    -----
        This function is decorated app.route.
        Routing to '/' page.
    """
    return render_template(
        'index.html',
        title="AllrunExecuterWithOpenFOAM"
    )

# ----------------------------------------------------------------------
# What happens when you click the Execute Calculation button.
# ----------------------------------------------------------------------
@app.route('/run', methods=['POST'])
def runOpenFOAM():
    """
    Copy the inputs to the temp folder.
    Unzip the inputs.
    Run the calculation.

    Parameters
    ----------

    Returns
    -------
    redirect(url_for('index')) ： function
        Return to top page.

    Notes
    -----

    """
    import subprocess as sp
    import shutil
    import datetime

    now = datetime.datetime.now()
    timeStomp = now.strftime('%Y%m%d_%H%M%S')

    f = request.files['mesh']
    folder_path = os.path.join("/mnt", "windows", "case"+timeStomp)
    os.mkdir(folder_path)
    zip_path = os.path.join(folder_path, f.filename)
    f.save(zip_path)

    pwd = os.getcwd()

    try:
        os.chdir(folder_path)
        sp.check_call(["unzip", f.filename])
        sp.check_call(["rm", f.filename])
        sp.check_call(["chmod", "755", "Allrun"])
        sp.check_call(["bash", "-c",  """. /opt/openfoam7/etc/bashrc;./Allrun"""])
        os.chdir(pwd)
        flash("Success run.", 'info')
        flash("Please watch "+"case"+timeStomp, 'info')
    except:
        os.chdir(pwd)
        flash("Don't success run.", 'error')

    return redirect(url_for('index'))


# ----------------------------------------------------------------------
# main routine
# ----------------------------------------------------------------------
if __name__ == '__main__':
    installDir = os.getcwd()
    app.run(host='0.0.0.0', port=8080,
        debug=True, use_reloader=False, use_debugger=True)