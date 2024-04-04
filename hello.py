from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


import base64
from io import StringIO

import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import numpy as np
import xml.etree.ElementTree as ET

svg = 'opg1_red_rgb_alz_p0405.svg'
tree = ET.parse('opg1_red_rgb_alz_p0405.svg')
root = tree.getroot()

def svg_write(fig, center=True):
    """
    Renders a matplotlib figure object to SVG.
    Disable center to left-margin align like other objects.
    """
    # Save to stringIO instead of file
    imgdata = StringIO()
    fig.savefig(imgdata, format="svg")

    # Retrieve saved string
    imgdata.seek(0)
    svg_string = imgdata.getvalue()

    # Encode as base 64
    b64 = base64.b64encode(svg_string.encode("utf-8")).decode("utf-8")

    # Add some CSS on top
    css_justify = "center" if center else "left"
    css = '<p style="text-align:center; display: flex; justify-content: {};">'.format(css_justify)
    html = r'{}<img src="data:image/svg+xml;base64,{}"/>'.format(
        css, b64
    )

    # Write the HTML
    st.write(html, unsafe_allow_html=True)

def svg_display(svg_string):
    """
    Renders a matplotlib figure object to SVG.
    Disable center to left-margin align like other objects.
    """
   
    # Encode as base 64
    b64 = base64.b64encode(svg_string.encode("utf-8")).decode("utf-8")

    # Add some CSS on top
    css_justify = "center" if center else "left"
    css = '<p style="text-align:center; display: flex; justify-content: {};">'.format(css_justify)
    html = r'{}<img src="data:image/svg+xml;base64,{}"/>'.format(
        css, b64
    )

    # Write the HTML
    st.write(html, unsafe_allow_html=True)
    
if __name__ == "__main__":
    fig, ax = plt.subplots(nrows=5, ncols=5, figsize=(10, 10))
    ax = ax.ravel()

    for i in range(len(ax)):
        x = np.arange(0, np.pi * np.random.randint(2, 10), 0.1)
        y = np.sin(x)

        ax[i].plot(x, y)

    plt.tight_layout()

    st.subheader("Peasant pixels")
    st.write(fig)

    st.subheader("Glorious SVG")
    svg_display(svg)



def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

render_svg(svg)


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)


# from pyecharts import options as opts
# from pyecharts.charts import Map
# from pyecharts.faker import Faker

# c = (
#     Map()
#     .add("A", [list(z) for z in zip(Faker.country, Faker.values())], "world")
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="Map-X"),
#         visualmap_opts=opts.VisualMapOpts(max_=200),
#     )
#     .render("map_world.html")
# )

# st_pyecharts(c)

# # with open("./data/countries.geo.json", "r") as f:
# #     map = st_Map("world", json.loads(f.read()),)
# # c = Map(init_opts=opts.InitOpts(bg_color="white"))
# # c.add("Demo", [list(z) for z in zip(Faker.country, Faker.values())], "world")
# # c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# # c.set_global_opts(
# #     title_opts=opts.TitleOpts(title="Map world"),
# #     visualmap_opts=opts.VisualMapOpts(max_=200),
# # )
# #st_pyecharts(c, map=map, height=500)
