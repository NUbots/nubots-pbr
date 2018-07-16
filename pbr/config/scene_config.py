# Field-specific Configuration Settings
#   * All measurements are in metres

from math import pi
from os import path, pardir

# Get project path
proj_path = path.abspath(
    path.join(
        path.join(path.dirname(path.realpath(__file__)), pardir), pardir))

classes = {
    'unclassified': {
        'index': 0,
        'colour': (0., 0., 0., 1.)
    },
    'ball': {
        'index': 1,
        'colour': (1., 0., 0., 1.)
    },
    'field': {
        'index': 2,
        'colour': (0., 1., 0., 1.),
        'field_lines_colour': (1., 1., 1., 1.)
    },
    'goal': {
        'index': 3,
        'colour': (1., 1., 0., 1.)
    },
}

field = {
    'length': 9,
    'width': 6,
    'goal_area': {
        'length': 1,
        'width': 5
    },
    'penalty_mark_dist': 2.1,
    'centre_circle_radius': 0.75,
    'border_width': 0.7,
    'field_line_width': 0.05,
    'grass_height': 0.033,
}

goal = {
    'depth': 0.6,
    'width': 2.6,
    'height': 1.8,
    'post_width': 0.12,
    'shape': 'circular',
    'net_height': 1.2,
}

ball_radius = 0.5969 / (2 * pi)

ball = {
    'radius':
    ball_radius,
    'img_types': ['.jpg', '.png'],
    'mesh_types': ['.fbx', '.obj'],
    'ball_dir':
    path.abspath(path.join(path.join(proj_path, 'resources'), 'balls')),
    'limits': {
        'position': {
            'x': [-field['length'] / 2., field['length'] / 2.],
            'y': [-field['width'] / 2., field['width'] / 2.],
            'z': [ball_radius, ball_radius],
        },
        'rotation': {
            'pitch': [-180., 180.],
            'roll': [-180., 180.],
            'yaw': [-180., 180.],
        },
    }
}

camera = {
    'type': 'PANO',
    'cycles': {
        'type': 'FISHEYE'
    },
    'focal_length': 10.5,
    'fov': pi,
    'stereo_cam_dist': 0.1,
    'limits': {
        # Defines possible random placement range of x, y and z positional components
        'position': {
            'x': [-field['length'] / 2., field['length'] / 2.],
            'y': [-field['width'] / 2., field['width'] / 2.],
            'z': [0.8, 1.0],
        },
        # Rotation limits (degrees)
        'rotation': {
            'pitch': [30., 70.],
            'roll': [0., 360.],
            'yaw': [0., 10.],
        },
    },
}

field_uv = {
    'type':
    '.png',
    'mode':
    'RGBA',
    'pixels_per_metre':
    100,
    'uv_path':
    path.abspath(path.join(path.join(proj_path, 'resources'), 'field_uv')),
    'name':
    'default',
    'orientation':
    'portrait',
}

scene_hdr = {
    'path':
    path.abspath(path.join(path.join(proj_path, 'resources'), 'scene_hdr')),
}

##############################################
##         CONFIGURATION PROCESSING         ##
##############################################

# Create regex string suffix for image extensions
IMG_EXT = '('
for i in range(0, len(ball['img_types'])):
    IMG_EXT += '({0})'.format(ball['img_types'][i])
    if i + 1 < len(ball['img_types']):
        IMG_EXT += '|'
IMG_EXT += ')'

# Create regex string suffix for mesh extensions
MESH_EXT = '('
for i in range(0, len(ball['mesh_types'])):
    MESH_EXT += '({0})'.format(ball['mesh_types'][i])
    if i + 1 < len(ball['mesh_types']):
        MESH_EXT += '|'
MESH_EXT += ')'

# Establish regex strings for normals (norm, normal), colour (color(s), colour(s)) and mesh (*.fbx)
NORM_REGEX = r'(.*)norm(a?l?)(.*)' + IMG_EXT
COL_REGEX = r'(.*)col(u?)or(s?)(.*)' + IMG_EXT
MESH_REGEX = r'(.*)' + MESH_EXT