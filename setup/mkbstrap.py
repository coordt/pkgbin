import virtualenv, textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess
def adjust_options(options, args):
    options.unzip_setuptools = True
    options.use_distribute = True
    options.no_site_packages = True
    # options.relocatable = True # has to be done after everything is installed
    if not args:
        args.append('../virtualenv')
def after_install(options, home_dir):
    import os.path
    import subprocess
    requirements = os.path.join(os.path.dirname(home_dir), 'setup', 'requirements.txt')
    if os.path.exists(requirements):
        subprocess.call([os.path.join(home_dir, 'bin', 'pip'), 'install' , '-r', 'requirements.txt'])
"""))
f = open('bootstrap.py', 'w').write(output)
