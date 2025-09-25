import os
import streamlit.components.v1 as components
import streamlit as st

# Create a _RELEASE constant. We'll set this to False while developing
# the component, and True when we're ready to package and distribute it.
_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "crochet_design_tool",
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend")

    # Debug: Check if path exists
    if not os.path.exists(build_dir):
        st.error(f"Component frontend directory not found: {build_dir}")
        st.error(f"Parent dir: {parent_dir}")
        st.error(f"Files in parent: {os.listdir(parent_dir) if os.path.exists(parent_dir) else 'N/A'}")
    else:
        st.success(f"Component frontend directory found: {build_dir}")
        if os.path.exists(os.path.join(build_dir, "index.html")):
            st.success("index.html found")
        else:
            st.error("index.html not found")

    _component_func = components.declare_component("crochet_design_tool", path=build_dir)


def crochet_design_tool(key=None):
    """Create a new instance of "crochet_design_tool".

    Parameters
    ----------
    key : str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict
        The component's return value. This will be None until the user
        interacts with the component.

    """
    component_value = _component_func(key=key, default=None)
    return component_value