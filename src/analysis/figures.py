"""Contains functions to help with the creation of figures
in the analysis notebooks.
"""
import altair as alt
from pathlib import Path


def format_chart(chart):
    """Sets size of chart and fontsize of axis and legend

    Parameters
    ----------
    chart : alt.Chart
        Chart which should be configured

    Returns
    -------
    alt.Chart
        Chart with set size and fontsize
    """
    return chart.properties(
        width=600, height=400).configure_axis(
            labelFontSize=12, titleFontSize=12).configure_legend(
                labelFontSize=12, titleFontSize=12)


def save_to_jekyll(chart, name, reverse_colors=False):
    """Converts chart to html representation and adds it to
    the correct folder.

    Parameters
    ----------
    chart : alt.Chart
        Chart which should be configured

    name : str
        Name of the chart. Upon saving, ".html" will be
        automatically appended.

    reverse_colors : boolean, optional (default=False)
        If True, reverses the color scheme "redyellowgreen".
        ATTENTION: This only works for the beforementioned scheme.
        For any other scheme nothing will happen.
        This seems to be not yet possible directly in Altair and might
        change in future versions.

    Returns
    -------
    Nothing
    """
    body = f'<div id="{name}"></div>'
    body += '\n<script type="text/javascript">'
    body += f'\nvar spec = {chart.to_dict()};'
    body += '\nvar embed_opt = {"mode": "vega-lite"};'
    body += f"""vegaEmbed("#{name}", spec, embed_opt)
      .catch(console.error);
    </script>
    """

    # Fix issues with javascript not recognizing True, False and None
    body = body.replace('True', '"True"')
    body = body.replace('False', '"False"')
    body = body.replace('None', 'null')
    if reverse_colors:
        body = body.replace(
            "'scale': {'scheme': 'redyellowgreen'}",
            "'scale': {'scheme': 'redyellowgreen', 'reverse': 'True'}")
    with Path(f'../../docs/_includes/{name}.html').open('w') as f:
        f.write(body)
    return
