#!/usr/bin/env python
from SceneGraph.ui.node_widgets import NodeWidget


class MergeWidget(NodeWidget):
    widget_type  = 'merge'
    def __init__(self, dagnode, parent=None):
        NodeWidget.__init__(self, dagnode, parent)

