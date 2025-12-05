# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ISIF/CSIF FOOD'
copyright = 'Smart Sensor Fusion Laboratory'


author = 'Smart Sensor Fusion Laboratory'

release = '2.01'
version = '2.01'


# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# html_static_path = '_static'

# -- Options for EPUB output
epub_show_urls = 'footnote'


bibtex_bibfiles = ['refs.bib']


#used for videos
import os
import shutil

def setup(app):
    app.connect('build-finished', copy_videos)

def copy_videos(app, exception):
    if exception is None:  # build succeeded
        # Define the source and destination paths
        source_video_path = os.path.join(app.srcdir, 'videos')
        dest_video_path = os.path.join(app.outdir, '_static', 'videos')
        
        # Create destination directory if it does not exist
        if not os.path.exists(dest_video_path):
            os.makedirs(dest_video_path)
        
        # Copy video files from source to destination
        for file_name in os.listdir(source_video_path):
            full_file_name = os.path.join(source_video_path, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest_video_path)