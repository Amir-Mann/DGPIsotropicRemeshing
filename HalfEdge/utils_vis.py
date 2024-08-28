import numpy as np
import plotly.graph_objs as go

def vis_he_trimesh(he_trimesh, wireframe=True, v_labels=True, e_labels=True, f_labels=True):
    # plot only referenced vertices, edges and faces
    V = he_trimesh.V
    F = he_trimesh.F
    vertices_d = he_trimesh.get_vertices()
    edge_midpoints_d = he_trimesh.get_edges_midpoints()
    face_midpoints_d = he_trimesh.get_faces_midpoints()

    fig = go.Figure()

    # Plot wireframe of the triangle mesh
    if wireframe:
        for f_idx, f_verts_inds in enumerate(F):
            if f_idx in he_trimesh.unreferenced_faces:
                continue
            i, j, k = f_verts_inds
            fig.add_trace(go.Scatter3d(x=[V[i, 0], V[j, 0], V[k, 0], V[i, 0]],
                                       y=[V[i, 1], V[j, 1], V[k, 1], V[i, 1]],
                                       z=[V[i, 2], V[j, 2], V[k, 2], V[i, 2]],
                                       mode='lines',
                                       line=dict(color='lightblue', width=2)))

    # Plot vertices with labels
    if v_labels:
        for idx, vertex in vertices_d.items():
            fig.add_trace(go.Scatter3d(x=[vertex[0]], y=[vertex[1]], z=[vertex[2]], mode='markers+text',
                                       text=[f'v{idx}'], textposition="top center", marker=dict(size=5, color='red')))

    # Plot edge midpoints with labels
    if e_labels:
        for he_idx, edge_midpoint in edge_midpoints_d.items():
            he_face_idx = he_trimesh.half_edges[he_idx].face
            twin_idx = he_trimesh.half_edges[he_idx].twin
            twin_face_idx = he_trimesh.half_edges[twin_idx].face
            he_string = "{},{}".format(he_idx, twin_idx) if he_face_idx < twin_face_idx else "{},{}".format(twin_idx, he_idx)
            fig.add_trace(go.Scatter3d(x=[edge_midpoint[0]], y=[edge_midpoint[1]], z=[edge_midpoint[2]], mode='markers+text', text=[he_string], textposition="top center", marker=dict(size=5, color='green')))

    # Plot face midpoints with labels
    if f_labels:
        for idx, face_midpoint in face_midpoints_d.items():
            fig.add_trace(go.Scatter3d(x=[face_midpoint[0]], y=[face_midpoint[1]], z=[face_midpoint[2]], mode='markers+text', text=[f"f{idx}"], textposition="top center", marker=dict(size=5, color='blue')))

    camera = dict(
        eye=dict(x=0., y=0., z=1.3),
        up=dict(x=0., y=1., z=0.),
    )
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode='data'),
        showlegend=False,
        scene_camera=camera,
        margin=dict(l=0, r=0, b=0, t=0)
    )
    fig.show()
