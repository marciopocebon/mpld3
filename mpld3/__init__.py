__all__ = ["fig_to_d3"]

from ._objects import D3Figure

def fig_to_d3(fig):
    """Output d3 representation of the figure"""
    return D3Figure(fig).html()
